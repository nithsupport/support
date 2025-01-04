from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Grievance)
admin.site.register(models.Amaatra)
admin.site.register(models.SSM)
admin.site.register(models.RRTransportation)
admin.site.register(models.ECTransportation)
admin.site.register(models.CETRanking)
admin.site.register(models.JEEMain1)
admin.site.register(models.JEEMain2)

admin.site.register(models.FAQ)
admin.site.register(models.SSMFAQ)
admin.site.register(models.AmaatraFAQ)
admin.site.register(models.PESIMSRFAQ)
admin.site.register(models.PESUIMSRFAQ)
admin.site.register(models.PESPublicSchoolFAQ)
admin.site.register(models.PESHospitalFAQ)


admin.site.register(models.AmaatraCategory)
admin.site.register(models.SSMCategory)
admin.site.register(models.PESIMSRCategory)
admin.site.register(models.PESUIMSRCategory)
admin.site.register(models.PESHospitalCategory)
admin.site.register(models.PESPublicSchoolCategory)