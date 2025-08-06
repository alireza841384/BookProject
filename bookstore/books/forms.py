from django import forms


class BookForm(forms.Form):
    BookName = forms.CharField(max_length=50)
    Chocies = {"c1": "Derama", "c2": 'Action',
               "c3": 'SienceFiction', "c4": 'Sience', "c5": "Story"}
    Title = forms.ChoiceField(choices=Chocies)
    Author = forms.CharField(max_length=40)
