import xadmin
from .models import UserProfile
# Register your models here.



class UserProfileAdmin(object):
    list_display = ['username','email','mobile']



xadmin.site.unregister(UserProfile)

xadmin.site.register(UserProfile,UserProfileAdmin)