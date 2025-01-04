from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Grievance, Amaatra, AmaatraFAQ, AmaatraCategory, SSM, ECTransportation, RRTransportation, FAQ, CETRanking, PUCUpoloadMarks, DailyReport, User, JEEMain1, JEEMain2,COMEDK
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group, Permission
from django.core.validators import MinValueValidator, MaxValueValidator
import re


def validate_name(value):
    # Allow only letters, spaces, and dots
    if not re.match(r'^[a-zA-Z\s.]+$', value):
        raise ValidationError("Name can only contain letters, spaces, and dots.")

def create_name_field():
    return forms.CharField(
        label='Full Name',
        widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': 'Type your full name here',
            'class': 'form-control',
        }),
        validators=[validate_name],
    )
    
def create_phone_number_field():
    return forms.CharField(
        label='Phone Number',
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message='Please enter a valid 10-digit Indian phone number.',
                code='invalid_phone_number'
            ),
        ],
        widget=forms.TextInput(attrs={
            'placeholder': 'Please enter a 10-digit phone number',
            'class': 'form-control',
            'maxlength': '10',
            'pattern': r'^\d{10}$',  # HTML5 pattern for client-side validation
        })
    )
    
def create_parent_phone_number_field():
    return forms.CharField(
        label='Parent Phone Number',
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message='Please enter a valid 10-digit Indian phone number.',
                code='invalid_parent_phone_number'
            ),
        ],
        widget=forms.TextInput(attrs={
            'placeholder': 'Please enter a 10-digit phone number',
            'class': 'form-control',
            'maxlength': '10',
            'pattern': r'^\d{10}$',  # HTML5 pattern for client-side validation
        })
    )
    
def create_email_field():
    return forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Type your email address here',
                # 'pattern': '.+pes\.edu$',
                'title': 'Please enter a valid email address',
                'class': 'form-control',
                'required': True,
            }
        )
    )

def create_number_field(label, placeholder, required, max_value):
    return forms.IntegerField(
        label=label,
        required=required,
        widget=forms.NumberInput(attrs={
            'placeholder': placeholder,
            'class': 'form-control',
            'min': '0',
            'max': str(max_value),  # Convert max_value to string for the widget attribute
        }),
        validators=[MinValueValidator(0), MaxValueValidator(max_value)]
    )
    
def create_decimal_number_field(label, placeholder, required, max_value):
    return forms.DecimalField(
        label=label,
        required=required,
        widget=forms.NumberInput(attrs={
            'placeholder': placeholder,
            'class': 'form-control',
            'min': '0',
            'max': str(max_value),
            'step': '0.01',  # Allow two decimal places
        }),
        validators=[MinValueValidator(0), MaxValueValidator(max_value)],
        max_digits=5,  # Adjust as needed
        decimal_places=2  # Allow up to two decimal places
    )
    

class GrievanceForm(forms.ModelForm):
    name = create_name_field()
    phone_number = create_phone_number_field()
    email = create_email_field()
    def clean_email(self):
        email = self.cleaned_data['email']
        cleaned_email = email.strip()  # Remove leading and trailing whitespace
        return cleaned_email
    
    designation = forms.CharField(
        label='Designation',
        widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': 'Type your designation here',
            'class': 'form-control',
        })
    )
    
    identity_number = forms.CharField(
        label='Identity Number',
        widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': 'Type your identity number here',
            'class': 'form-control',
        })
    )
    
    IDENTITY = [
        ('Aadhaar Card','Aadhaar Card'),
        ('Passport','Passport'),
    ]
    identity = forms.ChoiceField(
        choices=IDENTITY, label='identity',
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    
    TYPES_OF_GRIEVANCE = [
        ('Complaint','Complaint'),
        ('Suggestion','Suggestion'),
        ('Seeking Guidance / Information','Seeking Guidance / Information'),
    ]
    types_of_grievance = forms.ChoiceField(
        choices=TYPES_OF_GRIEVANCE, label='types_of_grievance',
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    
    
    
    class Meta:
        model = Grievance
        fields = ('name', 'phone_number', 'designation', 'email', 'identity', 'identity_number', 'types_of_grievance', 'your_grievance')
        widgets = {
            'your_grievance': forms.Textarea(attrs={'class': 'form-control', "rows":"4", 'placeholder':"Type your your grievance here.."}),
        }
        


class AmaatraForm(forms.ModelForm):
    name = create_name_field()
    phone_number = create_phone_number_field()
    email = create_email_field()
    def clean_email(self):
        email = self.cleaned_data['email']
        cleaned_email = email.strip()  # Remove leading and trailing whitespace
        return cleaned_email
    
    class Meta:
        model = Amaatra
        fields = ('name', 'phone_number', 'email', 'address')
        widgets = {
            'address': forms.Textarea(attrs={'class': 'form-control', "rows":"4",'placeholder':"Type your address here"}),
        }


class SSMForm(forms.ModelForm):
    name = create_name_field()
    phone_number = create_phone_number_field()
    email = create_email_field()
    def clean_email(self):
        email = self.cleaned_data['email']
        cleaned_email = email.strip()  # Remove leading and trailing whitespace
        return cleaned_email
    
    class_admission = forms.CharField(
        label='Class to which admission is sought',
        widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': 'Type your class here',
            'class': 'form-control',
        })
    )
    
    class Meta:
        model = SSM
        fields = ('name', 'phone_number', 'email', 'class_admission')
        # widgets = {
        #     'address': forms.Textarea(attrs={'placeholder':"Type your address here.."}),
        # }

RR_ROUTE_CHOICES = [
        ('', 'Choose a Route'),
        ('Route A', 'Route A'),
        ('Route B', 'Route B'),
        ('Route C', 'Route C'),
        ('Route D', 'Route D'),
        ('Route E', 'Route E'),
        ('Route F', 'Route F'),
    ]

