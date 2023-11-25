from django.urls import path, include


urlpatterns = [
    # path('', include('viewset.urls')),
    # path('', include('genericview.urls')),
    path('', include('apiview.urls')),
]