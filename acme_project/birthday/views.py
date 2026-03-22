from .forms import BirthdayForm
# Импортируем из utils.py функцию для подсчёта дней.
from .utils import calculate_birthday_countdown
# Импортируем модель дней рождения.
from .models import Birthday
# Импортируем класс пагинатора.

from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy


class BirthdayMixin:
    # Указываем модель, с которой работает CBV...
    model = Birthday
    # Указываем namespace:name страницы, куда будет перенаправлен пользователь
    # после создания объекта:
    success_url = reverse_lazy('birthday:list')


class BirthdayDeleteView(BirthdayMixin, DeleteView):
    pass


class BirthdayUpdateView(BirthdayMixin, UpdateView):
    form_class = BirthdayForm


class BirthdayCreateView(BirthdayMixin, CreateView):
    form_class = BirthdayForm


# Наследуем класс от встроенного ListView:
class BirthdayListView(ListView):
    # Указываем модель, с которой работает CBV...
    model = Birthday
    # ...сортировку, которая будет применена при выводе списка объектов:
    ordering = 'id'
    # ...и даже настройки пагинации:
    paginate_by = 5
