from django.shortcuts import render, redirect
from revies.forms import Revies_form, sh_form
# Create your views here.
def Revies(request):
    if request.method == "POST":
        form = Revies_form(request.POST)
        # showform = Show_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data.get("name")
            email = data.get("email")
            review = data.get("review")
            with open("./data.csv", "a", encoding='cp1251') as file:    #добавил encoding
                file.write(f"{name}|{email}|{review}\n")
            return redirect(Revies)
        form = Revies_form()
        return render(request, "index.html", {"form": form})

    with open("./data.csv") as file:
        revies = file.readlines()
    if len(revies) > 0:
        revies_1 = revies[0]
        name_1 = revies_1.split("|")[0]
        email_1 = revies_1.split("|")[0]
        review_1 = revies_1.split("|")[0]
    else:
        name_1 = ""
        email_1 = ""
        review_1 = ""
    form = Revies_form()
    return render(request, "index.html", {"form":form, "name":name_1, "email":email_1, "review":review_1})

# def Showrev(request):
#     if request.method == "GET":
#         form = sh_form
#         return render(request, "index.html", {"form": form})
#     elif request.method == "POST":
#         form = sh_form(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             rating = data.get("rating")
#             with open("../data.csv", "a") as file:
#                 file.write(f"{rating}\n")
#             return redirect(Showrev)
#         else:
#             form = sh_form()
#             return render(request, "index.html", {"form": form})