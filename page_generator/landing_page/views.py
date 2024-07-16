from django.shortcuts import render, redirect
from .forms import MyModelForm
from .serializers import ReactSerializer
from .models import React
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# Create your views here.
class ReactView(APIView):
    permission_classes = [AllowAny]
    serializer_class = ReactSerializer

    def get(self, request):
        output = [{
            "name": output.name,
            "email": output.email,
            "message": output.message}
            for output in React.objects.all()]
        return Response(output)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


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