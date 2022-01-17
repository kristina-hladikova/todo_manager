from django.urls import path
from todo_manager_app.views import homepage, RegistrationView, LoginView, LogoutView, ChangePasswordView, todo_detail, \
    todo_list, create_todo, delete_todo, update_todo, search_todo

urlpatterns = [
    path('', homepage, name="homepage"),
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('change_password', ChangePasswordView.as_view(), name='change_password'),
    path("todos/", todo_list, name="todos"),
    path("todos/<int:todo_id>/", todo_detail, name="todo_detail"),
    path("create_todo/", create_todo, name="create_todo"),
    path("todos/<int:todo_id>/update_todo/", update_todo, name="update_todo"),
    path("todos/<int:todo_id>/delete_todo/", delete_todo, name="delete_todo"),
    path("search_todo/", search_todo, name="search_todo"),

]


