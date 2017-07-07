from django.contrib import admin
from.models import Story, Comment,Chapter


class StoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'author', 'summary')
    list_filter = ('author', 'author')
    ordering = ('pub_date',)
    search_fields = ('title', 'author')


class CommentAdmin(admin.ModelAdmin):
    list_display = 'id', 'story', 'writer', 'comment'
    search_fields = ('story', 'writer')


class ChapterAdmin(admin.ModelAdmin):
    list_display = ('id', 'story', 'chapter_number', 'update_time')
    search_fields = ('story', 'chapter_number')


admin.site.register(Story, StoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Chapter, ChapterAdmin)
