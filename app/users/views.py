from djoser.views import UserViewSet

from .serializers import UserSerializer
from posts.models import User


class CustomView(UserViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()