import xadmin
from .models import CompanyInfo

class CompanyInfoAdmin(object):
    list_display = ['company','email','start_time','end_time','is_alive']
    import_excel = True

    def post(self, request, *args, **kwargs):
        #  导入逻辑
        if 'excel' in request.FILES:
            pass  # 此处是一系列的操作接口, 通过  request.FILES 拿到数据随意操作
        return super(CompanyInfoAdmin, self).post(request, args, kwargs)  # 此返回值必须是这样


xadmin.site.register(CompanyInfo,CompanyInfoAdmin)
