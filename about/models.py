from django.db import models

# contact model.
class Contact(models.Model):
    name =  models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    class Meta:
        db_table = "contact"
    