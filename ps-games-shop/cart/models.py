from django.db import models
from games.models import Games


class Cart(models.Model):

    ACCEPT = "a"
    REFUSE = "r"
    WAITING = "w"
    
    STATUS_CHOICES = [
    (ACCEPT, 'Accept'),
    (REFUSE, 'Refuse'),
    (WAITING, 'Waiting'),
    ]

    total_price = models.DecimalField(max_digits=6,decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)
    total_quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=WAITING)

    def __str__(self):
        return f"{self.total_quantity} order "
    

    
class OrderItem(models.Model):

    games = models.ForeignKey(Games, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6,decimal_places=2)