RR_PICKUP_POINT_CHOICES = {
        "Route A":['Koramangala Water Tank','Koramangala BDA Complex','Koramangala Canara Bank','Sony World Signal','Domlur Flyover','Indiranagar 13th Main Signal','80 Feet Road (Tippasandra) BSNL Office','Jeevan Bheemanagar Bus Stop','BEML Gate','Binnamangala (Old Madras Road)','Chinmaya Mission Hospital','KFC Junction','Ulsoor Police Station','Manipal Centre','Commercial Street','Vydehi Super Speciality Hospital','Corporation Circle','Town Hall'],
        "Route B":['Hennur Rd/Ring Rd Junction Via 80FT RD','Lingarajapuram Bus Stop/ SBI Bank','Clarence School','Coles Park','Nandi Durga Road','T V Tower','Mekhri Circle','18th Cross Malleshwaram','13th Cross Margosa Road','K.C. General Hospital','Devaiah Park','Mariyappana Pallya','Navarang Theatre','Rajajinagar Police Station','ESI Hospital','Bashyam Circle – Rajajinagar','Dhobi Ghat Signal'],
        "Route C":['Nandini Layout','Mahalakshmi Layout','Shell Petrol Bunk (Soap Factory)','Rajajinagar 1st Block','Star Circle (Near Navrang)','Modi Hospital','Shankar Mutt','Water Tank','Hotel Pavithra Paradise','Housing Board (Magadi Road Jn.)','Vijayanagar Bus Stop','BTS Garage West of Chord Road'],
        "Route D":['Meenakshi Temple','Hulimavu (Bus Stop/Bata Showroom)','BPL Bus Stop','Arkere Bus Stop','Bannerghatta Road (IIMB)','J P Nagar 3rd Phase (Mondovi Motors)','J P Nagar 15th Cross','R V Dental College','Raghavendra Swamy Mutt','Jayanagar BDA Complex','Jayanagar 7th Block','Banashankari BDA Complex'],
        "Route E":['Yelahanka Police station','Canara Bank ATM Yelahanka Kogilu','GKVK /UAS Bangalore Airport road entrance','Jakkur Signal','Kodigehalli Gate','Hebbal Ring Road Junction (Below Flyover)','Nagashettyhalli, Bhadrappa Lyt Railway Gate (Sanjaynagar)','BEL Kuvempu Circle (Jalahalli, Vidyaranyapura)','Devasandra/Chikkamaranahalli Bus Stop','Ramaiah Hospital (Mathikere, Sanjaynagar)','Sadashivnagar Police Station'],
        "Route F":['Marathahalli Bridge Bus Stop','Kadubeesanahalli Bridge Stop','Devarabisanahalli Bus Stop','Bellandur Bus Stop','Iblur Bus Stop (Previously Sarjapura Sun City Circle)','Agara Bus Stop','Mantri Sarovar Bus Stop','HSR Layout Flyover Bus Stop','Silk Board Junction','BTM Layout Signal','Jayadeva Hospital Signal'],
    }
    
class RRTransportationForm(forms.ModelForm):
    MAX_IMAGE_SIZE = 500 * 1024  # 500KB in bytes

    def clean_photo(self):
        photo = self.cleaned_data.get('photo', None)
        if photo and photo.size > self.MAX_IMAGE_SIZE:
            raise ValidationError("Image file size cannot exceed 500KB")
        return photo
    
    name = create_name_field()
    phone_number = create_phone_number_field()
    parent_phone_number = create_parent_phone_number_field()
    email = create_email_field()
    def clean_email(self):
        email = self.cleaned_data['email']
        cleaned_email = email.strip()  # Remove leading and trailing whitespace
        return cleaned_email
    
    dob = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'date',
            'class': 'form-control',
        })
    )
    
    blood_group = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': 'Type your blood group here',
            'class': 'form-control',
        })
    )
    
    registration_no = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': 'Type your registeration number here',
            'class': 'form-control',
        })
    )
    
    photo = forms.FileField(widget=forms.ClearableFileInput(attrs={
        'class': 'form-control',
        'id': 'formFile',
        'accept': '.pdf,.jpg,.jpeg,.png',
    }))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['photo'].widget.attrs.update({
            'type': 'file',  # 'type': 'file' is already the default for FileField widget
        })
    
    

    route = forms.ChoiceField(choices=RR_ROUTE_CHOICES, label='Route',
                              widget=forms.Select(attrs={'class': 'form-select', 'data-trigger': 'true', 'id': 'route'}))
    pickup_point = forms.ChoiceField(label='Pickup Point',
                                     widget=forms.Select(attrs={'class': 'form-select', 'id': 'pickup_point'}))
    
    PROGRAM = [
        ('Bachelor of Computer Applications (BCA)', 'Bachelor of Computer Applications (BCA)'),
        ('Bachelor of Science (B.Sc) in Medical', 'Bachelor of Science (B.Sc) in Medical'),
        ('Bachelor of Science (B.Sc) in Economics – Honors', 'Bachelor of Science (B.Sc) in Economics – Honors'),
        ('Bachelor of Technology (B.Tech)', 'Bachelor of Technology (B.Tech)'),
        ('Bachelor of Business Administration, LLB (Hons.)', 'Bachelor of Business Administration, LLB (Hons.)'),
        ('Bachelor of Arts, LLB (Hons.)', 'Bachelor of Arts, LLB (Hons.)'),
        ('Bachelor of Design (B.Des)', 'Bachelor of Design (B.Des)'),
        ('Bachelor of Architecture (B.Arch)', 'Bachelor of Architecture (B.Arch)'),
        ('Bachelor of Business Administration (BBA – Gen/Hons)', 'Bachelor of Business Administration (BBA – Gen/Hons)'),
        ('Bachelor of Science (B.Sc) in Nursing', 'Bachelor of Science (B.Sc) in Nursing'),
        ('Bachelor of Arts (B.A) in Performing Arts', 'Bachelor of Arts (B.A) in Performing Arts'),
        ('Bachelor of Business Administration – BBA (Hons) in Business Analytics', 'Bachelor of Business Administration – BBA (Hons) in Business Analytics'),
        ('BBA – Hospitality & Event Management (BBA-HEM)', 'BBA – Hospitality & Event Management (BBA-HEM)'),
        ('Bachelor of Commerce – B.Com (Hons) with ACCA', 'Bachelor of Commerce – B.Com (Hons) with ACCA'),
        ('BBA – Sports Management', 'BBA – Sports Management'),
        ('Master of Technology (M.Tech)', 'Master of Technology (M.Tech)'),
        ('Master of Business Administration (MBA)', 'Master of Business Administration (MBA)'),
        ('Master of Computer Application (MCA)', 'Master of Computer Application (MCA)'),
        ('Master of Technology by Research', 'Master of Technology by Research'),
        ('Doctor of Philosophy (Ph.D)', 'Doctor of Philosophy (Ph.D)'),
        ('Bachelor of Commerce – B.Com (General/ Hons/ Evening College)', 'Bachelor of Commerce – B.Com (General/ Hons/ Evening College)'),
        ('Master of Commerce (M.Com)', 'Master of Commerce (M.Com)'),
        ('Bachelor of Science – B.Sc (Hons) in Psychology', 'Bachelor of Science – B.Sc (Hons) in Psychology')
    ]
    program = forms.ChoiceField(
        choices=PROGRAM, label='Program',required=True,
        widget=forms.Select(attrs={'class': 'form-select', 'data-trigger': 'true', 'name': 'choices-single-default', 'id': 'choices-single-default'})
    )
    
    class Meta:
        model = RRTransportation
        fields = ('name', 'phone_number', 'parent_phone_number', 'email', 'address', 'dob', 'registration_no', 'blood_group', 'photo', 'program', 'route', 'pickup_point')
        widgets = {
            'address': forms.Textarea(attrs={'class': 'form-control', "rows":"4", 'placeholder':"Type your address here.."}),
        }
        
        
    def __init__(self, *args, **kwargs):
        route = kwargs.pop('route', None)
        super().__init__(*args, **kwargs)
        if route:
            self.fields['pickup_point'].choices = [(point, point) for point in RR_PICKUP_POINT_CHOICES.get(route, [])]
        else:
            self.fields['pickup_point'].choices = [('', 'Choose a Pickup Point')]
        

