from django.db import models

RATE_CHOICES = (
    (1, "*"),
    (2, "**"),
    (3, "***"),
    (4, "****"),
    (5, "*****"),
)


class Product(models.Model):
    price = models.FloatField()
    title = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)
    rating = models.IntegerField(choices=RATE_CHOICES, default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
