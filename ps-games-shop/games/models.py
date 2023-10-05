from django.db import models



class Category(models.Model):

    name = models.CharField(max_length=60 , unique=True)

    def __str__(self):
        return f"{self.name}"
    
class Creator(models.Model):

    name = models.CharField(max_length=60 , unique=True)

    def __str__(self):
        return f"{self.name}"
    

class Games(models.Model):

    PS5 = "5"
    PS4 = "4"
    PS3 = "3"
    PS2 = "2"

    CONSOL_TYPE = [
        (PS5, "Play Station 5"),
        (PS4, "Play Station 4"),
        (PS3, "Play Station 3"),
        (PS2, "Play Station 2"),

    ]

    title=models.CharField(max_length=70)
    image=models.ImageField(upload_to='media/games')
    summary=models.TextField()
    console=models.CharField(
        max_length=1, choices=CONSOL_TYPE, default=PS5
    )
    release_time=models.DateField()
    price=models.DecimalField(max_digits=8,decimal_places=3)
    players=models.CharField(max_length=10)
    is_online=models.BooleanField(default=False)
    category=models.ForeignKey(Category,on_delete=models.PROTECT)
    creator=models.ForeignKey(Creator,on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.title}"