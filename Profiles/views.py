from django.shortcuts import render,redirect,get_object_or_404
from django.views import generic
from .models import Post
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import View
from .forms import Postform , Userform
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login
from  django.contrib.auth.decorators import login_required


from django.utils import timezone

class PostList(generic.ListView):
    template_name ='Profiles/index.html'

    def get_queryset(self):
        return Post.objects.all()

class Detailview(generic.DetailView):
    model = Post
    template_name = 'Profiles/detail.html'


class addpost(CreateView):
    model = Post
    fields = ['title','text']
    form_class = Postform
    template_name = 'Profiles/post_form.html'


    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})


    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            post.save()
            return redirect('Profiles:detail', pk=post.pk)


"""def post_new(request):
    if request.method == "POST":
        form = Postform(request.POST)
        if form.is_valid():
          post = form.save(commit=False)
          post.author = request.user
          post.published_date = timezone.now()
          post.save()
          return redirect('Profiles:detail', pk=post.pk)
        else:
            form = Postform()
        return render(request, 'Profiles:updatepost', {'form': form})"""

class updatepost(UpdateView):
    model = Post
    fields = ['title','text']



class post_draftView(View):
    model = Post
    template_name = 'Profiles/post_drafts.html'

    def post_draft (self,request):
        posts=Post.objects.filter(published_date__isnull=True).order_by('created_date')
        return render(request,self.template_name,{'posts':posts})

class publishpostView(View):

    model =Post
    template_name = 'Profiles/detail.html'

    def postpublish (self,request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.publish()
        return redirect(self.template_name, pk=pk)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class UserformView(View):
    form_class = Userform
    template_name = 'Profiles/registration_form.html'

    def get (self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)

            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()


            user=authenticate(username=username,password=password)
            if user is not None:

                if user.is_active:
                    login(request,user)
                    return redirect('Profiles:postlist')

        return render(request,self.template_name,{'form':form})


class PostDelete(DeleteView):
    model = Post
    success_url =reverse_lazy('Profiles:postlist')

class LoginView(View):
    template_name='Profiles/login.html'
