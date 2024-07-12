from django.shortcuts import render, redirect
from .forms import MyModelForm

# Create your views here.
def my_view(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = MyModelForm
    return render(request, 'landing_page/form.html', {'form': form})

def success_view(request):
    return render(request, 'landing_page/success.html')