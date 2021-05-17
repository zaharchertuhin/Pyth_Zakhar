from django.shortcuts import render, redirect
from revies.forms import Revies_form
from revies.models import Review
# Create your views here.
def Revies(request):
    if request.method == "POST":
        form = Revies_form(request.POST)
        # showform = Show_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data.get("name")
            email = data.get("email")
            review = data.get("revies")
            rating = data.get("rating")
            # with open("./data.csv", "a", encoding='cp1251') as file:    #добавил encoding
            #     file.write(f"{name}|{email}|{review}\n")
            Review.objects.create(name=name, email=email, revies=review, rating=rating)
            return redirect(Revies)
        form = Revies_form()
        Revies_1 = Review.objects.get(id=1)
        print(Revies_1.name)
        return render(request, "index.html", {"form": form}, {"Revies_1":Revies_1})

    # with open("./data.csv") as file:
    #     revies = file.readlines()
    # if len(revies) > 0:
    #     revies_1 = revies[-1]
    #     name_1 = revies_1.split("|")[0]
    #     email_1 = revies_1.split("|")[1]
    #     review_1 = revies_1.split("|")[2]
    # else:
    #     name_1 = ""
    #     email_1 = ""
    #     review_1 = ""
    form = Revies_form()
    return render(request, "../../djangoProject/templates/index.html", {"form": form})