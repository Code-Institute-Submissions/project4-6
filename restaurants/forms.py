from django import forms
from .models import Restaurant, Cuisine, Location
from .widgets import CustomClearableFileInput


class RestaurantForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = '__all__'

    image = forms.ImageField(
        label='', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cuisines = Cuisine.objects.all()
        print(cuisines)
        cuisine_names = [(c.id, c.get_name()) for c in cuisines]
        locations = Location.objects.all()
        location_names = [(c.id, c.get_name()) for c in locations]

        self.fields['cuisine'].choices = cuisine_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

        self.fields['location'].choices = location_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
