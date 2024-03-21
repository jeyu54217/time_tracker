import requests
# django
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
# DRF
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# JWT
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.backends import TokenBackend
# serializers
from .serializers import UserRegistrationSerializer


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Deactivate account till it is verified
            user.is_active = False 
            user.save()
            # Generate JWT for the user
            token = RefreshToken.for_user(user) 
            # Generate Verification URL
            verify_url = f"{request.build_absolute_uri(reverse('verify_email'))}?token={token.access_token}"
            # Email contents
            email_data = {'email_subject': 'Verify your email',
                    'html_message':f"""
                        <h2>Please verify your email: </h2>
                        <h3>Hi {user.username},</h3>
                        <p>Click the link below to verify your email :</p>
                        <p><a href={verify_url}><strong>Verify Email</strong></a></p>
                        """,
                    'to_email': user.email, 
                }
            # Send email to the user
            send_mail(
                subject = email_data['email_subject'],
                message = "",
                from_email = settings.EMAIL_HOST_USER,
                recipient_list = [email_data['to_email']],
                fail_silently = False,
                html_message = email_data['html_message']
                )
            return Response(serializer.data, 
                            status = status.HTTP_201_CREATED)
        return Response(serializer.errors, 
                        status = status.HTTP_400_BAD_REQUEST)


class VerifyEmailView(APIView):
    def get(self, request):
        try:
            # Get token from the URL
            token = request.GET.get('token')
            # Decode the token
            token_backend = TokenBackend(algorithm = settings.SIMPLE_JWT['ALGORITHM'])
            valid_data = token_backend.decode(token, verify=False)
            # Validate the user and activate the account
            user_id = valid_data['user_id']
            user = User.objects.get(id=user_id)
            if not user.is_active:
                user.is_active = True
                user.save()
                return Response(
                    {'email': 'Successfully activated'}, 
                    status = status.HTTP_200_OK
                    )
            else:
                return Response(
                    {'email': 'User already activated'}, 
                    status = status.HTTP_200_OK
                    )
        except (InvalidToken, TokenError, User.DoesNotExist) as e:
            return Response(
                {'error': 'Invalid token or user does not exist'}, 
                status = status.HTTP_400_BAD_REQUEST
                )

class GoogleOAuth2CallbackView(APIView):
    def get(self, request):
        code = request.GET.get('code')
        url = 'https://oauth2.googleapis.com/token'
        data = {
            'code': code,
            'client_id': settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY,
            'client_secret': settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET,
            'redirect_uri': 'http://127.0.0.1:8100/auth/google/callback',
            'grant_type': 'authorization_code',
        }
        r = requests.post(url, data=data)
        # Get access_token from the response
        access_token = r.json().get('access_token')
        # Use access_token to retrieve user's profile from google
        profile_url = 'https://www.googleapis.com/oauth2/v1/userinfo'
        headers = {'Authorization': f'Bearer {access_token}'}
        profile_response = requests.get(profile_url, headers=headers)
        profile_data = profile_response.json() 
        
        # Get or create user in the db using google profile data
        user, created = User.objects.get_or_create(
            username = profile_data['email'],
            defaults={
                'username': profile_data['email'],
                'first_name': profile_data['given_name'],
                'last_name': profile_data['family_name']
            })
        # Generate JWT token
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        # If user is created, set unusable password for the user
        if created:
            user.set_unusable_password()  
            user.save()
            return Response({'access_token': access_token, 
                             'user_id': user.id,
                             'msg': 'Oauth2, New user created successfully',},
                            status=status.HTTP_200_OK)
        else:
            return Response({'access_token': access_token, 
                            'user_id': user.id,
                            'msg': 'Oauth2, User log in successfully',}, 
                            status=status.HTTP_200_OK)

class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username).first()
        if user is None or not user.check_password(password):
            return Response(
                {'msg': 'Invalid username or password'},
                status=status.HTTP_401_UNAUTHORIZED)
        elif not user.is_active:
            return Response(
                {'msg': 'User is not active'},
                status=status.HTTP_401_UNAUTHORIZED)
        else:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response(
                {'access_token': access_token,
                 'msg': 'User log in successfully'},
                status=status.HTTP_200_OK)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Get the refresh token from request data
            refresh_token = request.data.get('refresh_token')
            token = RefreshToken(refresh_token)
            # Attempt to blacklist the given token
            token.blacklist()
            return Response({'msg': 'Logout successful.'}, status=status.HTTP_205_RESET_CONTENT)
        except (TokenError, InvalidToken):
            return Response({'msg': 'Bad token.'}, status=status.HTTP_400_BAD_REQUEST)


