from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    # display the item name instead of 'item object x' in the admin page
    def __str__(self):
        return self.name

