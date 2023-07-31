from posts.models import Post, Category
from django.db.models import Count
from django.db.models.functions import TruncMonth, TruncYear
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_posts"] = Post.objects.all()[:5]
        context['category_list'] = Category.objects.all()
        context['archive_list'] = Post.objects.annotate(
            year=TruncYear('created_at'),
            month=TruncMonth('created_at')).values('year', 'month').annotate(count=Count('id')).order_by('-year', '-month')
        return context
