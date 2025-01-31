from django.urls import include, path

import app.views.home as home
import app.views.task_2 as task_2
import app.views.task_3 as task_3
import app.views.task_4 as task_4
import app.views.task_5 as task_5
import app.views.task_7 as task_7

urlpatterns = [
    path(
        "",
        home.home,
        name="index",
    ),
    path(
        "task2/page1",
        task_2.first_GET_request,
        name="first_GET_request",
    ),
    path(
        "task2/page2",
        task_2.second_GET_request,
        name="second_GET_request",
    ),
    path(
        "task2/page3",
        task_2.first_POST_request,
        name="first_POST_request",
    ),
    path(
        "task3/page1",
        task_3.first_POST_request,
        name="first_POST_request.task3",
    ),
    path(
        "task4/login",
        task_4.login,
        name="login.task4",
    ),
    path(
        "task4/register",
        task_4.register,
        name="register.task4",
    ),
    path(
        "task5/",
        include(task_5.router.urls),
    ),
    path(
        "task7/login",
        task_7.login,
        name="task7.login",
    ),
    path(
        "task7/recovery",
        task_7.recovery,
        name="task7.recovery",
    ),
    path(
        "task7/recovery/new_pass",
        task_7.recovery_new_pass,
        name="task7.recovery_new_pass",
    ),
    path(
        "task7/register",
        task_7.registration,
        name="task7.registration",
    ),
    path(
        "task7/profile",
        task_7.user_profile,
        name="task7.profile",
    ),
    path(
        "task7/profile/logout",
        task_7.logout,
        name="task7.logout",
    ),
]
