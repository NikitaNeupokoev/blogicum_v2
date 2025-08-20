from django.shortcuts import render


def about(request):
    """Отображает страницу "О нас"."""
    return render(request, 'pages/about.html')


def rules(request):
    """Отображает страницу с правилами."""
    return render(request, 'pages/rules.html')
