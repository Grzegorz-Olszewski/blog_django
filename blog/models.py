from django.db import models
from django.urls import reverse


class Post(models.Model):
    ''' Class representing Post model object. It defines how post are
    going to be represented in database.
    '''
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("blog:details_post", kwargs={"pk": self.pk})
