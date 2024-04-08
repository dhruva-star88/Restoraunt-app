from django.db import models
from django.contrib.auth.models import User

MEAL_TYPE = (
    ("starters", "Starters"),
    ("salads", "Salads"),
    ("main_dishes", "Main Dish"),
    ("desserts", "Desserts")
)

STATUS = (
    (0, "Unavailable"),
    (1, "Available")
)

class item(models.Model):
    meal = models.CharField(max_length=255)
    description = models.CharField(max_length=1200)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    meal_type = models.CharField(max_length=120 ,choices=MEAL_TYPE)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS, default=1)
    # Records time when item is created
    date_created = models.DateTimeField(auto_now_add=True)
    # Records time when same item is edited or updated
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meal