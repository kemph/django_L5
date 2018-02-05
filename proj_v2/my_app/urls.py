from my_app import views
from django.conf.urls import url,include

app_name = 'my_app'

urlpatterns = [
    url(r'^register/',views.register,name='register'),
    url(r'^other/',views.other,name='other'),
    url(r'^user_login/$',views.user_login,name='user_login'),


]