EC_ROUTE_CHOICES = [
        ('', 'Choose a Route'),
        ('Route 1', 'Route 1'),
        ('Route 2', 'Route 2'),
        ('Route 3', 'Route 3'),
        ('Route 4', 'Route 4'),
        ('Route 5', 'Route 5'),
        ('Route 6', 'Route 6'),
        ('Route 7', 'Route 7'),
        ('Route 8', 'Route 8'),
    ]
EC_PICKUP_POINT_CHOICES = {
        "Route 1":['Banaswadi Main Road - HP Petrol Bunk','Uttam Sagar','Horamau Signal','Ramamurthynagar Jn.','Kasturinagar Ring Road','Tin Factory','KR Puram Railway Station','B Narayanapura Ring Road Jn.','Mahadevpura Ring Road Jn.','Doddanekkundi Ring Road Jn.','Kartiknagar Ring Road Jn.','Multiplex-Marathahalli','Bellandur Ring Road Jn.','Sarjapura / Iblur Junction.','Agara','CPWD Quarters','MK Ahmed','HSR Water Tank','HSR BDA Complex','Mangammanapalya','Bomanahalli'],
        "Route 2":['Halsoor Lake (Ganapathy Temple)','Old Madras Road','Indiranagar KFC', 'CMH Hospital','Thippasandra EntrancenBus stop','Jeevan Bima Nagar Bus stop','Beml Compound','Hal Road Signal','Rajeshwari Theater','Mnipal Bus stop','Domlur Flyover','Ejipura','Koramangala Sony World Signal','WIPRO Park','Venkatapura Bus Stop','Madivala Police Station','Roopna Agrahara Bus Stop'],
        "Route 3":['Hebbala Flyover/Ganganagar Road','Ganganagar CBI Bustand','Mechri Circle','Sadashiv nagar Police Station','Tata institute','Yeshwantpura Police Station','Mahalaxmi Layout','Rajaji nagar Metro station','Varier Beakery','Vijayanagar Bus Stop','Maruthi Mandir','Attiguppe','Dipanjali Nagar','Mysore Road Metro Staton'],
        "Route 4":['Kadranahalli Cross','Kumarswamy Layout','ISRO Layout','Konankunte Cross','Yelechanahalli','Sindhoor Klyan Mantapa','J.P. Nagar 15th Cross','DELMIYA','Mandovi Motors','Reliance Mart','Meenakshi Mall','Gottigere / Bannerghatta Road','NICE Road'],
        "Route 5":['Sai Baba Hospital','Fire Station Sarjapur Road','CMRIT College','Kundanahalli Junction','Multiplex-Marathahalli','New Horizon College Of Engineering','Ecospace','Bellandur Junction','Iblur Junction','Agara Junction','CPWD Quarters','MK Ahmed Supermarket','HSR Water Tank','HSR BDA Complex','Mangammanapalya','Bommanahalli Bus Stop'],
        "Route 6":['PESU RR Campus','Janatha Bazar','Katriguppe','Kamakya','Devegowda Petrol Bunk','Mandovi Motors','Bilekahalli','Apollo Hospital / Wockhardt Hospital','Ayappa Temple','Reliance / Hulimavu','BPL','Meenakshi Temple','Kaalena Agrhara','Gottigere','NICE Road'],
        "Route 7":['Innovative Multiplex, Marathahalli','Kadubeesanahalli Bus Stop','New Horizon College','Eco space','Central Mall, Bellandur','HP petrol bunk','wipro gate','Kaikonanahalli Bus stop','Fire Satation','Harlur Road Bus stop','Iblur junction','Agara Junction','HSR Layout Police Station','CPWED Quarters','MK Ahamad','Kempegouda Circle','BDA Complex Mc Donalds'],
        "Route 8":['Attibele Circle (checkpost)','Guestline Hotel Bus Stop BMTC, Attibele','Neraluru Bus Stop', 'Hale Chandapura Bus stop','Chandapura Circle','Kittanahalli Bus Stop','Narayana Hrudralaya Bus Stop (NH)','Bommasandra Bus Stop','Hebbagudi Bus Stop','Veerasandra Bus Stop','Electronic City Bus Stop'],
    }

class ECTransportationForm(forms.ModelForm):
    MAX_IMAGE_SIZE = 500 * 1024  # 500KB in bytes

    def clean_photo(self):
        photo = self.cleaned_data.get('photo', None)
        if photo and photo.size > self.MAX_IMAGE_SIZE:
            raise ValidationError("Image file size cannot exceed 500KB")
        return photo
    
    name = create_name_field()
    phone_number = create_phone_number_field()
    parent_phone_number = create_parent_phone_number_field()
    email = create_email_field()
    def clean_email(self):
        email = self.cleaned_data['email']
        cleaned_email = email.strip()  # Remove leading and trailing whitespace
        return cleaned_email
    
    dob = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'date',
            'class': 'form-control',
        })
    )
    
    blood_group = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': 'Type your blood group here',
            'class': 'form-control',
        })
    )
    
    registration_no = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': 'Type your registeration number here',
            'class': 'form-control',
        })
    )
    
    photo = forms.FileField(widget=forms.ClearableFileInput(attrs={
        'class': 'form-control',
        'id': 'formFile',
        'accept': '.pdf,.jpg,.jpeg,.png',
    }))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['photo'].widget.attrs.update({
            'type': 'file',  # 'type': 'file' is already the default for FileField widget
        })
    
    

    route = forms.ChoiceField(choices=EC_ROUTE_CHOICES, label='Route',
                              widget=forms.Select(attrs={'class': 'form-select', 'data-trigger': 'true', 'id': 'route'}))
    pickup_point = forms.ChoiceField(label='Pickup Point',
                                     widget=forms.Select(attrs={'class': 'form-select', 'id': 'pickup_point'}))
    
    PROGRAM = [
        ('Bachelor of Technology', 'Bachelor of Technology'),
        ('Bachelor of Business Administration (General / Hons)', 'Bachelor of Business Administration (General / Hons)'),
        ('Bachelor of Science (B.Sc) in Nursing', 'Bachelor of Science (B.Sc) in Nursing'),
        ('Bachelor of Commerce', 'Bachelor of Commerce'),
        ('Bachelor of Pharmacy', 'Bachelor of Pharmacy'),
        ('Master of Pharmacy', 'Master of Pharmacy'),
        ('Doctor of Pharmacy', 'Doctor of Pharmacy'),
        ('MBA from IUP', 'MBA from IUP'),
    ]
    program = forms.ChoiceField(
        choices=PROGRAM, label='program',
        widget=forms.Select(attrs={'class': 'form-select', 'data-trigger': 'true', 'name': 'choices-single-default', 'id': 'choices-single-default'})
    )
    
    class Meta:
        model = ECTransportation
        fields = ('name', 'phone_number', 'parent_phone_number', 'email', 'address', 'dob', 'registration_no', 'blood_group', 'photo', 'program', 'route', 'pickup_point')
        widgets = {
            'address': forms.Textarea(attrs={'class': 'form-control', "rows":"4", 'placeholder':"Type your address here.."}),
        }
        
        
    def __init__(self, *args, **kwargs):
        route = kwargs.pop('route', None)
        super().__init__(*args, **kwargs)
        if route:
            self.fields['pickup_point'].choices = [(point, point) for point in EC_PICKUP_POINT_CHOICES.get(route, [])]
        else:
            self.fields['pickup_point'].choices = [('', 'Choose a Pickup Point')]
        
        
