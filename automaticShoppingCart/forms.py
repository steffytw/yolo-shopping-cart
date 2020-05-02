from django import forms

class registerForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(widget=forms.EmailInput)
    mobile_number = forms.CharField(widget=forms.NumberInput)
    password = forms.CharField(widget =forms.PasswordInput)
    confirm_Password = forms.CharField(widget = forms.PasswordInput)
    def clean_username(self):
        value = self.cleaned_data['username']
        if value.isupper():
            raise forms.ValidationError("please dont use uppercase")
        return value
    
    def clean_confirm_Password(self):
       password = self.cleaned_data['password']
       confirm_Password = self.cleaned_data['confirm_Password']
       if not password == confirm_Password:
            raise forms.ValidationError("Password and Confirm Password not match")
       return password

class productForm(forms.Form):
    serialNo = forms.CharField(widget=forms.NumberInput)
    product =  forms.CharField()
    product_details =  forms.CharField()
    price = forms.CharField()
    quantity = forms.CharField(widget=forms.NumberInput)
    subtotal = forms.CharField()