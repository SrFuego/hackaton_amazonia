# Python imports


# Django imports
from django.contrib.auth.models import update_last_login


# Third party apps imports
from rest_framework import parsers, renderers, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


# Local imports


# Create your views here.
class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (
        parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        update_last_login(None, user)
        token, created = Token.objects.get_or_create(user=user)
        try:
            account = user.account
            if account.level == "operator":
                return Response({
                    "account_id": account.id,
                    "account_level": account.level,
                    "protected_natural_area": {
                        "id": account.protected_natural_area.id,
                        "name": account.protected_natural_area.name
                    },
                    "token": token.key
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "account_id": account.id,
                    "account_level": account.level,
                    "token": token.key
                }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
