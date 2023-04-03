from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self) -> str:
        return str(self.name)


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, default=None, blank=True)
    status = models.BooleanField(default=False)
    tag = models.ManyToManyField(to=Tag, related_name="tasks")

    class Meta:
        ordering = ["-status"]

    def __str__(self) -> str:
        return str(self.content)
