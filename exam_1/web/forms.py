from django import forms

from web.models import Profile, Album


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfileForm(ProfileBaseForm):
    pass


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name',
                },

            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist'
                },
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                },
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Image URL',
                },
            ),
            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Price'
                },
            ),
        }


class CreateAlbumForm(AlbumBaseForm):
    pass


class EditAlbumForm(AlbumBaseForm):
    pass


class DeleteAlbumForm(AlbumBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set__disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def set__disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'


class DeleteProfileForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set__hidden_fields()

    def save(self, commit=True):
        if commit:
            Album.objects.all().delete()
            self.instance.delete()

        return self.instance

    def set__hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()



