from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Author

# View for listing posts, with optional category and author filtering
def post_list_view(request, category_name=None, author_id=None):
    if category_name:
        queryset = Post.objects.filter(category__name=category_name, is_public=True)
    elif author_id:
        queryset = Post.objects.filter(author__id=author_id, is_public=True)
    else:
        queryset = Post.objects.filter(is_public=True)

    queryset = queryset.order_by('-date_publish')

    # Pagination
    paginator = Paginator(queryset, 3)  # Show 3 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'object_list': page_obj,
        'category_list': Category.objects.all(),
        'author': get_object_or_404(Author, id=author_id) if author_id else None,
    }
    return render(request, 'blog/post_list.html', context)

# Detailed view of a post
def post_detail_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {
        'object': post,
        'author': post.author,
    }
    return render(request, 'blog/post_detail.html', context)
