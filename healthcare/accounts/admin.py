# from django.contrib import admin
# from django.contrib.auth import get_user_model

# User = get_user_model()
# admin.site.register(User)


# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User

# # If you want to extend the User admin
# class CustomUserAdmin(UserAdmin):
#     # Your customizations here
#     pass

# # Unregister the default User admin first
# admin.site.unregister(User)
# # Then register your custom User admin
# admin.site.register(User, CustomUserAdmin)





from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)