from django.contrib.auth.views import LogoutView
from django.urls import path

from apps.catalog import views
from apps.catalog.views import LoginUserView

urlpatterns = [
    path('', views.PhonebookListView.as_view(), name='home'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('birthday', views.BirthdayTemplateView.as_view(), name='birthday'),
    path('birthday_full', views.BirthdayFullTemplateView.as_view(), name='birthday_full'),
    path('companies', views.CompaniesCreateView.as_view(), name='companies'),
    path('companies_update/<int:pk>', views.CompaniesUpdateView.as_view(), name='companies_update'),
    path('companies_delete/<int:pk>', views.CompaniesDeleteView.as_view(), name='companies_delete'),
    path('workers', views.WorkersListView.as_view(), name='workers'),
    path('workers_update/<int:pk>', views.WorkersUpdateView.as_view(), name='workers_update'),
    path('workers_delete/<int:pk>', views.WorkersDeleteView.as_view(), name='workers_delete'),
    path('partners', views.PartnersListView.as_view(), name='partners'),
    path('partners_update/<int:pk>', views.PartnersUpdateView.as_view(), name='partners_update'),
    path('partners_delete/<int:pk>', views.PartnersDeleteView.as_view(), name='partners_delete'),
]