class FAQForm(forms.ModelForm):
    question = forms.CharField(
        label='Question',
        widget=forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Type your Question here..',
        })
    )
    
    CATEGORY_CHOICE = (
        # ('Admissions', 'Admissions'),
        # ('Counseling', 'Counseling'),
        ('Placement', 'Placement'),
        ('Hostel', 'Hostel'),
        ('Transportation', 'Transportation'),
        ('General', 'General'),
    )
    category = forms.MultipleChoiceField(
        choices=CATEGORY_CHOICE,
        label='Category',
        required=True,
        widget=forms.SelectMultiple(attrs={'class': 'form-select'})
    )

    priority = forms.IntegerField(widget=forms.NumberInput(attrs={ 'class':'form-control', 'id':'input-password', 'placeholder': 'Please enter a Priority No'}),
        required=True)


    class Meta:
        model = FAQ
        fields = ('question', 'answer', 'priority', 'category')
        # answer = forms.CharField(widget=CKEditorWidget())
        widgets = {
            'answer': forms.Textarea(attrs={'class': 'form-control', 'placeholder':"Type your Answer here.."}),
            'category': forms.CheckboxSelectMultiple(attrs={'class':"form-select",'type':"checkbox", 'role':"switch", 'id':"switch-sm"}),
        }
        
        
def get_faq_form(model_class):
    class DynamicFAQForm(forms.ModelForm):
        question = forms.CharField(
            label='Question',
            widget=forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Type your Question here..',
            })
        )
        
        priority = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Priority'}))
        
        class Meta:
            model = model_class
            fields = ('question', 'answer', 'priority', 'category')
            widgets = {
                'answer': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Type your Answer here.."}),
                'category': forms.CheckboxSelectMultiple(attrs={'required':True}),
            }
        def clean_category(self):
            category = self.cleaned_data.get('category')
            if not category:
                raise forms.ValidationError("At least one category must be selected.")
            return category
        
    return DynamicFAQForm



SPECIALIZATION_SELECT = (
    ('Computer Science (CSE)', 'Computer Science (CSE)'),
    ('Computer Science (CSE) - AIML', 'Computer Science (CSE) - AIML'),
    ('Electronics & Communication (ECE)', 'Electronics & Communication (ECE)'),
    ('Electrical & Electronics (EEE)', 'Electrical & Electronics (EEE)'),
    ('Mechanical (ME)', 'Mechanical (ME)'),
    ('Biotechnology (BT)', 'Biotechnology (BT)'),
    ('Architecture (Arch)', 'Architecture (Arch)'),
)
CAMPUS_SELECT = (
    ('Ring Road Campus (Banashankari 3rd Stage)', 'Ring Road Campus (Banashankari 3rd Stage)'),
    ('Electronic City Campus (Hosur Road)', 'Electronic City Campus (Hosur Road)'),
) 


class CETRankingForm(forms.ModelForm):
    name = create_name_field()
    phone_number = create_phone_number_field()
    email =  create_email_field()
    def clean_email(self):
        email = self.cleaned_data['email']
        cleaned_email = email.strip()  # Remove leading and trailing whitespace
        return cleaned_email
    
    registration_number = forms.CharField(
        label='Application Number',
        required=True,
        widget=forms.TextInput(attrs={
            'type': 'number',
            'placeholder': 'Type your application number here',
            'class': 'form-control',
        })
    )
    
    TAKEN_KCET = (
        (True, 'Yes'),
        (False, 'No'),
    )    
    taken_kcet = forms.ChoiceField(
        choices=TAKEN_KCET, label='Taken KCET', 
        # widget=forms.RadioSelect(attrs={
        #     'class': 'btn-check',
        # }), 
        required=True,
    )
    
    kcet_rank = forms.CharField(
        label='KCET Rank',
        required=False,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': 'Type your kcet rank here',
            'class': 'form-control',
        })
    )
    
    # taken_kcet = forms.BooleanField(
    #     label='Taken KCET',
    #     required=False,
    #     widget=forms.CheckboxInput(attrs={
    #         'class': 'form-check-input',
    #         # 'id': 'reverseCheck1',
    #     })
    # )
    
    kcet_registration_number = forms.CharField(
        label='KCET Registration Number',
        required=False,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': 'Type your kcet registeration number here',
            'class': 'form-control',
        })
    )

    specialization = forms.ChoiceField(
        choices=SPECIALIZATION_SELECT,
        label='Specialization',
        widget=forms.Select(attrs={'class': 'form-select', 'data-trigger': 'true', 'name': 'choices-single-default', 'id': 'choices-single-default'}),
        required=True
    )
    campus = forms.ChoiceField(
        choices=CAMPUS_SELECT, label='Campus',
        widget=forms.Select(attrs={'class': 'form-select', 'data-trigger': 'true', 'name': 'choices-single-default', 'id': 'choices-single-default'}),
        required=True
    )
    
    class Meta:
        model = CETRanking
        fields = [
            'name', 'email', 'phone_number', 'registration_number',
            'taken_kcet', 'specialization', 'campus', 'kcet_rank',
            'kcet_registration_number'
        ]

    def clean(self):
        cleaned_data = super().clean()
        taken_kcet = cleaned_data.get('taken_kcet')

        # Check if 'taken_kcet' is a string and convert it to a boolean if needed
        if taken_kcet == 'True' or taken_kcet is True:
            required_fields = ['kcet_rank', 'kcet_registration_number']
            for field in required_fields:
                if not cleaned_data.get(field):
                    self.add_error(field, f'{field.replace("_", " ").capitalize()} is required.')
        elif taken_kcet == 'False' or taken_kcet is False:
            # Clear fields if 'No' is selected
            cleaned_data['kcet_rank'] = None
            cleaned_data['kcet_registration_number'] = None

        # Ensure optional fields are set to None if empty
        for field in ['kcet_rank', 'kcet_registration_number', 'specialization', 'campus']:
            value = cleaned_data.get(field)
            if value == '':
                cleaned_data[field] = None
            elif value is not None and field in ['kcet_rank']:
                try:
                    cleaned_data[field] = int(value)
                except ValueError:
                    self.add_error(field, f'{field.replace("_", " ").capitalize()} must be a number.')

        return cleaned_data




