from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.template.loader import render_to_string
from otonevrolog_main.blog.forms import BlogPostForm, CommentForm
from otonevrolog_main.blog.models import BlogPost, Comment


class BlogCreateView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/blog_create.html'
    success_url = reverse_lazy('blog_list')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.groups.filter(name='Doctor Administrator').exists():
            return HttpResponseForbidden("You do not have permission to access this page.")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['can_add_blog'] = (self.request.user.groups.filter(name='Doctor Administrator')
                                   .exists()) if self.request.user.is_authenticated else False
        return context

    def get_queryset(self):
        return BlogPost.objects.all().order_by('-created_at')


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = self.object.comments.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog_post = self.object
            comment.author = request.user.get_full_name()
            comment.save()
            return redirect('blog_detail', pk=self.object.pk)

        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)


class EditCommentView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_edit_comment.html'

    def get_success_url(self):
        return reverse_lazy('blog_detail', kwargs={'pk': self.object.blog_post.pk})

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user.get_full_name())


class DeleteCommentView(DeleteView):
    model = Comment
    template_name = 'blog/comment_delete_comment.html'

    def get_success_url(self):
        return reverse_lazy('blog_detail', kwargs={'pk': self.object.blog_post.pk})

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user.get_full_name())
