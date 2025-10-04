from django.db import models
from django.contrib.auth.models import User

class Petition(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def vote_count(self):
        return self.votes.count()

    def __str__(self):
        return self.title

class Vote(models.Model):
    petition = models.ForeignKey(Petition, related_name="votes", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("petition", "user")