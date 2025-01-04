from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError
from django.core.files.storage import default_storage


class UserManager(BaseUserManager):
    def create_user(self, username, password, **kwargs):
        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        return self.create_user(username, password, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$')], null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    username = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    pic = models.ImageField(upload_to='user-profile/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.username
    
    class Meta:
        ordering = ["-created_at"]
        
    def save(self, *args, **kwargs):
        try:
            this = User.objects.get(pk=self.pk)
            if this.pic != self.pic:
                if this.pic and default_storage.exists(this.pic.name):
                    default_storage.delete(this.pic.name)
        except User.DoesNotExist:
            pass
        
        super(User, self).save(*args, **kwargs)
    

class ResetPassword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=255)
    forget_password_token_created_at = models.DateTimeField(auto_now_add=True)



class Grievance(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.BigIntegerField()
    designation = models.CharField(max_length=255)
    email = models.EmailField()
    identity = models.CharField(max_length=100)
    identity_number = models.CharField(max_length=30)
    types_of_grievance = models.CharField(max_length=100)
    your_grievance = models.TextField()
    
    published = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Name:{self.name}, Email:{self.email}'
    
    class Meta:
        ordering = ["-created_at"]
    
    
class Amaatra(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.BigIntegerField()
    email = models.EmailField()
    address = models.TextField()
    
    published = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Name:{self.name}, Email:{self.email}'
    
    class Meta:
        ordering = ["-created_at"]
        
class AmaatraCategory(models.Model):
    category = models.CharField(max_length=400)
    def __str__(self):
        return self.category
          
class AmaatraFAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    category = models.ManyToManyField(AmaatraCategory, blank=True)
    priority = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
    
    class Meta:
        ordering = ["-priority"]
    
    
class SSM(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.BigIntegerField()
    email = models.EmailField()
    class_admission = models.CharField(max_length=50)
    
    published = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Name:{self.name}, Email:{self.email}'
    
    class Meta:
        ordering = ["-created_at"]
        
        
class SSMCategory(models.Model):
    category = models.CharField(max_length=400) 
    def __str__(self):
        return self.category    
          
class SSMFAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    category = models.ManyToManyField(SSMCategory, blank=True)
    priority = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
    
    class Meta:
        ordering = ["-priority"]
        
        
class PESIMSRCategory(models.Model):
    category = models.CharField(max_length=400) 
    def __str__(self):
        return self.category    
          
class PESIMSRFAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    category = models.ManyToManyField(PESIMSRCategory, blank=True)
    priority = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
    
    class Meta:
        ordering = ["-priority"]
        
        
class PESUIMSRCategory(models.Model):
    category = models.CharField(max_length=400) 
    def __str__(self):
        return self.category    
          
class PESUIMSRFAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    category = models.ManyToManyField(PESUIMSRCategory, blank=True)
    priority = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
    
    class Meta:
        ordering = ["-priority"]
        
        
class PESPublicSchoolCategory(models.Model):
    category = models.CharField(max_length=400) 
    def __str__(self):
        return self.category    
          
class PESPublicSchoolFAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    category = models.ManyToManyField(PESPublicSchoolCategory, blank=True)
    priority = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
    
    class Meta:
        ordering = ["-priority"]
        
        
class PESHospitalCategory(models.Model):
    category = models.CharField(max_length=400) 
    def __str__(self):
        return self.category    
          
class PESHospitalFAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    category = models.ManyToManyField(PESHospitalCategory, blank=True)
    priority = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
    
    class Meta:
        ordering = ["-priority"]
    
      
class RRTransportation(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.BigIntegerField()
    parent_phone_number = models.BigIntegerField()
    email = models.EmailField()
    address = models.TextField()
    dob = models.DateField()
    blood_group = models.CharField(max_length=10)
    registration_no = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='rr_transportation/')
    program = models.CharField(max_length=255)
    route = models.CharField(max_length=255)
    pickup_point = models.CharField(max_length=255)
    
    published = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Name:{self.name}, Email:{self.email}'
    
    class Meta:
        ordering = ["-created_at"]
        
        
class ECTransportation(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.BigIntegerField()
    parent_phone_number = models.BigIntegerField()
    email = models.EmailField()
    address = models.TextField()
    dob = models.DateField()
    blood_group = models.CharField(max_length=10)
    registration_no = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='ec_transportation/')
    program = models.CharField(max_length=255)
    route = models.CharField(max_length=255)
    pickup_point = models.CharField(max_length=255)
    
    published = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Name:{self.name}, Email:{self.email}'
    
    class Meta:
        ordering = ["-created_at"]
        
          
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    category = models.CharField(max_length=400)
    priority = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
    
    class Meta:
        ordering = ["-priority"]
   
    
class DailyReport(models.Model):
    category = models.CharField(max_length=400)
    campus = models.CharField(max_length=255)
    date = models.DateField()
    title = models.CharField(max_length=255)
    description  = models.TextField()
    status = models.CharField(max_length=100)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-date", "-created_at"]
    
    
class CETRanking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    registration_number = models.CharField(max_length=20)
    taken_kcet = models.BooleanField(default=False)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    campus = models.CharField(max_length=100, blank=True, null=True)
    kcet_rank = models.IntegerField(blank=True, null=True)
    kcet_registration_number = models.CharField(max_length=20, blank=True, null=True)
    
    published = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
                
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["-created_at"]
    
    
class JEEMain1(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    registration_number = models.CharField(max_length=20)
    taken_jee_main1 = models.BooleanField(default=False)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    campus = models.CharField(max_length=100, blank=True, null=True)
    jee_main1_rank = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    jee_main1_registration_number = models.CharField(max_length=20, blank=True, null=True)
    upload_marks = models.ImageField(upload_to='jeemain1_upload_marks/', blank=True, null=True)
    
    published = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
                
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["-created_at"]
    
    
class JEEMain2(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    registration_number = models.CharField(max_length=20)
    taken_jee_main2 = models.BooleanField(default=False)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    campus = models.CharField(max_length=100, blank=True, null=True)
    jee_main2_rank = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    crl_rank = models.CharField(max_length=10, blank=True, null=True)
    jee_main2_registration_number = models.CharField(max_length=20, blank=True, null=True)
    upload_marks = models.ImageField(upload_to='jeemain2_upload_marks/', blank=True, null=True)
    
    published = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
                
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["-created_at"]
    
    
class COMEDK(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    registration_number = models.CharField(max_length=20)
    taken_comedk = models.BooleanField(default=False)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    campus = models.CharField(max_length=100, blank=True, null=True)
    comedk_rank = models.CharField(max_length=20, blank=True, null=True)
    comedk_registration_number = models.CharField(max_length=20, blank=True, null=True)
    tat_number = models.CharField(max_length=20, blank=True, null=True)
    upload_marks = models.ImageField(upload_to='comedk_upload_marks/', blank=True, null=True)
    
    published = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
                
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["-created_at"]
        
        
class PUCUpoloadMarks(models.Model):
    board = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    registration_number = models.CharField(max_length=20)
    specialization = models.CharField(max_length=100)
    campus = models.CharField(max_length=100)
    intermediate_candidates = models.BooleanField(default=False)
    physics = models.IntegerField()
    chemistry = models.IntegerField()
    mathematics_a = models.IntegerField()
    mathematics_b = models.IntegerField(blank=True, null=True)
    electronics = models.IntegerField(blank=True, null=True)
    computer_science = models.IntegerField(blank=True, null=True)
    biotechnology = models.IntegerField(blank=True, null=True)
    aggregate_percentage = models.IntegerField()
    upload_marks = models.ImageField(upload_to='puc_upload_marks/')
    comment = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def clean(self):
        
        if self.intermediate_candidates:
            required_fields = ['mathematics_b',]
            for field in required_fields:
                if not getattr(self, field):
                    raise ValidationError({field: f'{field.replace("_", " ").capitalize()} is required.'})
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["-created_at"]

