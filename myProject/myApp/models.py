from django.db import models
from django.contrib.auth.models import AbstractUser


class customUSer(AbstractUser):
    USER=[
        ('admin','Admin'),
        ('user','User'),
    ]
    
    city=models.CharField(max_length=10)
    profile_pic=models.ImageField(upload_to='Media/pro_pic')
    user_type=models.CharField(choices=USER,max_length=100)
    
    class Meta:
        ordering=["last_name","first_name"]
        verbose_name="Custom User"
        db_table="to_do_list_table"
        unique_together = ["username","email"]
    
class categoryModel(models.Model):
    user=models.ForeignKey(customUSer,on_delete=models.CASCADE)
    categoryName=models.CharField(max_length=20,null=True)
    created_at=models.DateField(auto_now_add=True,null=True)
    update_at=models.DateField(auto_now=True,null=True)
    
    def __str__(self):
        return self.categoryName
    
class TaskModel(models.Model):
    PRIORITY=[
        ('high','High'),
        ('medium','Medium'),
        ('low','Low'),
    ]
    categoryName=models.ForeignKey(categoryModel,on_delete=models.CASCADE)
    priority=models.CharField(choices=PRIORITY,max_length=20,null=True)
    taskName=models.CharField(max_length=20,null=True)
    description=models.TextField(max_length=100,null=True)
    due_date=models.DateField(null=True)
    status=models.CharField(max_length=100,default="On_Going",null=True)
    completed_date=models.DateField(null=True)
    created_at=models.DateField(auto_now_add=True,null=True)
    update_at=models.DateField(auto_now=True,null=True)
    
    class Meta:
        unique_together = ["categoryName","taskName"]