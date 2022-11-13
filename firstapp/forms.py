from django import forms
from .models import FirstModel

# very much look a like ModelAdmin and ModelAdmin Use ModelForm in behind
class firstappModelForm(forms.ModelForm):
    class Meta:
        model = FirstModel
        fields = ["title", "content"] # it will only render those fields which are in "Meta -> fields" and same as Type define in Model
        # only those Model fild we can skip in which we have set "NotNull = False" Because default "NotNull" is True
    #optional
    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = FirstModel.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error("title", f"{title} is already exists")
        return data

class firstappForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # To Check The data is valid or Clean form data
    # def clean_title(self):
    #     # clean() or clean_fildName() only this name will overwrite function
    #     # it will only clean "Title" data
    #     cleaned_data = self.cleaned_data # Dictionary :
    #     title = cleaned_data.get('title')
    #     return title

    def clean(self):
        # it will clean data life removing extra blank space and also many more
        cleaned_data = self.cleaned_data
        db_title = FirstModel.objects.values_list("title", flat=True)
        # Mainly we are going to use Clean method for this type o f validation's
        if cleaned_data.get('title') in db_title:
            self.add_error('title', 'This Title is taken') # this will not allow to validate data in view function
            # raise forms.ValidationError("This Title is taken") # this is non Fild error because not specified for witch fild this error is
        print("all data", cleaned_data)
        return cleaned_data

        # errorlist : error for any specific fild then we have to use this
        # errorlist NonFild : spesify this when error need's to be  General error