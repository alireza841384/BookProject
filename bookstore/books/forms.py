from django import forms


class BookForm(forms.Form):
    BookName = forms.CharField(max_length=50)
    Chocies = {"Derama": "Derama", "Action'": 'Action',
               "SienceFiction": 'SienceFiction', "Sience": 'Sience', "Story": "Story"}
    Title = forms.ChoiceField(choices=Chocies)
    Author = forms.CharField(max_length=40)
