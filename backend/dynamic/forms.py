from django import forms
class TeamMaking(forms.Form):
    name = forms.CharField(max_length= 30)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def __init__ (self, *args, **kwargs):
        extra = kwargs.pop('extra')
        super(TeamMaking,self).__init__(*args,**kwargs)

        for i in enumerate(extra):
            self.fields['name_%s' % i] = forms.CharField(label="Member Name")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError("The two password fields didn't match.")
        return password2

    def extra_name(self):
        for name,value in self.cleaned_data.items():
            if name.startswith('name_'):
                yield (value)