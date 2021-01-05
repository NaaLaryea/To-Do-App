from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# 
STATUS =(
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed'),
)

PRIORITY =(
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
)


class Todo(models.Model):
    user= models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=50)
    task_desc = models.CharField(max_length=254)
    status = models.CharField(max_length=50, choices=STATUS)
    priority = models.CharField(max_length=10, choices=PRIORITY)
    due_date = models.DateField()
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.task_name) + " " + str(self.due_date)
