from django.shortcuts import render
from django.http import JsonResponse
#from django.contrib.auth.decorators import login_required
from .models import ClickEvent

#@login_required
def home(request):
    return render(request, 'clicks/home.html')

#@login_required
def register_click(request):
    if request.method == "POST":
        element = request.POST.get("element_name")
        ClickEvent.objects.create(user=request.user, element_name=element)
        return JsonResponse({"status": "ok"})
    return JsonResponse({"status": "error"}, status=400)
