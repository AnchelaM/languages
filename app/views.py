from django.shortcuts import render_to_response, get_object_or_404, render
from app.models import BlogPost, BlogPostee, ContactForm
from django.template import RequestContext
from django.core.mail import send_mail
from django.core.paginator import *
from django.http import HttpResponseRedirect
from taggit.models import Tag


def index(request):
    homepage = BlogPost.objects.all().filter(homepage=True)
    posts = BlogPost.objects.all().filter(published=True)
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render_to_response('app/index.html', {'posts': posts, 'homepage': homepage, },
                              context_instance=RequestContext(request))


def indexee(request):
    postees = BlogPostee.objects.all().filter(published=True)
    paginator = Paginator(postees, 5)
    page = request.GET.get('page')

    try:
        postees = paginator.page(page)
    except PageNotAnInteger:
        postees = paginator.page(1)
    except EmptyPage:
        postees = paginator.page(paginator.num_pages)
    return render_to_response('app/indexee.html', {'postees': postees, },
                              context_instance=RequestContext(request))


def about(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            recipients = ['recipient@example.com']
            send_mail(subject, message, sender, recipients, fail_silently=True)
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()
    return render(request, 'app/about.html', {'form': form})


def category(request, tag):
    posts = BlogPost.objects.all().filter(tags__name__in=[tag])
    return render_to_response('app/category.html', {'posts': posts, 'tag': tag},
                              context_instance=RequestContext(request))


def post(request, slug):
    singlepost = get_object_or_404(BlogPost, slug=slug)
    return render_to_response('app/post.html', {'singlepost': singlepost},
                              context_instance=RequestContext(request))
