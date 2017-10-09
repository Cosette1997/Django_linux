from django import forms 
from mysite import models
#from captcha.fields import CaptchaField

class ContactForm(forms.Form):
    CITY = [
     ['TP', 'Taipei'],
     ['TY', 'Taoyuan'],
     ['TC', 'Taichung'],
     ['TN', 'Tainan'],
     ['KS', 'Kaohsiung'],
     ['NA', 'Others'],
    ]
    user_name = forms.CharField(label='Your name', max_length=50, initial='Eva')
    user_city = forms.ChoiceField(label='City', choices=CITY)
    user_school = forms.BooleanField(label='Learning?', required=False)
    user_email = forms.EmailField(label='Email')
    user_message = forms.CharField(label='Your opinion', widget=forms.Textarea)

class PostForm(forms.ModelForm):
   # captcha = CaptchaField()
    class Meta:
        model = models.Post
        fields = ['mood', 'nickname', 'message', 'del_pass']
      
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['mood'].label = 'Mood:'
        self.fields['nickname'].label = 'Your Nickname:'
        self.fields['message'].label = 'Post for mood:'
        self.fields['del_pass'].label = 'Set password:'
        #self.fields['captcha'].label = "Make sure you're not a robot"
        
class LoginForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=10)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

class DateInput(forms.DateInput):
    input_type = 'date'


class DiaryForm(forms.ModelForm):
    class Meta:
        model = models.Diary
        fields = ['budget', 'weight', 'note', 'ddate']
        widgets = {
            'ddate': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super(DiaryForm, self).__init__(*args, **kwargs)
        self.fields['budget'].label = "Today's spending"
        self.fields['weight'].label = "Today's weight"
        self.fields['note'].label = "Mood Post"
        self.fields['ddate'].label = "Date"
