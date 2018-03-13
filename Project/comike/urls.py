from django.conf.urls import url

from . import views #viewsの関数を読み込み

urlpatterns = [
    url(r'^comiket-entry/entry', views.entry),#viewsの関数を指定。 '^'は開始位置、'$'は終了位置
    url(r'^comiket-entry/confirmation', views.confirmation),  # viewsの関数を指定。 '^'は開始位置、'$'は終了位置
    url(r'^comiket-entry/complete', views.complete),
    url(r'^main-menu/executive', views.executive),
    url(r'^main-menu/information-setting', views.information),

]
