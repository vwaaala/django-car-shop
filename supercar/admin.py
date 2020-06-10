from __future__ import unicode_literals
from django.contrib import admin
from .models import (
    DictGroup,
    DictBrand,
    DictModel,
    DictType,
    DictCategory,
    DictTypeOfFuel,
    DictTrailerType,
    Item,
    Order,
    OrderItem
)


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'name_autopanel',
                    'identificator', 'is_active',)
    list_filter = ('id', 'name', 'name_autopanel',
                   'identificator', 'is_active',)


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'group', 'is_active',)
    list_filter = ('id', 'name', 'group', 'is_active',)


class DictModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'is_active',)
    list_filter = ('id', 'name', 'brand', 'is_active',)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'group', 'is_active',)
    list_filter = ('id', 'name', 'group', 'is_active',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'is_active',)
    list_filter = ('id', 'name', 'type', 'is_active',)


class TypeOfFuelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active',)
    list_filter = ('id', 'name', 'is_active',)


class TrailerTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'is_active',)
    list_filter = ('id', 'name', 'category', 'is_active',)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year_production', 'is_active', 'is_sold', 'brand', 'model',
                    'price', 'group', 'category', 'type', )
    list_filter = ('id', 'name', 'year_production', 'is_active', 'is_sold', 'brand', 'model',
                   'price', 'group', 'category', 'type', )
    search_fields = ['id']


customized_sitetree_admin = False

if customized_sitetree_admin:

    from sitetree.admin import TreeItemAdmin, TreeAdmin, override_tree_admin, override_item_admin

    class CustomTreeItemAdmin(TreeItemAdmin):

        fieldsets = None

    class CustomTreeAdmin(TreeAdmin):

        exclude = ('title',)

    override_item_admin(CustomTreeItemAdmin)
    override_tree_admin(CustomTreeAdmin)

# Register your models here.
admin.site.register(DictGroup, GroupAdmin)
admin.site.register(DictBrand, BrandAdmin)
admin.site.register(DictModel, DictModelAdmin)
admin.site.register(DictType, TypeAdmin)
admin.site.register(DictCategory, CategoryAdmin)
admin.site.register(DictTypeOfFuel, TypeOfFuelAdmin)
admin.site.register(DictTrailerType, TrailerTypeAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
