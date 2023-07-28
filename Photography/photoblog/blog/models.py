from django.db import models

# ContactSubmission representing database table
class ContactSubmission(models.Model):
    # Each attribute of model class = Fields of the database table 
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    