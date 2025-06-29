from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


# One To One Relationship
# class Female(models.Model):
#     Female_name = models.CharField(max_length=100, null=True)
#     def __str__(self):
#         return self.Female_name

# class Male(models.Model):
#     Male_name = models.CharField(max_length=100, null=True)
#     girl = models.OneToOneField(Female, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.Male_name
    

# # Many To One Relationship
# class Product(models.Model):
#     title = models.CharField(max_length=100, null=True)
#     def __str__(self):
#         return self.title
    
# class User(models.Model):
#     name = models.CharField(max_length=100, null=True)
#     products = models.ForeignKey(Product, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.name
    
# # Many To Many Relationship
# class Video(models.Model):
#     title = models.CharField(max_length=100, null=True)
#     def __str__(self):
#         return self.title
    
# class SimpleUser(models.Model):
#     name = models.CharField(max_length=100, null=True)
#     watch = models.ManyToManyField(Video, null=True)
#     def __str__(self):
#         return self.name
