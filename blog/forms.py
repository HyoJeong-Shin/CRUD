from django import forms
from .models import Post

class PostForm(forms.ModelForm):    #ModelForm

    class Meta:

        model = Post    #model에 정의된 class Post에서
        fields = ['title','author','content']   #사용자로부터 여기에 적어준 field 데이터를 직접 입력받는다.