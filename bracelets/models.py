from random import choice
from django.db import models
from django.utils.html import escape
from django.utils.safestring import mark_safe


class Item(models.Model):
    BRACELET = 'br'
    EARING = 'er'
    OTHER = 'ot'
    TYPE_CHOICES = [
        (BRACELET, 'bracelet'),
        (EARING, 'earing'),
        (OTHER, 'other')
    ]
    title = models.CharField(max_length=200, null=True)
    item_type = models.CharField(max_length=2, choices=TYPE_CHOICES, default=OTHER)
    description = models.TextField(max_length=200, null=True, blank=True)
    price = models.FloatField(default=0.0)
    available = models.IntegerField(default=1)

    @property
    def image_preview(self):
        
        string = ""
        if self.images:
            for represent in self.images.all():
                string += f'''
                        <img 
                        src="{represent.image.url}" 
                        style="
                        width: 300px;
                        height: auto;
                        padding: 10px;
                        margin: 10px;"
                        />
                        '''
            return mark_safe(string)
        return ''
    
    def __str__(self):
        return self.title


class ItemImage(models.Model):
    item = models.ForeignKey(Item, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='bracelets',null=True)

    def __str__(self):
        return f'bracelet for {self.item}'
