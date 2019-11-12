import xadmin
from .models import CompanyInfo

class CompanyInfoAdmin(object):
    import_excel = True
    list_display = ['company','email','start_time','end_time','is_alive']




xadmin.site.register(CompanyInfo,CompanyInfoAdmin)
