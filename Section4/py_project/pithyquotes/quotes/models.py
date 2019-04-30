from django.db import models

# Create your models here.

class Quote(models.Model):
    quote = models.CharField(max_length=250, help_text="Famous quote")
    attribute = models.CharField(max_length=50, help_text="Who said that?")
    
    def __str__(self):
        return self.quote
    
    class Meta:
        ordering = ['quote']
