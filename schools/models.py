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
    areas = models.ManyToManyField(Area, blank=True)

    
    Motorcycle = 'Motorcycle'
    Car = 'Car'
    CarTowing = 'CarTowing'
    RigidTruck = 'RigidTruck'
    ArticulatedTruck = 'ArticulatedTruck'
    MiniBus = 'MiniBus'
    Coach = 'Coach'
    
    
   
    TRAININGAREAS = (
        (Motorcycle, 'Motorcycle'),
        (Car, 'Car'),
        (CarTowing, 'Car Towing'),
        (RigidTruck, 'Rigid Truck'),
        (ArticulatedTruck, 'Articulated Truck'),
        (MiniBus, 'Mini Bus'),
        (Coach, 'Coach'),
       
      
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
    
    
   
    
    rsa_number = models.CharField(max_length=8 )

    Dublin1 = 'Dublin 1'
    Dublin2 = 'Dublin 2'
    Dublin3 = 'Dublin 3'
    Dublin4 = 'Dublin 4'
    Dublin5 = 'Dublin 5'
    Dublin6 = 'Dublin 6'
    Dublin7 = 'Dublin 7'
    Dublin8 = 'Dublin 8'
    Dublin9 = 'Dublin 9'
    Dublin10 = 'Dublin 10'
    Dublin11 = 'Dublin 11'
    Dublin12 = 'Dublin 12'
    Dublin13 = 'Dublin 13'
    Dublin14 = 'Dublin 14'
    Dublin15 = 'Dublin 15'
    Dublin16 = 'Dublin 16'
    Dublin17 = 'Dublin 17'
    Dublin18 = 'Dublin 18'
    Dublin20 = 'Dublin 20'
    Dublin22 = 'Dublin 22'
    Dublin24 = 'Dublin 24'
   
    AREAS = (
        (Dublin1, 'Dublin 1'),
        (Dublin2, 'Dublin 2'),
        (Dublin3, 'Dublin 3'),
        (Dublin4, 'Dublin 4'),
        (Dublin5, 'Dublin 5'),
        (Dublin6, 'Dublin 6'),
        (Dublin7, 'Dublin 7'),
        (Dublin8, 'Dublin 8'),
        (Dublin9, 'Dublin 9'),
        (Dublin10, 'Dublin 10'),
        (Dublin11, 'Dublin 11'),
        (Dublin12, 'Dublin 12'),
        (Dublin13, 'Dublin 13'),
        (Dublin14, 'Dublin 14'),
        (Dublin15, 'Dublin 15'),
        (Dublin16, 'Dublin 16'),
        (Dublin17, 'Dublin 17'),
        (Dublin18, 'Dublin 18'),
        (Dublin20, 'Dublin 20'),
        (Dublin22, 'Dublin 22'),
        (Dublin24, 'Dublin 24'),
      
    )
    Area = MultiSelectField(choices=AREAS, default='Dublin1')
    Business_des = HTMLField(default="-")
    
    Lesson_Price_For_12 = models.DecimalField(max_digits=6, decimal_places=0, default=0)
    Lesson_Price_For_1 = models.DecimalField(max_digits=6, decimal_places=0, default=0)
    
    
    def __str__(self):
        return self.school_name


