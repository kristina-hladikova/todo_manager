from django.contrib.auth.models import User
from django.db import models


def user_directory_path(todo, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(todo.user.id, filename)


class Todo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    due_date = models.DateField()
    status_done = models.BooleanField(null=True, default=False)
    attachment = models.FileField(upload_to=user_directory_path, blank=True, null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
