import json
from django.http import (
    HttpRequest,
    HttpResponseBadRequest,
    HttpResponseNotAllowed,
    JsonResponse,
    HttpResponse,
)


from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password, make_password
from django.views.decorators.http import require_http_methods


from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from app.models import User
from app.sender import send_email


@require_http_methods(["GET", "POST"])
@csrf_exempt
def login(request):

    if request.method == "POST":

        # Получаем email и пароль из формы
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Пытаемся найти пользователя в базе данных
        try:
            user = User.objects.get(email=email)
            # Сравниваем введенный пароль с паролем пользователя
            if check_password(password, user.password):
                response = redirect("/task7/profile")

                refresh = RefreshToken.for_user(user)
                response.set_cookie("auth_token", refresh)
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

    if request.GET.get("error_message"):
        return render(
            request,
            "app/task7/login.html",
            {"error_message": request.GET.get("error_message")},
        )
    return render(request, "app/task7/login.html")


# @require_http_methods(["POST"])
@csrf_exempt
def registration(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Проверка наличия всех обязательных полей
        if not all([email, password]):
            return render(
                request,
                "app/task7/register.html",
                {"error_message": "Введите email и пароль"},
            )

        # Проверка уникальности emailS
        if User.objects.filter(email=email).exists():
            return render(
                request,
                "app/task7/register.html",
                {"error_message": "Пользовтель с таким email уже существует"},
            )

        user = User.objects.create(
            email=email,
            password=make_password(password),  # Хэширование пароля
        )
        response = redirect("/task7/profile")

        refresh = RefreshToken.for_user(user)
        response.set_cookie("auth_token", refresh)
        return response
    if request.method == "GET":
        return render(
            request,
            "app/task7/register.html",
        )


@csrf_exempt
def user_profile(request):

    try:
        token = request.COOKIES.get("auth_token")

        user = RefreshToken(token)
        user_id = user.payload.get("user_id")
    except Exception as e:
        return redirect("/task7/login?error_message=ERROR")

    if request.method == "GET":

        user = User.objects.get(id=int(user_id))

        return render(request, "app/task7/profile.html", {"email": user.email})

    if request.method == "POST":

        new_email = request.POST.get("email")

        print(new_email)

        if not new_email:
            return redirect("/task7/profile")

        user = User.objects.get(id=int(user_id))

        user.email = new_email
        user.save()

        return redirect("/task7/profile")


@csrf_exempt
def recovery(request):

    if request.method == "GET":

        return render(request, "app/task7/recovery.html")

    if request.method == "POST":

        email = request.POST.get("email")

        if not email:
            return render(
                request,
                "app/task7/recovery.html",
                {"error_message": "Данный email не существует в системе"},
            )

        user = User.objects.filter(email=email).first()

        if not user:
            return render(
                request,
                "app/task7/recovery.html",
                {"error_message": "Данный email не существует в системе"},
            )

        refresh = RefreshToken.for_user(user)
        send_email(
            "Восстановление пароля",
            f"Ссылка для восстановления: /recovery/new_pass?token={refresh} ",
            user.email,
        )

        return render(
            request,
            "app/task7/recovery.html",
            {"error_message": "Ссылка отправлена на ваш email"},
        )


@csrf_exempt
def recovery_new_pass(request):

    try:
        token = request.GET.get("token")

        user = RefreshToken(token)
        user_id = user.payload.get("user_id")
    except Exception as e:
        return redirect("/task7/login?error_message=ERROR")

    if request.method == "GET":

        user = User.objects.get(id=int(user_id))

        return render(request, "app/task7/recovery_new_password.html")

    if request.method == "POST":

        password = request.POST.get("password")

        if not password:
            return render(
                request,
                "app/task7/recovery_new_password.html",
                {"error_message": "Введите пароль"},
            )

        user = User.objects.get(id=int(user_id))

        user.password = (make_password(str(password)),)
        user.save()

        response = redirect("/task7/profile")

        refresh = RefreshToken.for_user(user)
        response.set_cookie("auth_token", refresh)
        return response


@csrf_exempt
def logout(request):

    response = redirect("/task7/login")
    response.delete_cookie("auth_token")

    return response
