from django.db import models

class Search(models.Model):
    text = models.TextField(max_length =5000)
    
    def __str__(self):
       return self.text
       

class Find(models.Model):
     words = models.CharField(max_length=50)
     location = models.ManyToManyField(Search, blank=True)
     
     def __str__(self):
       return self.words



