from django import template
from support_app.models import( User, Grievance, Amaatra, SSM, ECTransportation, RRTransportation, FAQ, CETRanking, PUCUpoloadMarks, DailyReport, JEEMain1, JEEMain2, COMEDK,
                               AmaatraFAQ, SSMFAQ, PESIMSRFAQ, PESHospitalFAQ, PESUIMSRFAQ, PESPublicSchoolFAQ)
from django.contrib.auth.models import Group, Permission
from django.db.models import Q
from django.db.models import Sum
from datetime import datetime

register = template.Library()

model_name_mapping = {
    'amaatra': Amaatra,
    'ssm': SSM,
}
faq_model_mapping = {
    'pesu': FAQ,
    'amaatra': AmaatraFAQ,
    'ssm': SSMFAQ,
    'pesimsr': PESIMSRFAQ,
    'pesuimsr': PESUIMSRFAQ,
    'pespublicschool': PESPublicSchoolFAQ,
    'peshospital': PESHospitalFAQ,
}


@register.filter
def total_requested_count(model_key, filter_type):
    # Get the current date and time
    now = datetime.now()
    models_name = model_name_mapping.get(model_key.lower())
    if filter_type == 'day':
        # Filter for the current day (today)
        start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
        total = models_name.objects.filter(created_at__gte=start_of_day).count()

    elif filter_type == 'month':
        # Filter for the current month
        start_of_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        total = models_name.objects.filter(created_at__gte=start_of_month).count()

    elif filter_type == 'year':
        # Filter for the current year
        start_of_year = now.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
        total = models_name.objects.filter(created_at__gte=start_of_year).count()

    else:
        total = models_name.objects.count()

    return total


@register.filter
def total_category_count(model_key, category_type):
    models_name = faq_model_mapping.get(model_key.lower())
    total = models_name.objects.filter(category__category__icontains=category_type).count()
    return total


@register.filter
def total_faqs_count(model_key):
    models_name = faq_model_mapping.get(model_key.lower())
    total = models_name.objects.all().count()
    return total


@register.filter
def check_requested_permissions(user, permission_codename):
    if user.is_superuser:
        return True
    try:
        permission = Permission.objects.get(codename=permission_codename, group__user=user)
        return True
    except Permission.DoesNotExist:
        return False
    
    
@register.filter
def total_categoy(categoy):
    return FAQ.objects.filter(category__icontains=categoy).count()
    
    
@register.filter
def total_groups(value):
    return Group.objects.all().count()
    
    
@register.filter
def total_users(value):
    return User.objects.filter(is_active=True).count()
    



@register.filter
def total_database_count(value):
    return (
        Grievance.objects.all().count()
        # + FAQ.objects.all().count()
        + Amaatra.objects.all().count()
        + SSM.objects.all().count()
        + ECTransportation.objects.all().count()
        + RRTransportation.objects.all().count()
        + CETRanking.objects.all().count()
        + JEEMain1.objects.all().count()
        + JEEMain2.objects.all().count()
        + COMEDK.objects.all().count()
        + PUCUpoloadMarks.objects.all().count()
        + DailyReport.objects.all().count()
    )


@register.filter
def total_grievance(value):
    return Grievance.objects.all().count()

@register.filter
def total_amaatra(value):
    return Amaatra.objects.all().count()

@register.filter
def total_ssm(value):
    return SSM.objects.all().count()

@register.filter
def total_ec_transportation(value):
    return ECTransportation.objects.all().count()

@register.filter
def total_rr_transportation(value):
    return RRTransportation.objects.all().count()

@register.filter
def total_cet_ranking(value):
    return CETRanking.objects.all().count()

@register.filter
def total_jee_main1(value):
    return JEEMain1.objects.all().count()

@register.filter
def total_jee_main2(value):
    return JEEMain2.objects.all().count()

@register.filter
def total_comedk(value):
    return COMEDK.objects.all().count()

@register.filter
def total_puc_upload_marks(value):
    return PUCUpoloadMarks.objects.all().count()

@register.filter
def total_daily_report(value):
    return DailyReport.objects.all().count()


@register.simple_tag
def get_progress_bars():
    total_counts = {
        'grievance': Grievance.objects.count(),
        'amaatra': Amaatra.objects.count(),
        'ssm': SSM.objects.count(),
        'ec_transportation': ECTransportation.objects.count(),
        'rr_transportation': RRTransportation.objects.count(),
        'cet_ranking': CETRanking.objects.count(),
        'jee_main1': JEEMain1.objects.count(),
        'jee_main2': JEEMain2.objects.count(),
        'comedk': COMEDK.objects.count(),
        'puc_upload_marks': PUCUpoloadMarks.objects.count(),
        'daily_report': DailyReport.objects.count(),
    }
    
    total_sum = sum(total_counts.values())
    
    if total_sum == 0:
        percentages = {key: 0 for key in total_counts}
    else:
        percentages = {key: (count / total_sum) * 100 for key, count in total_counts.items()}
    
    return percentages