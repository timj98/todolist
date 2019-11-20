from django.db import models

class Todo(models.Model):
    content = models.TextField()
    completed = models.BooleanField()
    created = models.DateTimeField()
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        """
        the string for the model
        :return: shorted content to make it easier to read
        """
        return self.content[:10]

