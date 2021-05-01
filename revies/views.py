from django.shortcuts import render, redirect
from revies.forms import Revies_form, sh_form
# Create your views here.
def Revies(request):
    if request.method == "GET":
        form = Revies_form()
        # showform = Show_form()
        return render(request, "index.html", {"form":form})
    elif request.method == "POST":
        form = Revies_form(request.POST)
        # showform = Show_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data.get("name")
            email = data.get("email")
            review = data.get("review")
            with open("../data.csv", "a") as file:
                file.write(f"{name}|{email}|{review}\n")
            return redirect(Revies)
        else:
            form = Revies_form()
            # showform = Show_form()
            return render(request, "index.html", {"form": form})
def Showrev(request):
    if request.method == "GET":
        form = sh_form
        return render(request, "index.html", {"form": form})
    elif request.method == "POST":
        form = sh_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            rating = data.get("rating")
            with open("../data.csv", "a") as file:
                file.write(f"{rating}\n")
            return redirect(Showrev)
        else:
            form = sh_form()
            return render(request, "index.html", {"form": form})