from django import forms

from web.models import Profile, Fruit


class ProfileBaseForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput
    )

    class Meta:
        model = Profile
        exclude = ('image_url', 'age',)


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('password', 'email',)

        labels = {
            'image_url': 'Image URL',
        }


class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_hidden_fields()

    def save(self, commit=True):
        if commit:
            Fruit.objects.all().delete()
            self.instance.delete()

        return self.instance

    def set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'

        labels = {
            'name': '',
            'image_url': '',
            'description': '',
            'nutrition': '',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Full Name',
                }
            ),
            'image_url': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Image URL',
                }

            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Fruit description',
                },
            ),
            'nutrition': forms.Textarea(
                attrs={
                    'placeholder': 'Nutrition Info',
                }
            )
        }


class FruitCreateForm(FruitBaseForm):
    pass


class FruitEditForm(FruitBaseForm):
    class Meta:
        model = Fruit
        fields = '__all__'

        labels = {
            'name': 'Name',
            'image_url': 'Image URL',
            'description': 'Description',
            'nutrition': 'Nutrition',
        }


class FruitDeleteForm(FruitEditForm):
    def save(self, commit=True):
        if commit:
            return self.instance.delete()
        return self.instance

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = Fruit
        exclude = ('nutrition',)

        labels = {
            'name': 'Name',
            'image_url': 'Image URL',
            'description': 'Description',
        }
