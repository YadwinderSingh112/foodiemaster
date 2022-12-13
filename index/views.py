from django.shortcuts import HttpResponse, HttpResponseRedirect, get_object_or_404, render, redirect
from account.models import *
from django.views.generic import *
from .forms import *
# Create your views here.

def index(request):
        objs = Post.objects.all().order_by('-created_on')
        CAT1 = Post.objects.filter(category__name = "Desserts").order_by('-created_on')
        CAT2 = Post.objects.filter(category__name = "Recipes").order_by('-created_on')
        CAT3 = Post.objects.filter(category__name = "Vegan").order_by('-created_on')
        CAT4 = Post.objects.filter(category__name = "Dinner").order_by('-created_on')
        categories = Category.objects.all()
        def get_context_data(self, **kwargs):
            context = super(index, self).get_context_data(**kwargs)
            context["categories"] = categories
            return context
        
        list = {
                'categories': categories,
                'objs': objs,
                'CAT1': CAT1,
                'CAT2': CAT2,
                'CAT3': CAT3,
                'CAT4': CAT4
        
        }
        return render(request, 'index.html', list)
        
def likeView(request, slug):
        post = get_object_or_404(Post, slug = request.POST.get('post_slug'))
        if post.likee.filter(id = request.user.id).exists():
                post.likee.remove(request.user)
                liked = False
        else:
                post.likee.add(request.user)
                liked = True
        return HttpResponseRedirect(reverse('article_detail', args=[str(slug)]))

class UpdatePost(UpdateView):
        model = Post
        fields = ['image','title', 'body']
        form_class = PostForm
        template_name = 'Edit.html'

def Add_PostView(request):
        if request.method == 'POST':
                form = PostForm(request.POST, request.FILES)
                #print(form.data)
                # initial= {
                #         "author": request.user,
                #         "title":request.POST["title"],
                #         "content":request.POST["content"],
                # }
                # form['author'] = Post.objects.get(pk = request.user.id)
                if form.is_valid():
                        ab = form.save(commit = False)
                        ab.author = request.user
                        ab.save()
                        return redirect('index')
        else:
            form = PostForm()
            return render(request, 'add_post.html', {'form': form})
def category_grid(request,categ=None):
        if categ:
                print(categ)
                objs = Post.objects.filter(category__name = categ).order_by('-created_on')
        else:
                objs = Post.objects.all().order_by('-created_on')
        return render(request, 'categories-grid.html', {'objs': objs, 'categ': categ})

def category_list(request, categ = None):
        if categ:
                objs = Post.objects.filter(category__name = categ).order_by('-created_on')
        else:
                objs = Post.objects.all().order_by('-created_on')
        return render(request, 'categories-list.html', {'objs': objs,'categ': categ, 'list':list})

class category_single(DetailView):
        model = Post
        template_name = 'single-post.html'

        def slugg (request, slug):
                post = Post.objects.get(slug=slug)
                return render(request,'single-post.html', {'obj': post })
        
        def get_context_data(self, **kwargs):
                comments_connected = Comment.objects.filter(post=self.get_object()).order_by('-created_on')
                context = super(category_single, self).get_context_data(**kwargs)
                stuff = get_object_or_404(Post, slug = self.kwargs['slug'])
                total_likes = stuff.total_likes()
                liked = False
                if stuff.likee.filter(id = self.request.user.id).exists():
                        liked = True
                context["total_likes"] = total_likes
                context['comments'] = comments_connected
                if self.request.user.is_authenticated:
                        context['comment_form'] = CommentForm(instance=self.request.user)
                context['post_liked'] =  liked
                return context
        def post(self, request, *args, **kwargs):
                new_comment = Comment(body=request.POST.get('body'),
                                  user=self.request.user,
                                  post=self.get_object())
                new_comment.save()
                return self.get(self, request, *args, **kwargs)
        # def form_valid(self, comment_form):
        #         comment_form.instance.user = self.request.user 
        #         comment_form.instance.post_id = self.kwargs['slug']
        #         return super().form_valid(comment_form)
def about(request):
        return render(request, 'about.html')

def contact(request):
        return render(request, 'contact.html')

# def AuthorView(request):
        #         objs = Post.objects.all()
        #         return render(request, 'author_chamber.html', { 'objs': objs } ) 
        #         # model = Post
        #         # template_name = 'author_chamber.html'
        #         #  all_objs
        #         # def get_context_data(self):
        #                 # if  self.request.user.is_author:

#         # ...