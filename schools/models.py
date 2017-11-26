from django.db import models


class School(models.Model):

    slug = models.SlugField(max_length=50, default="none" )
    logo = models.ImageField(upload_to="avatars", blank=True, null=True, default="avatars/profile.png")
    school_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=70,blank=True)
    phone_number = models.CharField(max_length=15, default=0)
    url = models.URLField()
    rsa_number = models.CharField(max_length=8)

    Dublin1 = 'D1'
    Dublin2 = 'D2'
    Dublin3 = 'D3'
    Dublin4 = 'D4'
    Dublin5 = 'D5'
    Dublin6 = 'D6'
    Dublin7 = 'D7'
    Dublin8 = 'D8'
    Dublin9 = 'D9'
    Dublin10 = 'D10'
    Dublin11 = 'D11'
    Dublin12 = 'D12'
    Dublin13 = 'D13'
    Dublin14 = 'D14'
    Dublin15 = 'D15'
    Dublin16 = 'D16'
    Dublin17 = 'D17'
    Dublin18 = 'D18'
    Dublin20 = 'D20'
    Dublin22 = 'D22'
    Dublin24 = 'D24'
   
    AREAS = (
        (Dublin1, 'Dublin1'),
        (Dublin2, 'Dublin2'),
        (Dublin3, 'Dublin3'),
        (Dublin4, 'Dublin4'),
        (Dublin5, 'Dublin5'),
        (Dublin6, 'Dublin6'),
        (Dublin7, 'Dublin7'),
        (Dublin8, 'Dublin8'),
        (Dublin9, 'Dublin9'),
        (Dublin10, 'Dublin10'),
        (Dublin11, 'Dublin11'),
        (Dublin12, 'Dublin12'),
        (Dublin13, 'Dublin13'),
        (Dublin14, 'Dublin14'),
        (Dublin15, 'Dublin15'),
        (Dublin16, 'Dublin16'),
        (Dublin17, 'Dublin17'),
        (Dublin18, 'Dublin18'),
        (Dublin20, 'Dublin20'),
        (Dublin22, 'Dublin22'),
        (Dublin24, 'Dublin24'),
      
    )
    Area = models.CharField(choices=AREAS, max_length=3, default='Dublin1')
    
    Lesson_Price_For_12 = models.DecimalField(max_digits=6, decimal_places=0, default=0)
    Lesson_Price_For_1 = models.DecimalField(max_digits=6, decimal_places=0, default=0)
    
    def __str__(self):
        return self.school_name


