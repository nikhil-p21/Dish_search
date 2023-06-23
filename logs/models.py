from django.db import models
#creating a model for the database
class restaurant(models.Model):
    #restaurant name
    name = models.CharField('name',max_length=255)
    #restaurant location
    location = models.CharField('location',max_length=255)
    #restaurant menu
    items = models.TextField('items')

    def __str__(self):
        return self.name
