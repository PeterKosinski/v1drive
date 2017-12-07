from django.db import models
from multiselectfield import MultiSelectField
from tinymce.models import HTMLField
from areas.models import Area


class School(models.Model):

    slug = models.SlugField(max_length=50, default="none" )
    logo = models.ImageField(upload_to="avatars", blank=True, null=True, default="avatars/profile.png")
    school_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=70,blank=True)
    phone_number = models.CharField(max_length=15, default=0)
    url = models.URLField()
  

    
    Motorcycle = 'Motorcycle'
    Car = 'Car'
  
    TRAININGAREAS = (
        (Motorcycle, 'Motorcycle'),
        (Car, 'Car'),
      
    )
    products = MultiSelectField(choices=TRAININGAREAS, default='Car')
    
    
    
    IndependentDrivingInstructor = 'Independent Driving Instructor'
    DrivingSchool = 'Driving School'
    InsuranceCompany = 'Insurance Company'
    
   
    TYPES = (
        (IndependentDrivingInstructor, 'Independent Driving Instructor'),
        (DrivingSchool, 'Driving School'),
        (InsuranceCompany, 'Insurance Company'),
       
      
    )
    school_type = models.CharField(choices=TYPES, default='Driving School', max_length=30)
    
    
   
    
    adi_number = models.CharField(max_length=8 )

    Carlow = 'Carlow'
    Cavan = 'Cavan'
    Clare = 'Clare'
    Cork = 'Cork'
    Donegal = 'Donegal'
    Dublin = 'Dublin'
    Galway = 'Galway'
    Kerry = 'Kerry'
    Kildare = 'Kildare'
    Kilkenny = 'Kilkenny'
    Laois = 'Laois'
    Leitrim = 'Leitrim'
    Limerick = 'Limerick'
    Longford = 'Longford'
    Louth = 'Louth'
    Mayo = 'Mayo'
    Meath = 'Meath'
    Monaghan = 'Monaghan'
    Offaly = 'Offaly'
    Roscommon = 'Roscommon'
    Sligo = 'Sligo'
    Tipperary = 'Tipperary'
    Waterford = 'Waterford'
    Westmeath = 'Westmeath'
    Wexford = 'Wexford'
    Wicklow = 'Wicklow'
   
    AREAS = (
        (Carlow, 'Carlow'),
        (Cavan, 'Cavan'),
        (Clare, 'Clare'),
        (Cork, 'Cork'),
        (Donegal, 'Donegal'),
        (Dublin, 'Dublin'),
        (Galway, 'Galway'),
        (Kerry, 'Kerry'),
        (Kildare, 'Kildare'),
        (Kilkenny, 'Kilkenny'),
        (Laois, 'Laois'),
        (Leitrim, 'Leitrim'),
        (Limerick, 'Limerick'),
        (Longford, 'Longford'),
        (Louth, 'Louth'),
        (Mayo, 'Mayo'),
        (Meath, 'Meath'),
        (Monaghan, 'Monaghan'),
        (Offaly, 'Offaly'),
        (Roscommon, 'Roscommon'),
        (Sligo, 'Sligo'),
        (Tipperary, 'Tipperary'),
        (Waterford, 'Waterford'),
        (Westmeath, 'Westmeath'),
        (Wexford, 'Wexford'),
        (Wicklow, 'Wicklow')
      
    )
    Area = MultiSelectField(choices=AREAS, default='Dublin1')
    Business_des = HTMLField(default="-")
    
    Lesson_Price_For_12 = models.DecimalField(max_digits=6, decimal_places=0, default=0)
    Lesson_Price_For_1 = models.DecimalField(max_digits=6, decimal_places=0, default=0)
    
    
    def __str__(self):
        return self.school_name


