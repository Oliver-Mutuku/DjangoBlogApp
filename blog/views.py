from django.shortcuts import render


posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog 1',
        'content': 'First Post Content',
        'date_posted': 'January 11th, 2024'
    },
    {
        'author': 'Oliver Mutuku',
        'title': 'Blog 2',
        'content': 'Second Post Content',
        'date_posted': 'January 12th, 2024'      
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


