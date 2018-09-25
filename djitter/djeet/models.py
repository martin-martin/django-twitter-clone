from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Djeet(models.Model):
    user = models.ForeignKey(User,
                             related_name='djeets',
                             on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    # this allows us to display the djeets in order of newest post first
    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return "{0} at {1}: {2}...".format(self.user,
                                           self.created_at,
                                           self.body[:20])
