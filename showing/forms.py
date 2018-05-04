from django import forms
from .models import List_of_regedit_buy

class SearchForm(forms.Form):
    START_YEAR_CHOICES = (
        ('2013', ''),
        ('2013', '2013'),
        ('2014', '2014'),
        ('2015', '2015'),
        ('2016', '2016'),
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021'),
        ('2022', '2022'),
        ('2023', '2023'),
        ('2024', '2024')
        )
    CHECKBOX_INPUT_CHOICES = (
        ('ПО', 'ПО'),
        ('ПНР и ШМР', 'ПНР и ШМР'),
        ('СХД', 'СХД'),
        ('server', 'Серверное оборудование'),
        ('network', 'Сетевое оборудование'),
        ('support', 'Техническая поддержка'),
        ('ibp', 'ИБП'),
        ('consulting', 'Консалтинг')
        )
    END_YEAR_CHOICES = (
        ('2025', ''),
        )
    q = forms.CharField(
            widget=forms.TextInput(
                    attrs={'size' : 30,
                    'id' : 'typeahead',
                    'placeholder' : 'Введите название',
                    'autocomplete' : 'off',
                    }),
            required=False,
            label='Наименование компании')
    checkbox_input = forms.MultipleChoiceField(
        choices=CHECKBOX_INPUT_CHOICES,
        widget=forms.CheckboxSelectMultiple(),
        required=True,
        )
    start_year = forms.ChoiceField(
        choices=START_YEAR_CHOICES,
        widget=forms.Select(attrs={"onChange":"Add_option_to_select();"})
        )
    end_year = forms.ChoiceField(
        choices=END_YEAR_CHOICES,
        )

   
class ModelForm(forms.ModelForm):
    data = forms.ModelChoiceField(
                queryset=List_of_regedit_buy.objects.all(),
                widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = List_of_regedit_buy
        fields = ['data']
