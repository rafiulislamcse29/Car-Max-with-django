from django.db import models
from cars.models import Car
from django.contrib.auth.models import User

# Create your models here
class Order(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  car=models.ForeignKey(Car,on_delete=models.CASCADE)
  ordered_at=models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:
    return f'order {self.id} by {self.user}'

