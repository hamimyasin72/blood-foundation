from django.db import models



class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    summary = models.TextField(max_length=500)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title
 
class Member(models.Model):
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    hospital = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} ({self.hospital})"




class CarouselSlide(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    subtitle = models.CharField(max_length=300, blank=True, null=True)
    image = models.ImageField(upload_to="carousel/")  # upload folder
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title or " "
    
    
class NewsTicker(models.Model):
    message = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message



class RareBloodDonor(models.Model):
    BLOOD_GROUP_CHOICES = [
        ('A-', 'A−'),
        ('B-', 'B−'),
        ('AB-', 'AB−'),
        ('O-', 'O−'),
        ('A2B-', 'A2B−'),
        ('Bombay', 'Bombay (hh)'),
        ('Rhnull', 'Rh null'),
        ('Other', 'Other (specify below)'),
    ]

    name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=20, choices=BLOOD_GROUP_CHOICES)
    custom_blood_type = models.CharField(
        max_length=50, blank=True, null=True, help_text="If not listed above"
    )
    age = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(
        max_length=10,
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
        blank=True,
        null=True,
    )
    phone = models.CharField(max_length=20, help_text="Include country code if possible")
    email = models.EmailField(blank=True, null=True)
    location = models.CharField(max_length=150, help_text="City / Hospital / Area")
    availability = models.BooleanField(default=True, help_text="Available for donation?")
    last_donated = models.DateField(blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.blood_group})"

    class Meta:
        verbose_name = "Rare Blood Donor"
        verbose_name_plural = "Rare Blood Directory"
        ordering = ['blood_group', 'name']


































 

class DonationRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled')
    ]

    patient_name = models.CharField(max_length=100)
    required_blood_group = models.CharField(max_length=3, choices=Donor.BLOOD_GROUPS)
    units_needed = models.PositiveIntegerField()
    hospital_name = models.CharField(max_length=200)
    request_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    fulfilled_by = models.ForeignKey(Donor, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Request for {self.required_blood_group} ({self.units_needed} units)"

