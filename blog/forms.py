from django import forms

class AddCommentForm(forms.Form):
  description = forms.TextArea()
  blogtitle = forms.CharField()