class JEEMain1Form(forms.ModelForm):
    name = create_name_field()
    phone_number = create_phone_number_field()
    email =  create_email_field()
    def clean_email(self):
        email = self.cleaned_data['email']
        cleaned_email = email.strip()  # Remove leading and trailing whitespace
        return cleaned_email
    
    TAKEN_JEE_MAIN1 = (
        (True, 'Yes'),
        (False, 'No'),
    )    
    taken_jee_main1 = forms.ChoiceField(
        choices=TAKEN_JEE_MAIN1, label='Taken JEE MAIN 1', 
        required=True,
    )
    # taken_jee_main1 = forms.BooleanField(
    #     label='Taken JEE Main 1',
    #     required=False,
    #     widget=forms.CheckboxInput(attrs={
    #         'class': 'form-check-input',
    #         # 'id': 'reverseCheck1',
    #     })
    # )
    registration_number = forms.CharField(
        label='Application Number',
        required=True,
        widget=forms.TextInput(attrs={
            'type': 'number',
            'placeholder': 'Type your application number here',
            'class': 'form-control',
        })
    )
    
    jee_main1_rank = forms.DecimalField(
        label='JEE Main 1 Rank',
        required=False,
        max_digits=9,
        decimal_places=6,
        validators=[
            RegexValidator(
                regex=r'^\d{1,2}(\.\d{1,6})?$',  # Only 1 or 2 digits before decimal
                message='Please enter a valid rank with up to 6 decimal places.'
            )
        ],
        widget=forms.NumberInput(attrs={
            'placeholder': 'Type your rank here',
            'class': 'form-control',
        })
    )
    
    jee_main1_registration_number = forms.CharField(
        label='Registration Number',
        required=False,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': 'Type your registeration number here',
            'class': 'form-control',
        })
    )

    specialization = forms.ChoiceField(
        choices=SPECIALIZATION_SELECT,
        label='Specialization',
        widget=forms.Select(attrs={'class': 'form-select', 'data-trigger': 'true', 'name': 'choices-single-default', 'id': 'choices-single-default'}),
        required=True
    )
    campus = forms.ChoiceField(
        choices=CAMPUS_SELECT, label='Campus',
        widget=forms.Select(attrs={'class': 'form-select', 'data-trigger': 'true', 'name': 'choices-single-default', 'id': 'choices-single-default'}),
        required=True
    )
    
    MAX_IMAGE_SIZE = 500 * 1024  # 500 KB

    upload_marks = forms.FileField(
        label='Upload Marks',
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'id': 'formFile',
            'accept': '.pdf,.jpg,.jpeg,.png',
        })
    )

    def clean_upload_marks(self):
        upload_marks = self.cleaned_data.get('upload_marks', None)
        if upload_marks:
            # Validate file size
            if upload_marks.size > self.MAX_IMAGE_SIZE:
                raise ValidationError("File size cannot exceed 500KB.")

            # Validate file type
            valid_extensions = ['.pdf', '.jpg', '.jpeg', '.png']
            extension = upload_marks.name.split('.')[-1].lower()
            if f".{extension}" not in valid_extensions:
                raise ValidationError("Invalid file type. Allowed types: .pdf, .jpg, .jpeg, .png.")

        return upload_marks

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
        
    #     # Update the attributes of the 'upload_marks' field
    #     self.fields['upload_marks'].widget.attrs.update({
    #         'type': 'file',  # 'type': 'file' is already the default for FileField widget
    #     })
    
    class Meta:
        model = JEEMain1
        fields = [
            'name', 'email', 'phone_number', 'registration_number',
            'taken_jee_main1', 'specialization', 'campus', 'jee_main1_rank',
            'jee_main1_registration_number', 'upload_marks'
        ]

    def clean(self):
        cleaned_data = super().clean()
        taken_jee_main1 = cleaned_data.get('taken_jee_main1')

        if taken_jee_main1 == 'True' or taken_jee_main1 is True:
            required_fields = ['jee_main1_rank', 'jee_main1_registration_number', 'upload_marks']
            for field in required_fields:
                if not cleaned_data.get(field):
                    self.add_error(field, f'{field.replace("_", " ").capitalize()} is required.')
        elif taken_jee_main1 == 'False' or taken_jee_main1 is False:
            # Set optional fields to None if not filled
            for field in ['jee_main1_rank', 'jee_main1_registration_number', 'upload_marks']:
                if field in cleaned_data:
                    cleaned_data[field] = None

        return cleaned_data
    
    def clean_jee_main1_rank(self):
        value = self.cleaned_data.get('jee_main1_rank')
        print("Form value for jee_main1_rank:", value)  # Debugging output
        return value


