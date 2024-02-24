from django.db import models

# Create your models here.
class Student_Data(models.Model):
    stu_name=models.CharField(max_length=20)
    stu_age=models.IntegerField()
    stu_dob=models.DateTimeField()
    stu_mob=models.BigIntegerField()
    stu_subject=models.CharField(max_length=20)
    stu_marks=models.IntegerField()
    stu_rank=models.IntegerField()
    stu_collage=models.CharField(max_length=20)
    stu_addmisson_date=models.DateField()

    class Meta:
        verbose_name="STUDENT DATA"