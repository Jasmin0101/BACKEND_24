from django.urls import path
import app.views.task_3 as task_3
import app.views.task_2 as task_2


urlpatterns = [
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
    # path(
    #     "task3/page1",
    #     task_3.first_GET_request,
    #     name="first_GET_request.task3",
    # ),
    path(
        "task3/page1",
        task_3.first_POST_request,
        name="first_POST_request.task3",
    ),
]
