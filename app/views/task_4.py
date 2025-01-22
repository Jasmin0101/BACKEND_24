import json
from django.http import (
    HttpRequest,
    HttpResponseBadRequest,
    HttpResponseNotAllowed,
    JsonResponse,
    HttpResponse,
)
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password, make_password

from app.models import *

from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.http import require_http_methods


@require_http_methods(["POST"])
def login(request):
    data = json.loads(request.body)
    email = data.get("email")
    password = data.get("password")

    # Проверка наличия email и пароля
    if not email or not password:
        return HttpResponseBadRequest("Login and password are required.")

    try:
        # Ищем пользователя по email
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return HttpResponseBadRequest("User not found.")

    # Проверяем пароль
    if not check_password(password, user.password):
        return HttpResponseBadRequest("Invalid password.")

    refresh = RefreshToken.for_user(user)

    # Возвращаем успешный ответ
    return JsonResponse(
        {
            "message": "Login successful.",
            "access_token": str(refresh.access_token),
        }
    )
