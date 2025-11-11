from django.db import models

from django.db import models

class Drink(models.Model):

    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    ]

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    size = models.CharField(max_length=1, choices=SIZE_CHOICES, default='M')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    caffeine_mg = models.PositiveIntegerField(null=True, blank=True)

    slug = models.SlugField(max_length=120, unique=True, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse('drinks_counter:drink_display', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.get_size_display()} {self.name}"

    class Meta:
        ordering = ['name']
        verbose_name = 'Drink'
        verbose_name_plural = 'Drinks'
