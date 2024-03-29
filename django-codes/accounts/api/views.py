from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from drf_yasg.utils import swagger_auto_schema
from accounts.api.serializers import UserProfileTokenSerializer


class UserTokenView(TokenObtainPairView):
    @swagger_auto_schema(responses={200: UserProfileTokenSerializer(many=True)})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)