from django.shortcuts import render, redirect
from .forms import HarcamaForm
from .forms import Harcama

def harcama_ekle(request):
    if request.method == "POST":
        form = HarcamaForm(request.POST)
        if form.is_valid():
            harcama = form.save(commit=False)
            harcama.user = request.user
            harcama.save()
            return redirect('dashboard')
    else:
        form = HarcamaForm()
    return render(request, 'harcama/harcama_ekle.html', {'form': form})

def dashboard(request):
    harcamalar = Harcama.objects.filter(user=request.user)
    return render(request, 'harcama/dashboard.html', {'harcamalar': harcamalar})
