from django.conf.urls import url

from . import views

app_name = 'news'
urlpatterns = [
    url(r'^$', views.ArticleListView.as_view(), name='article-list'),
    url(r'^article/(?P<slug>[-\w]+)/$', views.ArticleDetailView.as_view(), name='article-detail'),
    url(r'^article/(?P<slug>[-\w]+)/comment$', views.comment, name='comment'),
    url(r'^addarticle/?$', views.ArticleCreateView.as_view(), name='add-article'),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.category, name='category'),
    url(r'^reviewcomment/(?P<comment_id>[0-9]+)/$', views.reviewcomment, name='review-comment'),
    url(r'^article/(?P<slug>[-\w]+)/like$', views.like, name='like'),
]
