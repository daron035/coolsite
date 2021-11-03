from django.contrib import admin

from .models import *


class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'time_update', 'photo', 'cat', 'is_published') # список (кортеж) отображаемых полей
    list_display_links = ('id', 'title') # список полей в виде ссылки для перехода к соответствующей записи
    search_fields = ('title', 'content') # поля по которым можно производить поиск
    list_editable = ('is_published',) # поле, которое можно изменять в админке (галки)
    list_filter = ('is_published', 'time_create') # фильтр в правом sidebar'е
    prepopulated_fields = {"slug": ("title",)} # указать заполнять автоматически поле слаг на основе поля title
                                              # это при создании новой категории в админке
                                              
admin.site.register(Women, WomenAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)} # указать заполнять автоматически поле слаг на основе поля name
                                              # это при создании новой категории в админке

admin.site.register(Category, CategoryAdmin)