from django.conf.urls import url,include
from django.contrib import admin
from deneme import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
#    url(r'^word/$', views.wordList),
    url(r'^word/(?P<id>[0-9]+)/$', views.word_detail),
    url(r'^word3/$', views.wordlist3),
    url(r'^login/$', views.login),
    url(r'^mean/$', views.meanlist),
    url(r'^wedit/$', views.wordEdit),
    url(r'^wdelete/$', views.worddelete),
    url(r'^kullanici/$', views.kullanici),
    url(r'^wordsearch/$', views.wordsearch),
    url(r'^wordid/$', views.wordgetid),
    url(r'^meanid/$', views.meangetid),
    url(r'^mdelete/$', views.meansil),
    url(r'^medit/$', views.meanedit),
    url(r'^wgetuser/$', views.wordgetuserid),

]
