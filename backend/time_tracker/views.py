from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Act_type, Act_name, Date, Time
from .serializers import (ActTypeSerializer, 
                          ActNameSerializer, 
                          DateSerializer, 
                          TimeSerializer) 

from django.utils import timezone
from django.db.models import Q

def filter_record(user_id, start_date,end_date, act_type, act_name):
    # Filter the data based on the provided parameters
    data = Act_name.objects.filter(
        Q(act_type__user=user_id) &
        Q(date__range=(start_date, end_date)) &
        Q(act_type=act_type) &
        Q(act_name=act_name)
    )
    return data

TODAY = timezone.now().date()

 

class Dashboard_view(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user_id = request.user.id
        act_types = Act_type.objects.filter(user=user_id)
        act_names = Act_name.objects.filter(act_type__user=user_id)
        records_today = Time.objects.filter(Q(date__user = user_id) & 
                                            Q(date__date = TODAY))
        act_types_serializer = ActTypeSerializer(act_types, many=True)
        act_name_serializer = ActNameSerializer(act_names, many=True)
        records_serializer = TimeSerializer(records_today, many=True)
        
        return Response({
            'act_types': act_types_serializer.data,
            'act_name': act_name_serializer.data,
            'records_today': records_serializer.data,
        }, status=status.HTTP_200_OK)
        

    def post(self, request):
        # Check if all required fields are present in the request
        required_fields = ['date', 'start_time', 'end_time', 'act_type', 'act_name', 'notes']
        if not all(field in request.data for field in required_fields):
            return Response({'detail': 'Missing required field(s).'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            date_data = {
                'user': request.user.id,
                'date': request.data.get('date'),
            }
            time_data = {
                'date' : None,
                'start_time': request.data.get('start_time'),
                'end_time': request.data.get('end_time'),
                'act_type': request.data.get('act_type'),
                'act_name': request.data.get('act_name'),
                'notes': request.data.get('notes'),
            }
            # Save the date data
            date_serializer = DateSerializer(data=date_data)
            if date_serializer.is_valid():
                date = date_serializer.save()
                
                # Save the time data
                time_data['date'] = date.id
                time_serializer = TimeSerializer(data=time_data)
                if time_serializer.is_valid():
                    time_serializer.save()
                    return Response(status=status.HTTP_201_CREATED)
                else:
                    return Response(time_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(date_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Act_type_view(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        user_id = request.user.id
        act_types = Act_type.objects.filter(user=user_id)
        act_types_serializer = ActTypeSerializer(act_types, many=True)
        return Response(act_types_serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        act_type_serializer = ActTypeSerializer(data=request.data)
        if act_type_serializer.is_valid():
            act_type_serializer.save()
            return Response(act_type_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(act_type_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        act_type = Act_type.objects.get(pk=pk)
        act_type_serializer = ActTypeSerializer(act_type, data=request.data)
        if act_type_serializer.is_valid():
            act_type_serializer.save()
            return Response(act_type_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(act_type_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        act_type = Act_type.objects.get(pk=pk)
        act_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class Act_name_view(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        user_id = request.user.id
        act_name = Act_name.objects.filter(act_type__user=user_id)
        act_name_serializer = ActNameSerializer(act_name, many=True)
        return Response(act_name_serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        act_name_serializer = ActNameSerializer(data=request.data)
        if act_name_serializer.is_valid():
            act_name_serializer.save()
            return Response(act_name_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(act_name_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        act_name = Act_name.objects.get(pk=pk)
        act_name_serializer = ActNameSerializer(act_name, data=request.data)
        if act_name_serializer.is_valid():
            act_name_serializer.save()
            return Response(act_name_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(act_name_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        act_name = Act_name.objects.get(pk=pk)
        act_name.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Record_view(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user_id = request.user.id
        records = Time.objects.filter(date__user=user_id)
        records_serializer = TimeSerializer(records, many=True)
        return Response(records_serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        pass
    def delete(self, request, pk):
        pass


'''

CRUD Task_type, Task_name by User ID


Post data (update or create)


filter



'''