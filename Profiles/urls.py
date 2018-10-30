from django.urls import path
from . import views

app_name = 'Profiles'

urlpatterns = [
    path('',views.PostList.as_view(),name='postlist'),
    path('<int:pk>/',views.Detailview.as_view(),name='detail'),
    path('post/add/',views.addpost.as_view(),name='addpost'),
    path('post/<int:pk>/',views.updatepost.as_view(),name='updatepost'),
    path('post/drafts/',views.post_draftView.as_view() ,name='post_draft'),
    path('post/<int:pk>/publish/',views.publishpostView.as_view(),name='publishpost'),
    path('post/<int:pk>/delete/',views.PostDelete.as_view(),name='postdelete'),
    path('register/',views.UserformView.as_view(),name='register'),
    path('login/',views.LoginView.as_view(),{'template_name':'Profiles/login.html'}, name='login')
    ]
