from django.db import models

# Create your models here.
class Product(models.Model):
    choix = [
        ('phone','Phone'),
        ('laptop','Laptop'),
        ('tablet','Tablet'),
        ('accessories','Accessories'),
    ]


    name = models.CharField(max_length=50,default='name', verbose_name='Title')
    content = models.TextField(null=True, blank=True, verbose_name='Description')
    price = models.DecimalField(max_digits=5, decimal_places=2,default=10.00)
    image = models.ImageField(upload_to='photos/%y/%m/%d', default='photos/25/06/27', verbose_name='Photo')
    active = models.BooleanField(default=True,verbose_name='Is True')
    category = models.CharField(max_length=50,null=True, blank=True,choices=choix)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Phone'
        ordering = ['-price']