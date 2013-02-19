from django.conf.urls import patterns, url
from django.http import HttpResponse
from django.views.generic import ListView,DetailView

from djangor.models import entries

def stub(request, *args, **kwargs):
    return HttpResponse('Blog Stub View', mimetype="text/plain")

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(queryset=entries.objects.order_by('-pub_date')[:5],
            context_object_name='entries',
            template_name="blog/MainPage.html"), name="blog_list"),
    url(r'^add/user/', stub, name="add_entry"),
    url(r'^login/', stub, name="login"),
    url(r'^logut/', stub, name="logout"),
    url(r'^view/owner/', stub, name="showUserBlog"),
    url(r'^view/dateRange/', stub, name="showBlogArchive"),

    )

