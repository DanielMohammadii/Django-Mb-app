from django.db import models

# Create your models here.

class Post(models.Model):
    text = models.TextField()
     

    def __str__(self):
        return self.text[:30]

    # def get_absolute_url(self):
    #     return reverse("Post_detail", kwargs={"pk": self.pk})
