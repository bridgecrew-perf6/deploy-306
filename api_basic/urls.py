from .views import article_list,article_detail,ArticleList,ArticleDetail,GenericAPI
from django.urls import path
from api_basic import views 
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('article/',ArticleList.as_view()),
    path('detail/<int:pk>/', ArticleDetail.as_view()),
    path('generic/article/<int:id>/',GenericAPI.as_view()),
    path('login',views.login,name="login"),
]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)