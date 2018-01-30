from users.models import User
from rest_framework import generics
from users.serializers import UserSerializer
from rest_framework import permissions
from users.permissions import IsOwnerOrReadOnly


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    # def get_queryset(self):
    #     return User.objects.all().filter(username=self.request.user)