from django.contrib import admin

from .models import Drink

@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'price', 'available', 'caffeine_mg', 'created_at', 'updated_at')
    list_filter = ('size', 'available')
    search_fields = ('name', 'description', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('name',)
