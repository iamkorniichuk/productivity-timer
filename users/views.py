from rest_framework import generics

from .serializers import UserSerializer
from .models import User


class CurrentUserDetail(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user
