from django.contrib import admin
from .models import Item, ItemImage


class ItemImageInLine(admin.TabularInline):
    model = ItemImage
    extra = 1


class ItemAdmin(admin.ModelAdmin):
    inlines = [
        ItemImageInLine,
    ]
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        return obj.image_preview
    
    image_preview.short_description = 'Image Preview'
    image_preview.allow_tags = True
    
    class Meta:
        model = Item

admin.site.register(Item, ItemAdmin)

