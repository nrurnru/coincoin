from django.urls import path
from community import views


app_name = 'community'
urlpatterns = [
    path('', views.index, name='index'),      # /community
    path('<int:agenda_id>', views.detail, name='detail'),      # /community/3
    path('write', views.write, name='write'), # /community/write
    path('submit', views.submit, name='submit'), # submit 호출
    path('<int:agenda_id>/replysubmit', views.replysubmit, name='replysubmit') #replysubmit
]
