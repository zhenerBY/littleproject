from django.contrib import admin

from main.models import AdvUser, AnimalImage


class AdvUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'is_superuser', 'is_active')
    list_display_links = ('username', 'first_name', 'last_name',)
    search_fields = ('username', 'first_name', 'last_name', 'email',)
    ordering = ('username',)


class AnimalImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'animal_type', 'pic_url', 'user',)
    list_display_links = ('animal_type', 'pic_url',)
    search_fields = ('animal_type', 'pic_url',)
    ordering = ('-created_at',)


admin.site.register(AdvUser, AdvUserAdmin)
admin.site.register(AnimalImage, AnimalImageAdmin)
