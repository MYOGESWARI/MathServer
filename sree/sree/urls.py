from django.contrib import admin
from django.urls import path
from side import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Lamp Power Calculator/',views.powerlamp,name="Lamp Power Calculator"),
    path('',views.powerlamp,name="Lamp Power Calculator"),
]