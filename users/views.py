from users.models import User
from rest_framework import generics
from users.serializers import UserSerializer
from rest_framework import permissions
from rest_framework import authentication
from users.permissions import IsOwnerOrReadOnly


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    authentication_classes = (authentication.SessionAuthentication, authentication.BasicAuthentication,authentication.TokenAuthentication )
    # permission_classes = (permissions.IsAuthenticated,)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    authentication_classes = (
        authentication.SessionAuthentication, authentication.BasicAuthentication, authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    # def get_queryset(self):
    #     return User.objects.all().filter(username=self.request.user)
