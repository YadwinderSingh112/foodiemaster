from django.forms import  *
from account.models import Post
from ckeditor.widgets import CKEditorWidget
class PostForm(ModelForm):
    # content = CharField(widget = CKEditorWidget())
    class Meta:
        model = Post
        exclude = ('author','slug')
        fields = '__all__' 
        widgets = {
                    'content': CKEditorWidget(),
                    'title': TextInput(attrs={'class': 'form-control m-2'}),
                    'small_description': TextInput(attrs={'class': 'form-control m-2'}),
                    'category': Select( attrs={'class': 'form-control m-2'}),
                }