
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import accountform
from django.contrib import messages






def account_view(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = accountform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f"Your account has been created! You are now able to log in")
            return redirect('account-user_login')

    else:
        form = accountform()
    context = {
        "form": form
    }
    return render(request, "accounts/account-user_register.html", context)



