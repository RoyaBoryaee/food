from django.shortcuts import render
from django.http import HttpResponse
from restaurant_admin import models
#from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView

def index(request):
    my_dict = {'insert_me': 'HELLO I AM FROM VIEWS.PY OF KITCHEN !'}
    return render(request, 'kitchen/index.html', context=my_dict)

class TableStateListView(ListView):
    template_name = 'kitchen/TableStatelist.html'
    model = models.Table
    fields = '__all__'

class TableOrdersView(TemplateView):
    template_name = 'kitchen/TableOrders.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order_list = models.Table.objects.get(pk = kwargs['pk']).OrderList_Table.all()
        context['order_list'] = order_list
    
        return context
