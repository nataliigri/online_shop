from django.urls import path
from . import views
from .views import export_excel, import_data

app_name = 'store'

urlpatterns = [
     path('', views.all_products, name='all_products'),
     path('item/<slug:slug>/', views.product_detail, name='product_detail'),
     path('search/<slug:category_slug>/', views.category_list, name='category_list'),
     path('diagrams/',views.diagrams, name='diagrams'),
     path('export/', export_excel, name='export_excel'),
     path('import/', import_data, name='import_data'),
]
