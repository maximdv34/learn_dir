from django.db import models


class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.CharField(max_length=10000)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text[:50] + "..."
