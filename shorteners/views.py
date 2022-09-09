from django.shortcuts import render, redirect

from shorteners.models import Users

# Create your views here.


def index(request):
    user = Users.objects.filter(username="admin").first()
    email = user.email if user else "Anonymous User!"
    print(email)
    print(request.user.is_authenticated)
    if not request.user.is_authenticated:
        email = "Anonymous User@"
    print(email)

    return render(request, "base.html", {"welcome_msg": f"Hello {email}"})


def redirect_test(request):
    print("GO Redirect")
    return redirect("index")
