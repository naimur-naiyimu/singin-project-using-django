# from django.db import models

# # Create your models here.


# class User(models.Model):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     pass1 = models.CharField(max_length=100)
#     pass1 = models.CharField(max_length=100)
#     profile_picture = models.ImageField(upload_to='profile_pictures/')

#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name',
#                        'profile_picture', 'username']

#     def __str__(self):
#         return self.email


# class Patient(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     address_line1 = models.CharField(max_length=255)
#     city = models.CharField(max_length=255)
#     state = models.CharField(max_length=255)
#     pincode = models.CharField(max_length=6)

#     def __str__(self):
#         return self.user.email
