from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView


from djangor.models import Entry
from djangor.forms import EntryForm
from djangor.views import AddEntryView


urlpatterns = patterns('',
    # List view for all posts:
    url(r'^$',
        ListView.as_view(
            queryset=Entry.objects.order_by('-pub_date')[:5],
            context_object_name="entries",
            template_name="blog/entry_list.html"
        ),
        name="entry_list"),
    url(r'^add/$',
        login_required(AddEntryView.as_view(
            model=Entry,
            form_class=EntryForm,
            template_name="blog/entry_form.html",
            success_url="/",
        )),
        name="add_entry"),
    url(r'^accounts/profile/$',
        ListView.as_view(
            queryset=Entry.objects.all(),
            context_object_name="entries",
            template_name="blog/entry_list.html"
        ),
        name="entry_list"),
)