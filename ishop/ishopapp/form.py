from django.forms import ModelForm
#from django import

from ishopapp.models import Item

class ItemForm(ModelForm):
     class Meta:
         model = Item
         fields = ['Name', 'Price', 'Description', 'Type', 'TradingLocation']

#class UserForm(ModelForm):
 #   class Meta:
  #      model = User
   #     fields = ['Name', 'Sex', 'DOB', 'ContactNo']


