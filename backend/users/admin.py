from django.contrib import admin

from .models import User, Follow


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name',)
    search_fields = ('username', 'email',)
    list_filter = ('username', 'email',)


class FollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'author',)
    search_fields = ('user', 'author',)
    list_filter = ('user', 'author',)


admin.site.register(User, UserAdmin)
admin.site.register(Follow, FollowAdmin)
