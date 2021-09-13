from django.shortcuts import render
from django.http import HttpResponse
from .models import Lugat


def index(request):
    soz = request.GET.get('q', '')
    if soz and soz != '':
        natija = Lugat.objects.filter(inglizcha__contains=soz).all()[:3]
    else:
        natija = None

    return render(request, 'index.html', {'q':soz, 'natija': natija})

def salom2(request):
    return HttpResponse('MENING SAHIFAM !!!')
