from django.shortcuts import render
from django.views.generic import View, DeleteView, UpdateView
from django.shortcuts import get_object_or_404, render, redirect
from .forms import PostCreateForm
from .models import Post
from django.urls import reverse_lazy
from ckeditor.fields import RichTextField




class BlogListView(View):

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        context = {
            'posts':posts
        }
        return render(request, 'blog_list.html', context)



class BlogCreateView(View):
    def get(self, request, *args, **kwargs):
        form = PostCreateForm()
        context = {
            'form':form
        }
        return render(request, 'blog_create.html', context)

    def post(self, request, *args, **kwargs):
        if request.method=='POST':
            form = PostCreateForm(request.POST)
            if form.is_valid():
                nombre = form.cleaned_data.get('nombre')
                email = form.cleaned_data.get('email')
                titulo = form.cleaned_data.get('titulo')
                contenido = form.cleaned_data.get('contenido')

                p, created = Post.objects.get_or_create(nombre=nombre, email=email, titulo=titulo, contenido=contenido)
                p.save()
                return redirect('appMensajeria:blog')
        context = {
            
        }
        return render(request, 'blog_create.html', context)



class BlogDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)


        context = {
            'post':post
        }
        return render(request, 'blog_detail.html', context)



class BlogDeleteView(DeleteView):
    model=Post
    template_name='blog_delete.html'
    success_url= reverse_lazy('appMensajeria:blog')




