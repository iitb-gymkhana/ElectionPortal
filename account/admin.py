from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'roll_number', 'voter_type', 'user_type']

def make_active(modeladmin, news, queryset):
    queryset.update(is_active=True)
make_active.short_description = u"Activate selected Users"

def make_deactive(modeladmin, news, queryset):
    queryset.update(is_active=False)
make_deactive.short_description = u"Deactivate selected Users"

def make_staff(modeladmin, news, queryset):
    queryset.update(is_staff=True)
make_staff.short_description = u"Mark Users as staff"

def remove_staff(modeladmin, news, queryset):
    queryset.update(is_staff=False)
remove_staff.short_description = u"Mark Users as non-staff"

class CustomUserAdmin(UserAdmin):
    actions = [make_active, make_deactive, make_staff, remove_staff]

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)