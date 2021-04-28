from django.shortcuts import render, redirect
from revies.forms import Revies_form
# Create your views here.
def Revies(request):
    if request.method == "GET":
        form = Revies_form()
        return render(request, "index.html", {"form":form})
    elif request.method == "POST":
        form = Revies_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data.get("name")
            email = data.get("email")
            review = data.get("review")
            with open("../data.csv", "a") as file:
                file.write(f"{name}|{email}|{review}\n")
            return redirect("")
        else:
            form = Revies_form()
            return render(request, "index.html", {"form": form})
