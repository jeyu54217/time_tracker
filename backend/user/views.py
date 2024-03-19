from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from .serializers import UserRegistrationSerializer

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.backends import TokenBackend

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
            data = {
                'email_subject': 'Verify your email',
                'html_message': f"""
                                <h2>Please verify your email: </h2>
                                <h3>Hi {user.username},</h3>
                                <p>Click the link below to verify your email :</p>
                                <p><a href={verify_url}><strong>Verify Email</strong></a></p>
                                """,
                'to_email': user.email, 
                }
            
            # Send email to the user
            send_mail(
                subject = data['email_subject'],
                message = "",
                from_email = settings.EMAIL_HOST_USER,
                recipient_list = [data['to_email']],
                fail_silently = False,
                html_message = data['html_message']
                )
            
            return Response(serializer.data, 
                            status = status.HTTP_201_CREATED
                            )
        return Response(serializer.errors, 
                        status = status.HTTP_400_BAD_REQUEST
                        )


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
