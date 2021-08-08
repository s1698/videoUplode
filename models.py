from django.db import models

# Create your models here.
class Vedio(models.Model):
    caption=models.CharField(max_length=100)
    vedio=models.FileField(upload_to="vedio/%y")
    def __str__(self):
        return self.caption
        return self.vedio
        
