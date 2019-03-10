from tb_shop.models import Category


def get_category():
    # Queries 3 tables: cookbook_recipe, cookbook_ingredient,
    # and cookbook_food.
    return list(Categoryy.objects.prefetch_related('category'))