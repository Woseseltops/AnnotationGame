from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'annotationgame.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'main.views.stimulus'),
    url(r'^add_answer/(?P<stimulus_index>[0-9]{1,4})/(?P<answer_pk>[0-9]{1,4})$', 'main.views.add_answer'),
    url(r'^playername/(?P<streak_id>[0-9]{1,4})','main.views.playername'),
    url(r'^highscore/','main.views.highscore'),
    url(r'^admin/', include(admin.site.urls)),
]
