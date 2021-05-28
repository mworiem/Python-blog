from django.db import models

# Create your models here.
class Project(models.Model): #class of a model = a table
    title = models.CharField(max_length=100)
    description = models.TextField()#long str no max limit
    technology = models.CharField(max_length=20)#short strings - has max str
    image = models.FilePathField(path="/img")
    
    def __str__(self):
        return self.title