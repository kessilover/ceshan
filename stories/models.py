from django.db import models
from django.contrib.auth.models import User, Permission
from tinymce.models import HTMLField


class Story(models.Model):

    rating_choices = (
        ('k', 'K'),
        ('k+', 'K+'),
        ('t', 'T' ),
        ('m', 'M')
    )

    title = models.CharField(max_length=250, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    summary = models.TextField(max_length=500, null=False)
    pub_date = models.DateField(auto_now_add=True, blank=False, null=False)
    isCross = models.BooleanField(default=False)
    tags = models.CharField(max_length=250, null=False)
    rating = models.CharField(max_length=3, choices=rating_choices, default=rating_choices[1])
    has_chapter = models.BooleanField(default=False)

    def __str__(self):
        return self.title + " - " + self.author.username


class Comment(models.Model):
    comment = models.CharField(max_length=500, null=None)
    writer = models.CharField(max_length=50, default="guest")
    story = models.ForeignKey(Story, editable=False)

    def __str__(self):
        return "Comment is : " + str(self.comment) + "and written by : " + str(self.writer)


class Chapter(models.Model):
    story = models.ForeignKey(Story)
    chapter_number = models.IntegerField(editable=False, default=1)
    chapter = HTMLField()
    update_time = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        number = Chapter.objects.filter(story=self.story).count()

        self.chapter_number = number + 1
        story = self.story
        if not story.has_chapter:
            story.has_chapter = True
            story.save()
        super(Chapter, self).save(*args, **kwargs)
