from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class Home(View):
    def get(self, request):
        return HttpResponse("It works!")
    # def get(self, request):
    #     print("GET request received")
    #     return render(request, "index.html", {})