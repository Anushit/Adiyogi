from django.urls import path
from . import views
urlpatterns = [
    path('categorytable/', views.categorytable,name="categorytable"),
    path('AddCategory/', views.AddCategory, name="AddCategory"),
    path('delete_Category/<int:id>/', views.delete_Category, name="deleteCategory"),
    path('Update_Category/<int:id>/', views.Update_Category, name="UpdateCategory"),
    path('ProductTable/',views.ProductTable,name="ProductTable"),
    path('AddProduct/',views.AddProduct,name="AddProduct"),
    path('delete_Product/<int:id>/', views.delete_Product, name="deleteProduct"),
    path('Update_Product/<int:id>/', views.Update_Product, name="UpdateProduct"),
    path('AddItem/',views.AddItem,name="AddItem"),
    path('ItemTable/',views.ItemTable,name="ItemTable"),
    path('delete_Item/<int:id>/', views.delete_Item, name="deleteItem"),
    path('Update_Item/<int:id>',views.Update_Item, name="UpdateItem"),
    path('Items/', views.Items, name='Items'),
    path('SearchResultsView/', views.SearchResultsView, name="search_results"),
    path('AllProducts/',views.AllProducts, name="AllProducts"),
    path('ItemStatus/<int:id>/',views.ItemStatus,name='ItemStatus'),
    path('shop/',views.shop,name="shop"),
    path('SearchResultsView/', views.SearchResultsView, name='search_results'),
    path('product_detail/<int:id>/',views.product_detail, name="product_detail"),
    path('details/<int:id>/', views.details_view,name="details_view"),

    ]