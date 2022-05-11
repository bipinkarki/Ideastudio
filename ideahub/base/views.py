from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Panel, Idea
from .forms import PanelForm
# Create your views here.


# panels = [
#     {'id': 1, 'name': 'lets discuss about ideas!'},
#     {'id': 2, 'name': 'tech discussion'},
#     {'id': 3, 'name': 'blockchain technology ideas'},
# ]


def home(request):
    q = request.GET.get('q')
    panels = Panel.objects.filter()
    ideas = Idea.objects.all()
    context = {'panels': panels, 'ideas': ideas}
    return render(request, 'base/home.html', context)


def panel(request, pk):
    # panel = None
    # for i in panels:
    #     if i['id'] == int(pk):
    #         panel = i
    panel = Panel.objects.get(id=pk)
    context = {'panel': panel}
    return render(request, 'base/panel.html', context)


def createPanel(request):
    form = PanelForm()
    if request.method == 'POST':
        form = PanelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/panel_form.html', context)


def updatePanel(request, pk):
    panel = Panel.objects.get(id=pk)
    form = PanelForm(instance=panel)

    if request.method == 'POST':
        form = PanelForm(request.POST, instance=panel)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/panel_form.html', context)


def deletePanel(request, pk):
    panel = Panel.objects.get(id=pk)
    if request.method == 'POST':
        panel.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': panel})
