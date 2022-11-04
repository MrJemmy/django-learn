from django.shortcuts import (
    render,
    redirect
)
from django.contrib.auth import (
    authenticate,
    login,
    logout
)

# Create your views here.
def login_view(request):
    # if request.user.is_authenticated:
    #     return render(request, "accounts/already-logged-in.html", context={})
    if request.method == "POST":
        login_dict = request.POST
        username = login_dict.get('username')
        password = login_dict.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {
                "error" : "Invalid username or password"
            }
            return render(request, "accounts/login.html", context=context)
        login(request, user)

        next_url = request.GET.get('next')
        if next_url is not None:
            return redirect(next_url)

        return redirect('/')
    return render(request, "accounts/login.html", context={})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('/login')
    return render(request, "accounts/logout.html", context={})

def register_view(request):
    return render(request, "accounts/register.html", context={})
