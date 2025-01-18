from django.http import HttpResponse
from django.shortcuts import redirect, render


def first_GET_request(request):
    return render(request, "app/task2/page1.html", {})


def second_GET_request(request):
    # if request.POST:
    return render(request, "app/task2/page2.html", {})
    # return HttpResponse("I'm  Get request")


def first_POST_request(request):
    if request.method == "POST":

        name = request.POST.get("name", "No Name")

        request.session["user_name"] = name

        return render(request, "app/task2/page3.html", {"name": name})

    else:
        # Если запрос не POST, перенаправляем на страницу с формой
        return redirect("second_GET_request")
