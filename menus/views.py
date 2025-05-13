from django.shortcuts import render
from users.models import User
from sections.models import Section, Item

data = {
    "is_admin": True,
    "sections": [
        {
            "name": "Entradas",
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
            ]
        },
        {
            "name": "Pricipais",
            "items": [
                {
                    "name": "Filé ao molho madeira",
                    "price": 80.00,
                    "description": "Filé ao molho madeira acompanhado de arroz temperado e purê de batatas",
                },
                {
                    "name": "Filé ao molho madeira",
                    "price": 80.00,
                    "description": "Filé ao molho madeira acompanhado de arroz temperado e purê de batatas",
                },
                {
                    "name": "Filé ao molho madeira",
                    "price": 80.00,
                    "description": "Filé ao molho madeira acompanhado de arroz temperado e purê de batatas",
                },
            ]
        },
        {
            "name": "Sobremesas",
            "items": [
                {
                    "name": "Petit Gateau",
                    "price": 45.00,
                    "description": "Petit Gateau de chocolate acompanhado de sorvete de creme",
                },
                {
                    "name": "Petit Gateau",
                    "price": 45.00,
                    "description": "Petit Gateau de chocolate acompanhado de sorvete de creme",
                },
            ]
        }
    ],

}


def index(request):
    return render(request, "menus/index.html",)

def menus(request, id: str):
    user = User.objects.get(pk=id)
    sections = Section.objects.filter(user_id=id)
    dict_sections = []
    for section in sections:
        items = []
        for item in section.items.all():
            items.append(item)
        dict_sections.append({
            "name": section.name,
            "items": items
        })

    print(dict_sections)

    data.update({
        "user": user.to_json(),
        "sections": dict_sections
    })
    return render(request, "menus/menu.html", data)
