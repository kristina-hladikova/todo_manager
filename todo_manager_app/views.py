from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.db.models import Q
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin

from todo_manager_app.forms import RegistrationForm, TodoForm
from todo_manager_app.models import Todo


def homepage(request):
    return render(request, "homepage.html")


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('homepage')


class LoginView(FormMixin, TemplateView):
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            return redirect('login')

        login(request, user)
        return redirect('homepage')


class ChangePasswordView(PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('homepage')


class RegistrationView(FormMixin, TemplateView):
    template_name = 'accounts/register.html'
    form_class = RegistrationForm

    def post(self, request, *args, **kwargs):
        bounded_form = self.form_class(request.POST)
        if bounded_form.is_valid():
            bounded_form.save()
            return redirect('homepage')
        else:
            return TemplateResponse(request, 'accounts/register.html', context={'form': bounded_form})


@login_required(login_url='login')
def todo_list(request):
    # todo_list = Todo.objects.filter(user=request.user)
    todo_list_undone = Todo.objects.filter(user=request.user, status_done=False)
    todo_list_done = Todo.objects.filter(user=request.user, status_done=True)
    context = {
        'todo_list_undone': todo_list_undone,
        'todo_list_done': todo_list_done,
    }
    return render(request, 'todos.html', context=context)


@login_required(login_url='login')
def todo_detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    name = todo.name
    description = todo.description
    due_date = todo.due_date
    status_done = todo.status_done
    attachment = todo.attachment
    context = {
        "todo": todo,
        "name": name,
        'description': description,
        'due_date': due_date,
        'status_done': status_done,
        'attachment': attachment,
    }
    return render(request, 'todo_detail.html', context=context)


@login_required(login_url='login')
def create_todo(request):
    form = TodoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save(request.user)
        return redirect('/todos/')
    context = {"form": form}
    return render(request, "create_todo.html", context)


@login_required(login_url='login')
def update_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save(request.user)
        return redirect(f'/todos/{todo_id}/')
    context = {"form": form}
    return render(request, "update_todo.html", context)


def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('/todos/')


def search_todo(request):
    if request.method == "POST":
        searched = request.POST['searched']
        todos = Todo.objects.filter(user=request.user, name__contains=searched)
        return render(request, 'search_todo.html', {'searched': searched, 'todos': todos})
    else:
        return render(request, 'search_todo.html', {})

