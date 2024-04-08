from django.shortcuts import render
from django.views import generic
from .models import item, MEAL_TYPE

class MenuList(generic.ListView):
    queryset = item.objects.order_by("date_created")
    template_name = "index.html"

    # To get data from database
    def get_context_data(self, **kwargs):
        # Creates the dictionary
        context = super().get_context_data(**kwargs)
        context["meal"] = MEAL_TYPE
        return context

class MenuItemDetail(generic.DetailView):
    model = item
    template_name = "menu_item_detail.html"

