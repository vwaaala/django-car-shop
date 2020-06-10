from .models import (DictCategory)


def nav_menu(request):

    category = DictCategory.objects.all()

    return {
        'category': category
    }
