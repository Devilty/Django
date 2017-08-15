from django.shortcuts import render


def home(request):
    context = {}
    context['hello'] = 'hello you'
    return render(request, 'homepage.html', context)
    # return HttpResponse("Hello world ! ")
