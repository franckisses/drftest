
import xadmin
from .models import UserProfile

class UserProfileAdmin(object):
    list_display = ['username','email','mobile']


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = 'NIUBI-NOTICE'
    site_footer = 'tedu-python center'
    menu_style = 'accordion'

xadmin.site.unregister(UserProfile)

xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSetting)
xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)