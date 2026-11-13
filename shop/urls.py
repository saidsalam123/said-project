from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from catalog import views

urlpatterns = [
    path("", views.catalog, name="catalog"),
    path("new/", views.new_products, name="new_products"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
