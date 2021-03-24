from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from br.forms.user import LoginForm, RegisterForm


def sign_in(request):

    form = RegisterForm(request.POST or None)

    if form.is_valid():
        form.save()

        return redirect('br:login')

    context = {
        'form': form,
    }

    return render(request, 'br/accounts/sign_in.html', context)


def log_in(request):

    form = LoginForm()

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_staff:
                return redirect('/')

            return redirect('br:requirement-edit')

    context = {
        'form': form,
    }

    return render(request, 'br/accounts/login.html', context)


def log_out(request):

    logout(request)

    return redirect('br:login')  # 重新導向到登入畫面
