from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.views.decorators.csrf import csrf_exempt

favorite = []


# def first_GET_request(request):

#     return render(
#         request,
#         "app/task3/page1.html",
#         {"favorite": favorite},
#     )


def first_POST_request(request):
    if request.method == "POST":
        name = request.POST.get("name")
        favorite.append(name)
        return redirect("/task3/page1")

    if request.method == "GET":
        return render(
            request,
            "app/task3/page1.html",
            {"favorite": favorite},
        )
