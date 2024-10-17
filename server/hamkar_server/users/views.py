from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.views import Response
from .models import CustomUser
from .serializers import   CustomUserSerializer,UserRegisterSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class =CustomUserSerializer 

    def get_permissions(self):
        if self.action in ['create']:
            return [AllowAny()]  
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'status': 'User created', 'user_id': user.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
