from django.urls import path, re_path
from . import views


app_name = 'languages'
urlpatterns = [
    path('', views.index, name='Index'),
    path('<int:language_id>/<str:name>/<int:topic_id>/<str:topic_name>', views.topic_language_view,
         name='language_topic_view'),
    path('<int:language_id>/<str:name>/<str:framework_name>/<int:topic_id>/<str:topic_name>',
         views.topic_framework_view, name='framework_topic_view'),
    path('<int:item_id>/<str:name>/', views.language_view, name='language_view'),
    path('<int:item_id>/<str:name>/<str:framework_name>/', views.framework_view, name='framework_view'),
]
