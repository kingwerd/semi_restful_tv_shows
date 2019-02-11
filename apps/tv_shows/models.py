from django.db import models

class ShowManager(models.Manager):
    def validator(self, post_data):
        errors = {}

        if len(post_data['title']) < 5:
            errors['title'] = "Show name should at least 5 characters"
        if len(post_data['network']) < 1:
            errors['network'] = "Show network should be more than 1 character"
        if len(post_data['description']) < 10:
            errors['description'] = "Show description should be more than 10 characters long"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=100)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
