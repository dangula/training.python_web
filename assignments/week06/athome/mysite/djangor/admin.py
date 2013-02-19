from django.contrib import admin
from djangor.models import entries

class entriesAdmin(admin.ModelAdmin):
    list_display = ('pub_date','title', 'text','owned',
                    'published_today')
    list_filter = ('pub_date', )
    ordering = ('pub_date', )
    
admin.site.register(entries, entriesAdmin)