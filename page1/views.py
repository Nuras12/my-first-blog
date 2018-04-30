from django.shortcuts import render
from .models import First1
from . forms import UserForm

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    pasts=First1.objects.order_by('src')
    return render(
        request,
        'index.html',
        {'pasts': pasts}
    )
def send(request):
    userform = UserForm()
    return render(
        request,
        "form1.html",
        {"form": userform}
    )
