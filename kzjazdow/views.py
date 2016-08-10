from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from django.utils import timezone
from .models import Zjazd
from .forms import ZjazdForm


def lista_zjazdow(request):
    zjazdy = Zjazd.objects.order_by('data')
    return render(request, 'kzjazdow/lista_zjazdow.html', {'zjazdy':zjazdy})


def szczegoly_zjazdu(request, pk):
    zjazd = get_object_or_404(Zjazd, pk=pk)
    return render(request, 'kzjazdow/szczegoly_zjazdu.html', {'zjazd': zjazd})


def dodaj_zjazd(request):
    if request.method == 'POST':
        form = ZjazdForm(request.POST)
        if form.is_valid():
            zjazd = form.save(commit=False)
            zjazd.save()
            return redirect('szczegoly_zjazdu', pk=zjazd.pk)
    else:
        form = ZjazdForm()
    return render(request, 'kzjazdow/dodaj_zjazd.html', {'form': form})


def edytuj_zjazd(request, pk):
    zjazd = get_object_or_404(Zjazd, pk=pk)
    if request.method == 'POST':
        form = ZjazdForm(request.POST)
        if form.is_valid():
            zjazd = form.save(commit=False)
            zjazd.save()
            return redirect('szczegoly_zjazdu', pk=zjazd.pk)
    else:
        form = ZjazdForm(instance=zjazd)
    return render(request, 'kzjazdow/dodaj_zjazd.html', {'form': form})


def usun_zjazd(request, pk):
    zjazd = get_object_or_404(Zjazd, pk=pk)
    zjazd.delete()
    return redirect(lista_zjazdow)


def test(request):
    if request.method == 'POST':
        testowy_text = request.POST.get('hhh')
        print (request.POST.values())
        
        return render(request, 'kzjazdow/test.html', {'testowy_text': testowy_text})
    return render(request, 'kzjazdow/test.html', {'testowy_text': 'wpisz cos'})


