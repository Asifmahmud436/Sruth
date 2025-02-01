from django.db import models

class Ai(models.Model):
    question = models.TextField(blank=True,null=True)
    answer = models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.question[:50]
