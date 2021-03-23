from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('services/',views.services,name="services"),
    path('Product/',views.Product,name="Product"),
    path('register/', views.register,name="register"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('login1/', views.login1, name='login1'),
    path('logout1/', views.logout1, name="logout1"),
    path('UserTable/', views.UserTable, name="UserTable"),
    path('delete/<int:id>/', views.delete_data, name="deletedata"),
    path('update/<int:id>/', views.Update_data,name="updatedata"),
    path('adduser/', views.adduser, name="adduser"),
    path('EditProfile/<int:id>/', views.EditProfile, name="EditProfile"),
    path('forgot/',views.forgot,name='forgot'),
    path('UserStatus/<int:id>/',views.UserStatus,name="UserStatus"),
    # path('countries',views.countries,name="register"),
    path('stateFetch/<int:id>', views.stateFetch),
    path('cityFetch/<int:id>', views.cityFetch),
    path('ContentTable/',views.ContentTable,name="ContentTable"),
    path('UpdatePost/<int:id>',views.UpdatePost,name="UpdatePost"),
    path('delete/<int:id>',views.delete_post,name="deletepost"),
    path('PostStatus/<int:id>',views.PostStatus,name="PostStatus"),
]

