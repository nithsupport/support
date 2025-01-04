from django.db.models import Q
from django.contrib.auth.models import Permission
from support_app.models import User


# -----------------Admin dashboard permissions----------------------
# Checking all given permissions of admin dashboard


def check_requested_user_permissions(user, desired_permissions):
    if user.is_superuser:
        return True
    has_all_permissions = Permission.objects.filter(
        codename__in=desired_permissions,
        group__user=user
    ).all().values_list('codename', flat=True)

    return all(permission in has_all_permissions for permission in desired_permissions)

# -----------------End admin dashboard permissions----------------------



# -------------Edit club user details permisssions-----------------
# Checking only club user
def check_only_support_user_permissions(requested_user, permalink):
    if requested_user.is_active and requested_user.is_staff:
        if requested_user.is_superuser or User.objects.filter(permalink=permalink, user__pk=requested_user.pk).exists():
            return True
    else:
        return False

# Checking all given permissions of edit staff   
def check_given_permissions(requested_user, primary_key, check_permissions):
    if requested_user.is_active and requested_user.is_staff:
        
        if requested_user.is_superuser or requested_user.s_id==primary_key:
            return True
        else:
            has_all_permissions = Permission.objects.filter(
                codename__in=check_permissions,
                group__user=requested_user
            ).all().values_list('codename', flat=True)
            return all(permission in has_all_permissions for permission in check_permissions)
    else:
        return False



