from django.db import models

# Create your models here.

class New_Model(models.Model):
    Word = models.CharField(max_length = 255)
    def __str__(self):
        return self.Word

    Content = models.TextField(max_length = 70000)
    def __str__(self):
        return self.Content

class New_Feedback(models.Model):
    Feedback1 = models.CharField(max_length = 255)
    def __str__(self):
        return self.Feedback1