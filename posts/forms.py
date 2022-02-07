from django import forms
from .models import Posts,Category
class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    cateogry = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class':'form-control'}),
        queryset=Category.objects.all()
    )
    class Meta:
        model = Posts
        fields = '__all__'
