# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User

# # Unregister the default User admin first
# admin.site.unregister(User)
# # Then register your custom User admin
# admin.site.register(User, CustomUserAdmin)



from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)