from django.shortcuts import render

data = {
        "items": [
            {
                "name": "Hamburger Cheddar",
                "price": 33.80,
                "description": "Hamruger com chaddar cremoso",
            },
            {
                "name": "Hamburger Cheddar",
                "price": 33.80,
                "description": "Hamruger com chaddar cremoso",
            },
            {
                "name": "Hamburger Cheddar",
                "price": 33.80,
                "description": "Hamruger com chaddar cremoso",
            },
            {
                "name": "Hamburger Cheddar",
                "price": 33.80,
                "description": "Hamruger com chaddar cremoso",
            },
        ],
        "is_admin": True,
    }


def index(request):
    return render(request, "menus/index.html",)

def menus(request):
    return render(request, "menus/menu.html", data)
