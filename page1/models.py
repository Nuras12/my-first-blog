from django.db import models
class First1(models.Model):
    src = models.CharField(max_length=20, help_text="path of file")
    text = models.TextField(max_length=9000)
    def __str__(self):
        return self.src
