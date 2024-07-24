from django.db import models

class firstRow(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="firstRow")
    text = models.TextField(null=True, blank=True)

    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ("firstRow")
        verbose_name_plural = ("İlk satırdaki resimler")

# Create your models here.