class JEEMain2Form(forms.ModelForm):
    name = create_name_field()
    phone_number = create_phone_number_field()
    email =  create_email_field()
    def clean_email(self):
        email = self.cleaned_data['email']
        cleaned_email = email.strip()  # Remove leading and trailing whitespace
        return cleaned_email
    
    TAKEN_JEE_MAIN2 = (
        (True, 'Yes'),
        (False, 'No'),
    )    
    taken_jee_main2 = forms.ChoiceField(
        choices=TAKEN_JEE_MAIN2, label='Taken JEE MAIN 2', 
        required=True,
    )
    
    registration_number = forms.CharField(
        label='Application Number',
        required=True,
        widget=forms.TextInput(attrs={
            'type': 'number',
            'placeholder': 'Type your application number here',
            'class': 'form-control',
        })
    )
    
    jee_main2_rank = forms.DecimalField(
        label='JEE Main 2 Rank',
        required=False,
        max_digits=9,
        decimal_places=6,
        validators=[
            RegexValidator(
                regex=r'^\d{1,2}(\.\d{1,6})?$',  # Only 1 or 2 digits before decimal
                message='Please enter a valid rank with up to 6 decimal places.'
            )
        ],
        widget=forms.NumberInput(attrs={
            'placeholder': 'Type your rank here',
            'class': 'form-control',
        })
    )
    
    crl_rank = forms.DecimalField(
        label='All India CRL Rank',
        required=False,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Type your rank here',
            'class': 'form-control',
        })
    )
    
    
    jee_main2_registration_number = forms.CharField(
        label='Registration Number',
        required=False,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': 'Type your registeration number here',
            'class': 'form-control',
        })
    )

    specialization = forms.ChoiceField(
        choices=SPECIALIZATION_SELECT,
        label='Specialization',
        widget=forms.Select(attrs={'class': 'form-select', 'data-trigger': 'true', 'name': 'choices-single-default', 'id': 'choices-single-default'}),
        required=True
    )
    campus = forms.ChoiceField(
        choices=CAMPUS_SELECT, label='Campus',
        widget=forms.Select(attrs={'class': 'form-select', 'data-trigger': 'true', 'name': 'choices-single-default', 'id': 'choices-single-default'}),
        required=True
    )
    
    MAX_IMAGE_SIZE = 500 * 1024  # 500 KB

    upload_marks = forms.FileField(
        label='Upload Marks',
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'id': 'formFile',
            'accept': '.pdf,.jpg,.jpeg,.png',
        })
    )

    def clean_upload_marks(self):
        upload_marks = self.cleaned_data.get('upload_marks', None)
        if upload_marks:
            # Validate file size
            if upload_marks.size > self.MAX_IMAGE_SIZE:
                raise ValidationError("File size cannot exceed 500KB.")

            # Validate file type
            valid_extensions = ['.pdf', '.jpg', '.jpeg', '.png']
            extension = upload_marks.name.split('.')[-1].lower()
            if f".{extension}" not in valid_extensions:
                raise ValidationError("Invalid file type. Allowed types: .pdf, .jpg, .jpeg, .png.")

        return upload_marks
    
    class Meta:
        model = JEEMain2
        fields = [
            'name', 'email', 'phone_number', 'registration_number',
            'taken_jee_main2', 'specialization', 'campus', 'jee_main2_rank',
            'jee_main2_registration_number', 'upload_marks', 'crl_rank'
        ]

    def clean(self):
        cleaned_data = super().clean()
        taken_jee_main2 = cleaned_data.get('taken_jee_main2')

        if taken_jee_main2 == 'True' or taken_jee_main2 is True:
            required_fields = ['jee_main2_rank', 'crl_rank', 'jee_main2_registration_number', 'upload_marks']
            for field in required_fields:
                if not cleaned_data.get(field):
                    self.add_error(field, f'{field.replace("_", " ").capitalize()} is required.')
        elif taken_jee_main2 == 'False' or taken_jee_main2 is False:
            # Set optional fields to None if not filled
            for field in ['jee_main2_rank', 'crl_rank', 'jee_main2_registration_number', 'upload_marks']:
                if field in cleaned_data:
                    cleaned_data[field] = None

        return cleaned_data
    
    def clean_jee_main2_rank(self):
        value = self.cleaned_data.get('jee_main2_rank')
        print("Form value for jee_main2_rank:", value)  # Debugging output
        return value



class COMEDKForm(forms.ModelForm):
    name = create_name_field()
    phone_number = create_phone_number_field()
    email =  create_email_field()
    def clean_email(self):
        email = self.cleaned_data['email']
        cleaned_email = email.strip()  # Remove leading and trailing whitespace
        return cleaned_email
    
    TAKEN_COMEDK = (
        (True, 'Yes'),
        (False, 'No'),
    )    
    taken_comedk = forms.ChoiceField(
        choices=TAKEN_COMEDK, label='Taken COMEDK', 
        required=True,
    )

    
    registration_number = forms.CharField(
        label='Application Number',
        required=True,
        widget=forms.TextInput(attrs={
            'type': 'number',
            'placeholder': 'Type your application number here',
            'class': 'form-control',
        })
    )
    
    comedk_rank = forms.IntegerField(
        label='COMEDK Rank',
        required=False,
        widget=forms.NumberInput(attrs={
            'type': 'text',
            'placeholder': 'Type your rank here',
            'class': 'form-control',
            'min': '1',
            'max': '999999',
        }),
        validators=[MinValueValidator(1), MaxValueValidator(999999)],
    )

    
    tat_number = forms.CharField(
        label='COMEDK TAT Number',
        required=False,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': 'Type your tat number here',
            'class': 'form-control',
        })
    )
    
    comedk_registration_number = forms.CharField(
        label='Registration Number',
        required=False,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': 'Type your registeration number here',
            'class': 'form-control',
        })
    )

    specialization = forms.ChoiceField(
        choices=SPECIALIZATION_SELECT,
        label='Specialization',
        widget=forms.Select(attrs={'class': 'form-select', 'data-trigger': 'true', 'name': 'choices-single-default', 'id': 'choices-single-default'}),
        required=True
    )
    campus = forms.ChoiceField(
        choices=CAMPUS_SELECT, label='Campus',
        widget=forms.Select(attrs={'class': 'form-select', 'data-trigger': 'true', 'name': 'choices-single-default', 'id': 'choices-single-default'}),
        required=True
    )
    
    MAX_IMAGE_SIZE = 500 * 1024  # 500 KB

    upload_marks = forms.FileField(
        label='Upload Marks',
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'id': 'formFile',
            'accept': '.pdf,.jpg,.jpeg,.png',
        })
    )

    def clean_upload_marks(self):
        upload_marks = self.cleaned_data.get('upload_marks', None)
        if upload_marks:
            # Validate file size
            if upload_marks.size > self.MAX_IMAGE_SIZE:
                raise ValidationError("File size cannot exceed 500KB.")

            # Validate file type
            valid_extensions = ['.pdf', '.jpg', '.jpeg', '.png']
            extension = upload_marks.name.split('.')[-1].lower()
            if f".{extension}" not in valid_extensions:
                raise ValidationError("Invalid file type. Allowed types: .pdf, .jpg, .jpeg, .png.")

        return upload_marks
    
    class Meta:
        model = COMEDK
        fields = [
            'name', 'email', 'phone_number', 'registration_number',
            'taken_comedk', 'specialization', 'campus', 'comedk_rank',
            'comedk_registration_number', 'tat_number', 'upload_marks'
        ]

    def clean(self):
        cleaned_data = super().clean()
        taken_comedk = cleaned_data.get('taken_comedk')

        if taken_comedk == 'True' or taken_comedk is True:
            required_fields = ['comedk_rank', 'comedk_registration_number', 'tat_number', 'upload_marks']
            for field in required_fields:
                if not cleaned_data.get(field):
                    self.add_error(field, f'{field.replace("_", " ").capitalize()} is required.')
        elif taken_comedk == 'False' or taken_comedk is False:
            # Set optional fields to None if not filled
            for field in ['comedk_rank', 'comedk_registration_number', 'tat_number', 'upload_marks']:
                if field in cleaned_data:
                    cleaned_data[field] = None

        return cleaned_data
    
    def clean_comedk_rank(self):
        value = self.cleaned_data.get('comedk_rank')
        print("Form value for comedk_rank:", value)  # Debugging output
        return value


   
    
    
