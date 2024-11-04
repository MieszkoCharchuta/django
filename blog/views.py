from django.shortcuts import render, get_object_or_404


from .models import Post, Category, Author


# Create your views here.
def post_list_view(request, category_name=None):
    if category_name:
        queryset = Post.objects.filter(category__name=category_name)
    else:
        queryset = Post.objects.filter(is_public=True)
        queryset = queryset.order_by('-date_publish')
    context = {
        'object_list': queryset,
        'category_list': Category.objects.all(),
    }
    return render(request, 'blog/post_list.html', context)
def post_detail_view(request, post_id):
    context = {
        'object': get_object_or_404(Post, id=post_id),
        'author': get_object_or_404(Author)
    }
    return render(request, 'blog/post_detail.html', context)
