from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete='models.CASCADE')
    website = models.URLField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True)
    your_cv = models.FileField(blank=True, upload_to='uploads/pdf')

    def __str__(self):
        return self.user.username

class Category(models.Model):
    cat_name = models.CharField(verbose_name='Category Name', max_length=100)
    cat_desc = models.TextField(blank=True)

    def __str__(self):
        return self.cat_name

class Post(models.Model):
    post_title = models.CharField(verbose_name='Post Tile', max_length=120)
    category = models.ManyToManyField(Category, verbose_name='Category')
    post_img = models.ImageField(blank=True, null=True, upload_to='uploads/post_image')
    author = models.ForeignKey(User, on_delete='models.CASCADE')
    create_date = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    def __str__(self):
        return self.post_title

class ContactModel(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    GENDER_FIELD = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    FACEBOOK = 'facebook'
    INSTAGRAM = 'instagram'
    NAIRALAND = 'nairaland'
    TWITTER = 'twitter'
    CHOOSE = ''
    REFERER_FIELD = [
        (FACEBOOK, 'Faceboo'),
        (INSTAGRAM, 'Instagram'),
        (NAIRALAND, 'Nairaland'),
        (TWITTER, 'Twitter'),
        (CHOOSE, 'Please Choose'),
    ]

    name = models.CharField(verbose_name='Full name', max_length=100)
    phone = models.CharField(verbose_name='Your Phone', max_length=11)
    subject = models.CharField(verbose_name='Subject', max_length=20, null=True)
    email = models.EmailField(verbose_name='Company Email')
    referer = models.CharField(choices=REFERER_FIELD, default=CHOOSE, blank=True, max_length=10)
    gender = models.CharField(choices=GENDER_FIELD, default=MALE, max_length=7)
    image = models.ImageField(blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.name
     