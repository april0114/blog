from django.shortcuts import render,redirect

# Create your views here.
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def base(request, spk):
    s = Post.objects.get(id = spk)
    context = {
        "s":s,
    }
    return render(request, "blog/base.html",context)

def blogs_form(request):
    if request.method == "POST":
        t = request.POST.get("title")
        c = request.POST.get("content")
        a = request.POST.get("author")
        Post(title= t, content = c, author = a).save()
        return redirect("index")
    return render( request, "blog/blogs_form.html")

def blogs_update(request, spk):
    s = Post.objects.get(id = spk)
    if request.method == "POST":
        t = request.POST.get("title")
        c = request.POST.get("content")
        print(c)
        a = request.POST.get("author")
        s.title,s.content,s.author = t,c,a
        s.save()
        return redirect("index")
    context = {
        "s": s
    }
    return render(request,"blog/blogs_update.html",context)



def delete (request, spk):
    s = Post.objects.get(id = spk)
    s.delete()
    return redirect("index")





