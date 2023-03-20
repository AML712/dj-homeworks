from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'sup': {
    'вода, литр': 1,
    'картофель, шт': 1,
    'мясо, г': 100,
    'морковь, г': 30,
    'лук, г': 20,
    'соль, ч.л.': 1,
    },
}

def index(request):
    return render(request, 'calculator/index.html')


def dishes(request, dish):
    qty = int(request.GET.get('servings', 1))
    dish_ready = DATA[dish]
    dish_make = {}
    for key, value in dish_ready.items():
        dish_make[key] = value * qty
    context = {
        'recipe': dish_make,
        'qty': qty,
    }
    return render(request, 'calculator/dishes.html', context)


def pasta(request):
    return dishes(request, 'pasta')


def omlet(request):
    return dishes(request, 'omlet')


def buter(request):
    return dishes(request, 'buter')


def sup(request):
    return dishes(request, 'sup')