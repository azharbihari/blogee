from django.core.paginator import Paginator
from django.urls import reverse
from django.shortcuts import get_object_or_404
from posts.models import Post, Comment, Category
from django.views.generic import DetailView, ListView
from posts.forms import CommentForm
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.core.exceptions import PermissionDenied
from datetime import datetime, timezone
from django.db.models import Count
from django.db.models.functions import TruncMonth, TruncYear
from django.views.generic.dates import MonthArchiveView


class PostListView(ListView):
    model = Post
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['archive_list'] = Post.objects.annotate(
            year=TruncYear('created_at'),
            month=TruncMonth('created_at')).values('year', 'month').annotate(count=Count('id')).order_by('-year', '-month')
        return context


class PostDetailView(FormMixin, DetailView):
    model = Post
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['category_list'] = Category.objects.all()
        context['archive_list'] = Post.objects.annotate(
            year=TruncYear('created_at'),
            month=TruncMonth('created_at')).values('year', 'month').annotate(count=Count('id')).order_by('-year', '-month')

        context['next_post'] = Post.objects.filter(
            created_at__gt=self.get_object().created_at).order_by('created_at').first()
        context['previous_post'] = Post.objects.filter(
            created_at__lt=self.get_object().created_at).order_by('-created_at').first()
        return context

    def get_success_url(self):
        return reverse('post-detail', kwargs={'slug': self.object.slug})


class PostMonthArchiveView(MonthArchiveView):
    queryset = Post.objects.all()
    paginate_by = 10
    date_field = "created_at"
    allow_future = True


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = get_object_or_404(Post, slug=self.kwargs['slug'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post-detail', kwargs={'slug': self.kwargs['slug']})


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_object(self):
        object = super().get_object()
        if not object.user == self.request.user:
            raise PermissionDenied
        return object

    def get_success_url(self):
        return reverse('post-detail', kwargs={'slug': self.object.post.slug})


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ["content"]

    def get_object(self):
        object = super().get_object()
        if not object.user == self.request.user:
            raise PermissionDenied
        return object

    def get_success_url(self):
        return reverse('post-detail', kwargs={'slug': self.object.post.slug})


class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['archive_list'] = Post.objects.annotate(
            year=TruncYear('created_at'),
            month=TruncMonth('created_at')).values('year', 'month').annotate(count=Count('id')).order_by('-year', '-month')

        # Pagination for posts related to the category
        post_list = self.object.post_set.all()
        paginator = Paginator(post_list, 10)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['page_obj'] = page_obj
        return context
