from django.contrib import admin
from .models import *


@admin.register(Types_of_input)
class Types_of_inputAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_selectable')
    search_fields = ('title',)



@admin.register(ItemsOfInputs)
class ItemsOfInputsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)



@admin.register(Inputs)
class InputsAdmin(admin.ModelAdmin):
    list_display = ('title', 'type_of_input', 'is_required',)
    search_fields = ('title', 'type_of_input',)


@admin.register(Forms)
class FormsAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published')
    search_fields = ('title',)


@admin.register(Datas)
class DatasAdmin(admin.ModelAdmin):
    list_display = ('name', 'form', 'is_checked',)
    search_fields = ('name',)
    list_filter = ('form', 'is_checked',)


@admin.register(DetailDatas)
class DetailDatasAdmin(admin.ModelAdmin):
    list_display = ('data', 'input_type')
    search_fields = ('item',)
    list_filter = ('data', 'input_type')


# Register your models here.