from django.shortcuts import render, get_object_or_404

from .models import Drink

def index(request):
    drinks = Drink.objects.all()

    context = {
        'drinks': drinks,
    }

    return render(request, 'drinks_counter/index.html', context)


def drink_display(request, slug):
    drink = get_object_or_404(Drink, slug=slug)

    context = {
        'drink': drink
    }

    return render(request, 'drinks_counter/drink_display.html', context)
