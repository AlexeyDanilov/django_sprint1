from django.shortcuts import render


def about(request):
    return render(request=request, template_name='pages/about.html')


def rules(request):
    return render(request=request, template_name='pages/rules.html')