class PUCUpoloadMarksForm(forms.ModelForm):   
    name = create_name_field()
    phone_number = create_phone_number_field()
    email = create_email_field()
    def clean_email(self):
        email = self.cleaned_data['email']
        cleaned_email = email.strip()  # Remove leading and trailing whitespace
        return cleaned_email
    
    BOARD_SELECT = (
        ('Karnataka PU Board', 'Karnataka PU Board'),
        ('CBSE', 'CBSE'),
        ('ICSE', 'ICSE'),
        ('IGCSE', 'IGCSE'),
        ('IB', 'IB'),
        ('Others', 'Others'),
    )
    # board = forms.ChoiceField(
    #     choices=BOARD_SELECT, label='Which Board do you belong to?',
    #     widget=forms.Select(attrs={'class': 'form-control', 'data-trigger': 'true', 'name': 'choices-single-default', 'id': 'choices-single-default'})
    # )
    board = forms.ChoiceField(
        choices=BOARD_SELECT,
        label='Board',
        widget=forms.Select(attrs={'class': 'form-select', 'data-trigger': 'true', 'name': 'status-choices-single-default', 'id': 'status-choices-single-default'}),
    )
    # STATUS_SELECT = (
    #         (True, "Published"),
    #         (False, "Unpublish"),
    # )
    # status = forms.ChoiceField(
    #     choices=STATUS_SELECT,
    #     label='Status',
    #     widget=forms.Select(attrs={'class': 'form-control', 'data-trigger': 'true', 'name': 'status-choices-single-default', 'id': 'status-choices-single-default'}),
    # )
    other_board = forms.CharField(
        label='Please specify your board', required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type your board name here'})
    )
    
    specialization = forms.ChoiceField(
        choices=SPECIALIZATION_SELECT, label='Specialization',
        widget=forms.Select(attrs={'class': 'form-select', 'data-trigger': 'true', 'name': 'choices-single-default', 'id': 'choices-single-default'})
    )
    
    campus = forms.ChoiceField(
        choices=CAMPUS_SELECT, label='Campus',
        widget=forms.Select(attrs={'class': 'form-select', 'data-trigger': 'true', 'name': 'choices-single-default', 'id': 'choices-single-default'})
    )
    
    declaration = forms.BooleanField(
        label='I hereby declare that I have passed in all the subjects in 12th/ 2nd PU/ equivalent exam',
        required=True,
    )
    
    registration_number = forms.CharField(
        label='Application Number',
        widget=forms.TextInput(attrs={
            'type': 'number',
            'placeholder': 'Type your application number here',
            'class': 'form-control',
        })
    )
    physics = create_number_field(label='Physics', placeholder='Enter your Physics marks here', required=True, max_value=100)
    chemistry = create_number_field(label='Chemistry', placeholder='Enter your Chemistry marks here', required=True, max_value=100)
    mathematics_a = create_number_field(label='Mathematics A', placeholder='Enter your Mathematics A marks here', required=True, max_value=100)
    mathematics_b = create_number_field(label='Mathematics B', placeholder='Enter your Mathematics B marks here', required=False, max_value=75)
    electronics = create_number_field(label='Electronics', placeholder='Enter your Electronics marks here', required=False, max_value=100)
    computer_science = create_number_field(label='Computer Science', placeholder='Enter your Computer Science marks here', required=False, max_value=100)
    biotechnology = create_number_field(label='Biotechnology', placeholder='Enter your biotechnology marks here', required=False, max_value=100)
    aggregate_percentage = create_decimal_number_field(label='Percentage %', placeholder='Enter your Percentage % here', required=True, max_value=100)
    
    MAX_IMAGE_SIZE = 500 * 1024  # 500 KB

    upload_marks = forms.FileField(
        label='Upload Marks',
        required=True,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'id': 'formFile',
            'accept': '.pdf,.jpg,.jpeg,.png',
        })
    )

    def clean_upload_marks(self):
        upload_marks = self.cleaned_data.get('upload_marks', None)
        if upload_marks:
            # Validate file size
            if upload_marks.size > self.MAX_IMAGE_SIZE:
                raise ValidationError("File size cannot exceed 500KB.")

            # Validate file type
            valid_extensions = ['.pdf', '.jpg', '.jpeg', '.png']
            extension = upload_marks.name.split('.')[-1].lower()
            if f".{extension}" not in valid_extensions:
                raise ValidationError("Invalid file type. Allowed types: .pdf, .jpg, .jpeg, .png.")

        return upload_marks

    
    # intermediate_candidates = forms.BooleanField(
    #     required=False,
    #     widget=forms.CheckboxInput(attrs={
    #         'class': 'form-check-input',
    #     })
    # )
    INTERMEDIATE_CANDIDATE = (
        (None, 'Choose a scoring system'),
        (True, 'AP and Telangana Intermediate (out of 75/90/100)'),
        (False, 'Other States (out of 100)'),
    )    
    # intermediate_candidates = forms.ChoiceField(
    #     choices=INTERMEDIATE_CANDIDATE, label='INTERMEDIATE CANDIDATE', 
    #     required=True,
    # )
    intermediate_candidates = forms.ChoiceField(
        choices=INTERMEDIATE_CANDIDATE, label='Choose a scoring system',
        widget=forms.Select(attrs={'class': 'form-select', 'data-trigger': 'true', 'name': 'intermediate_candidates', 'id': 'id_intermediate_candidates'})
    )
    
    declaration = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
        })
    )
    
    # Alternatively, you can override the field to make it optional
    comment = forms.CharField(
        required=False,  # This makes the field optional
        widget=forms.Textarea(attrs={
            'class': 'form-control', "rows":"3", 
            'placeholder': "Type your comment here.."
        })
    )
    class Meta:
        model = PUCUpoloadMarks
        fields = [
            'board', 'other_board', 'name', 'email', 'phone_number', 'registration_number', 'intermediate_candidates',
            'specialization', 'campus', 'physics', 'chemistry', 'mathematics_a', 'mathematics_b',
            'electronics', 'computer_science', 'biotechnology', 'aggregate_percentage', 'upload_marks', 'comment', 'declaration'
        ]
        # widgets = {
        #     'comment': forms.Textarea(attrs={'class': 'form-control','placeholder':"Type your comment here.."}),
        # }

    def clean(self):
        cleaned_data = super().clean()
        board = cleaned_data.get('board')
        other_board = cleaned_data.get('other_board')
        intermediate_candidates = cleaned_data.get('intermediate_candidates')
        declaration = cleaned_data.get('declaration')

        # Check if 'Others' is selected for board and if other_board field is filled
        if board == 'Others':
            if not other_board:
                self.add_error('other_board', 'This field is required if you select Others.')
            else:
                cleaned_data['board'] = other_board  # Store the value of other_board in board
            
        if not declaration:
            self.add_error('declaration', 'You must agree to the declaration.')

        # Additional existing validation
        if intermediate_candidates == 'True' or intermediate_candidates is True:
            required_fields = ['mathematics_b']
            # for field in required_fields:
            #     if not cleaned_data.get(field):
            #         self.add_error(field, f'{field.replace("_", " ").capitalize()} is required.')
        elif intermediate_candidates == 'False' or intermediate_candidates is False:
            cleaned_data['mathematics_b'] = None

        return cleaned_data
    


