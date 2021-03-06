from django.conf.urls import url,include
from django.contrib import admin
from . import views

app_name = 'stories'
urlpatterns = [
    url(r'^index$', views.index, name="home"),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.login_user, name="login_user"),
    url(r'^register/$', views.register_user, name="register_user"),
    url(r'^logout_user/$', views.logout_user, name="logout_user"),
    url(r'^story/(?P<story_id>[0-9]+)/page/(?P<page>[0-9]+)/$', views.post, name="post"),
    url(r'^user/$', views.user_profile, name="profile"),
    url(r'^addstory/$', views.add_story, name="new_story"),
    url(r'^story/(?P<story_id>[0-9]+)/add_chapter/$', views.addChapter, name="add_chapter"),
    url(r'^delete_story/(?P<story_id>[0-9]+)/$', views.delete_story, name="delete_story"),
    url(r'^addcomment/(?P<story_id>[0-9]+)/$', views.addcomment, name="addcomment"),
    url(r'^edit_story/(?P<pk>[0-9]+)/$', views.EditStory.as_view(), name="edit_story"),
    url(r'^story/(?P<story_id>[0-9]+)/comments/$',views.viewComment, name="comments"),
    url('^$',views.welcome, name="welcome")





]