from django.shortcuts import render
from django.views import View
# Import necessary modules for the view


class Home(View):
    def get(self, request):
        print("GET request received")
        return render(request, "index.html", {})
