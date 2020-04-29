from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    Dolar = 'USD'
    Euro = 'EUR'
    Pound = 'GBP'
    Kurlar = [
        (Dolar, 'Dolar'),
        (Euro, 'Euro'),
        (Pound, 'Pound'),
    ]
    content = models.CharField(
        max_length=5,
        choices=Kurlar,
        default=Dolar,    
    )
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.author

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

