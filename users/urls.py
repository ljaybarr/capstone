from django.urls import path
from .views import UserLoginView, user_logout_view, UserRegisterView, UserProfileEditView, UserProfileView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name="login"), # CLASS-BASED VIEW
    path('register/', UserRegisterView.as_view(), name="register"),
    path('logout/', user_logout_view, name="logout"), # Function-based view
    path('edit_profile', UserProfileEditView.as_view(), name="edit_profile"),
    path('profile/<int:user_id>/', UserProfileView.as_view(), name="profile"),
]
