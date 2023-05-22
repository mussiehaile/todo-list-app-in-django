from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from rest_framework.permissions import IsAuthenticated,AllowAny

from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import AccountSerializer, CustomUserSerializer
from.models import Account

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save(username=request.data.get('username'))
        # Perform additional tasks if needed
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_accounts(request):
    accounts = Account.objects.all()
    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_user_detail(request, user_id):
    try:
        user = Account.objects.get(id=user_id)
        serializer = AccountSerializer(user)
        return Response(serializer.data)
    except Account.DoesNotExist:
        return Response({'error': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)

# Your other views...
@api_view(['GET', 'PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def user_profile(request):
    if request.method == 'GET':
        # Retrieve the user profile
        user = request.user
        serializer = AccountSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        # Update the user profile
        user = request.user
        serializer = AccountSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
