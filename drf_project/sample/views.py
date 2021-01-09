from django.shortcuts import render

# Basic html view

def index_view(request):
   context = {}
   return render(request, 'index.html', context=context)
