from django import forms
from common.models import PhotoComment, PhotoLike
from core.model_mixins import DisabledFormMixin

from photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('publication_date',)


class PhotoCreateForm(PhotoBaseForm):
    pass

class PhotoEditForm(PhotoBaseForm):
    class Meta:
        model = Photo
        exclude = ('publication_date', 'photo',)

class PhotoDeleteForm(DisabledFormMixin, PhotoBaseForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            self.instance.tagged_pets.clear()
            PhotoLike.objects.filter(photo_id=self.instance.id).delete()
            PhotoComment.objects.filter(photo_id=self.instance.id).delete()
            self.instance.delete()
        
        return self.instance
    
    def clean_tagged_pets(self):
        tagged_pets = self.cleaned_data['tagged_pets']
        if tagged_pets:
            raise forms.ValidationError('Pet are tagged in this photo!')
        