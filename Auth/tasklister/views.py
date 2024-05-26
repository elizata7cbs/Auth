from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password
from tasklister.serializers import UserSerializer, TaskSerializer
from tasklister.models import User, Task
from rest_framework.decorators import permission_classes


# Create your views here.
def index(request):
    return HttpResponse("Good morning, Elizabeth.")


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def register_user(request):
    data = request.data
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')

    # Check if the email already exists
    email_count = User.objects.filter(email=email).count()
    if email_count > 0:
        return Response({'error': 'Email already exists'}, status=400)

    # Check if the username already exists
    username_count = User.objects.filter(username=username).count()
    if username_count > 0:
        return Response({'error': 'Username already exists'}, status=400)

    # Create the user
    user = User.objects.create_user(email=email, password=password, username=username)

    # Serialize and save the user
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save(
            username=username,
            email=email,
            password=make_password(password)
        )
        return Response({'success': 'User created successfully'}, status=201)
    else:
        return Response(serializer.errors, status=400)


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_task(request):
    data = request.data
    title = data.get('title')
    description = data.get('description')

    # Serialize and save the task
    serializer = TaskSerializer(data=data)
    if serializer.is_valid():
        serializer.save(
            title=title,
            description=description,
        )
        return Response({'success': 'Task created successfully'}, status=201)
    else:
        return Response(serializer.errors, status=400)
