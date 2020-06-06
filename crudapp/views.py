from django.shortcuts import render, redirect, get_object_or_404
from .models import CiscoModel
from .forms import CiscoForm
from django.views.generic import ListView, DetailView

# Create your views here.
class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'cisco_list'

    def get_queryset(self):
        return CiscoModel.objects.all()

class CiscoDetailView(DetailView):
    model = CiscoModel
    template_name = 'cisco-detail.html'


def create(request):
    if request.method == 'POST':
        form = CiscoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = CiscoForm()

    return render(request,'create.html',{'form': form})

def edit(request, pk, template_name='edit.html'):
    cisco = get_object_or_404(CiscoModel, pk=pk)
    form = CiscoForm(request.POST or None, instance=cisco)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})

def delete(request, pk, template_name='confirm_delete.html'):
    cisco = get_object_or_404(CiscoModel, pk=pk)
    if request.method=='POST':
        cisco.delete()
        return redirect('index')
    return render(request, template_name, {'object':cisco})