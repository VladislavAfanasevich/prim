from django.contrib import admin
from news.models import News, Category, Tag, Comments
from django_summernote.admin import SummernoteModelAdmin


class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ('text_description', 'text')


admin.site.register(News, NewsAdmin)
admin.site.register(Category)
admin.site.register(Tag)


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'new', 'date', 'moderation')


admin.site.register(Comments, CommentsAdmin)
