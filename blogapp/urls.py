from .import views
from django.urls import path

app_name = 'blogapp'

urlpatterns = [
    path('', views.HomePageView.as_view(), name = 'homepage'),
    path('login/', views.LoginView.as_view(), name='login_user'),
    path('signup/', views.SignUpView.as_view(), name='sign_up'),
    path('logout/', views.logout_user, name='logout_user'),
    path('fav_blog/', views.fav_blog, name='fav_blog'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('user_blog/', views.UserBlogView.as_view(), name='user_blog'),
    path('<id>/', views.SingleBlogView.as_view(), name = 'single_blog'),
    path('add_comment/<post_id>', views.AddCommentView.as_view(), name = 'add_comment'),
]
