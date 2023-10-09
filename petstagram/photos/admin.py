from django.contrib import admin

from photos.models import Photo

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'publication_date',
        'description',
        'get_tagged_pets'
    )

    @staticmethod
    def get_tagged_pets(obj):
        tagged_pets = obj.tagged_pets.all()
        if tagged_pets:
            return ', '.join(x.name for x in obj.tagged_pets.all())
        return 'No tagged pets'
    