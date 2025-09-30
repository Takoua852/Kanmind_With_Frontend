from django.urls import path
from . import views


urlpatterns = [
    path("login/", views.login_page, name="auth"),
    path('registration/', views.register_page, name='register'),
    path("imprint/", views.imprint_page, name="imprint"),
    path("privacy/", views.privacy_page, name="privacy"),
    path("dashboard/", views.dashboard_page, name="dashboard"),
]