class GroupPermissionForm(forms.ModelForm):
    name = create_name_field()
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(
        # content_type_id__in=[1, 4, 18, 19, 20]
    ),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        required=False
    )

    class Meta:
        model = Group
        fields = ['name', 'permissions']
        

class DailyReportForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Type here..',
        })
    )
    
    date = forms.CharField(
        label='date',
        widget=forms.TextInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'placeholder': 'Type here..',
        })
    )
    
    STATUS =[
        ('Complete','Complete'),
        ('In Progress','In Progress'),
        ('Pending','Pending'),
    ]
    status = forms.ChoiceField(
        choices=STATUS, label='status',
        widget=forms.Select(attrs={'class': 'form-select', 'data-trigger': 'true', 'name': 'choices-single-default', 'id': 'choices-single-default'}),
    )
    
    DAILY_REPORT_CAMPUS =[
        ('PES University RR Campus','PES University RR Campus'),
        ('PES University EC Campus','PES University EC Campus'),
        ('PES Medical College Kuppam','PES Medical College Kuppam'),
        ('PES Degree College','PES Degree College'),
        ('PES College of Pharmacy','PES College of Pharmacy'),
        ('Amaatra Academy','Amaatra Academy'),
        ('PES Public School','PES Public School'),
        ('Polytechnic','Polytechnic'),
        ('PES PU','PES PU'),
        ('Hanumanth Nagar Campus','Hanumanth Nagar Campus'),
    ]
    campus = forms.ChoiceField(
        choices=DAILY_REPORT_CAMPUS, label='Campus',
        widget=forms.Select(attrs={'class': 'form-select', 'data-trigger': 'true', 'name': 'choices-single-default', 'id': 'choices-single-default'}),
    )


    CATEGORY_CHOICE = (
        ('Web Update', 'Web Update'),
        ('Emailer', 'Emailer'),
        ('Video', 'Video'),
        ('Photography', 'Photography'),
        ('Design', 'Design'),
        ('Development', 'Development'),
        ('Social Media', 'Social Media'),
    )
    category = forms.MultipleChoiceField(
        choices=CATEGORY_CHOICE,
        label='Category',
        widget=forms.SelectMultiple(attrs={'class': 'form-control', 'data-trigger': 'true', 'name': 'choices-multiple-remove-button', 'id': 'choices-multiple-remove-button'})
    )
    

    class Meta:
        model = DailyReport
        fields = ('title', 'description', 'status', 'date', 'campus', 'category')
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', "rows":"8", 'placeholder':"Type your Description here.."}),
        }


class AdminUserCreationForm(UserCreationForm):
    MAX_IMAGE_SIZE = 300 * 1024  # 300KB in bytes

    def clean_pic(self):
        pic = self.cleaned_data.get('pic', None)
        if pic and pic.size > self.MAX_IMAGE_SIZE:
            raise ValidationError("Image file size cannot exceed 300KB")
        return pic

    name = create_name_field()
    phone = forms.CharField(
        label='Full Name',
        widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': 'Type phone number here',
            'class': 'form-control',
        }),
        required=False,
    )
    username = forms.EmailField(
        label='',
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Example@pes.edu',
                'title': 'Please enter a valid email address',
                'class': 'form-control',
            }
        ),
        required=True,
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        return username.strip()

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control'}), required=True)

    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-input-field django-chickbox'}),
        required=True,
    )

    class Meta:
        model = User
        fields = ('name', 'username', 'password1', 'password2', 'pic', 'phone', 'details', 'is_superuser', 'groups', 'is_staff', 'is_active')
        widgets = {
            'pic': forms.FileInput(attrs={'class': 'form-control'}),
            'is_superuser': forms.CheckboxInput(attrs={'class': 'custom-toggle-switch'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'custom-toggle-switch'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'custom-toggle-switch'}),
            'details': forms.Textarea(attrs={'class': 'form-control','placeholder':"Type your details here.."}),
        }

class AdminUserEditForm(forms.ModelForm):
    MAX_IMAGE_SIZE = 300 * 1024  # 300KB in bytes

    def clean_pic(self):
        pic = self.cleaned_data.get('pic', None)
        if pic and pic.size > self.MAX_IMAGE_SIZE:
            raise ValidationError("Image file size cannot exceed 300KB")
        return pic

    name = create_name_field()
    phone = forms.CharField(
        label='Full Name',
        widget=forms.TextInput(attrs={
            'type': 'text',
            'placeholder': 'Type phone number here',
            'class': 'form-control',
        }),
        required=False,
    )
    username = forms.EmailField(
        label='',
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Example@pes.edu',
                'title': 'Please enter a valid email address',
                'class': 'form-control',
            }
        ),
        required=True
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        return username.strip()

    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': '', }),
        required=True,
    )


    class Meta:
        model = User
        fields = ('name', 'username', 'pic', 'is_superuser', 'phone', 'details', 'groups', 'is_staff', 'is_active')
        widgets = {
            'pic': forms.FileInput(attrs={'class': 'form-control'}),
            'is_superuser': forms.CheckboxInput(attrs={'class': 'custom-toggle-switch'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'custom-toggle-switch'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'custom-toggle-switch'}),
            'details': forms.Textarea(attrs={'class': 'form-control','placeholder':"Type your details here.."}),
        }

    # def save(self, commit=True):
    #     # check if a new image was uploaded
    #     if 'pic' in self.changed_data:
    #         old_pic = self.instance.pic
    #         # delete the old image file from the server
    #         if old_pic and default_storage.exists(old_pic.name):
    #             default_storage.delete(old_pic.name)
    #     # save the new image and form data
    #     user = super().save(commit=commit)
    #     return user
    
    