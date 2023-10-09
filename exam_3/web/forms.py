from django import forms
from django.db import models
from web.models import Profile, Car


class ProfileBaseForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
    )

    class Meta:
        model = Profile
        exclude = ('first_name', 'last_name', 'profile_picture',)


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set__hidden_fields()

    def save(self, commit=True):
        if commit:
            Car.objects.all().delete()
            return self.instance.delete()

        return self.instance

    def set__hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()


class ProfileEditForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class CarCreateForm(CarBaseForm):
    pass


class CarDetailsForm(CarBaseForm):
    pass


class CarEditForm(CarBaseForm):
    pass


class CarDeleteForm(CarBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disabled_fields()

    def save(self, commit=True):
        if commit:
            return self.instance.delete()
        return self.instance

    def __disabled_fields(self):
        for _, field in self.fields.items():
            if field == 'car_type':
                field.widget.attrs['disabled'] = 'disabled'
                continue
            field.widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = Car
        fields = '__all__'






