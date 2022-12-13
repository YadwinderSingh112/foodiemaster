from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


# class CustomRole(models.Model):
    # role = models.CharField(max_length=25)
class CustomUser(AbstractUser):
    # userrole = models.ForeignKey(CustomRole, on_delete=models.CASCADE)
    is_reader = models.BooleanField(default= False)
    is_author = models.BooleanField(default= False)
    about_me = models.CharField(max_length=200)
class Author(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
class Reader(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=5, unique=True)
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children' ,on_delete= models.DO_NOTHING)

    class Meta:
        #enforcing that there can not be two categories under a parent with same slug
        
        # __str__ method elaborated later in post.  use __unicode__ in place of
        
        # __str__ if you are using python 2

        unique_together = ('slug', 'parent',)    
        verbose_name_plural = "categories"     

    def __str__(self):                           
        full_path = [self.name]                  
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1]) 
    
class Post(models.Model):
    image = models.ImageField(upload_to='pics', blank= True, null=True, default= False)
    title = models.CharField(max_length=200, unique=True)
    small_description = models.CharField(max_length=255)
    slug = models.SlugField(null= False , unique=True)
    category = models.ForeignKey('Category', null=True, blank=False ,on_delete= models.DO_NOTHING)
    author = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    updated_on = models.DateTimeField(auto_now= True)
    content = RichTextUploadingField()
    created_on = models.DateTimeField(auto_now_add=True)
    likee = models.ManyToManyField(CustomUser, related_name= "blog_posts")

    def total_likes(self):
        return self.likee.count()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
          
    # html = RichTextField()  
        #status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_cat_list(self):
        k = self.category # for now ignore this instance method
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent
        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]

    def get_absolute_url(self):
        return reverse("index")

class Comment(models.Model):
        post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
        user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
        body = models.TextField()
        created_on = models.DateTimeField(auto_now_add=True)
        # active = models.BooleanField(default=False)

        def __str__(self):
            return '%s - %s' % (self.post.title, self.user)
        @property
        def number_of_comments(self):
            return Comment.objects.filter(post=self).count()
             