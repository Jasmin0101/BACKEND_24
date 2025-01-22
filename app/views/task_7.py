from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect, render
import json

from app.models import User


@require_http_methods(["GET", "POST"])
def login(request):

    if request.method == "POST":

        # Получаем email и пароль из формы
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Пытаемся найти пользователя в базе данных
        try:
            user = User.objects.get(email=email)
            # Сравниваем введенный пароль с паролем пользователя
            if user.password == password:  # В реальной жизни используйте хеширование
                # Создаем сессию или аутентификацию для пользователя (например, через куки)
                response = redirect("/dashboard")
                response.set_cookie("auth_token", "some_auth_token_value")
                return response
            else:
                # Если пароль неправильный, возвращаем ошибку
                return render(
                    request,
                    "app/task7/login.html",
                    {"error_message": "Неверный пароль"},
                )
        except User.DoesNotExist:

            return render(
                request,
                "app/task7/login.html",
                {"error_message": "Пользователь с таким email не найден"},
            )

    # Для GET запроса просто отображаем форму
    return render(request, "app/task7/login.html")
