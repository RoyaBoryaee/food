from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView,  ModelFormMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import FormView,TemplateView
from . import models
from . import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse , reverse_lazy
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View



# Create your views here.
@login_required
def change_password(request):
    if request.method == 'POST':
        form =PasswordChangeForm(request.user, request.POST)
        if form.is_valid():

            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('restaurant_admin:login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
        print(form.error_messages)

    return render(request, 'restaurant_admin/change_password.html', {
        'form': form
    })

def index(request):
    my_dict = {'insert_me': 'HELLO I AM FROM VIEWS.PY OF RESTAURANT_ADMIN !'}
    return render(request, 'restaurant_admin/index.html', context=my_dict)

@login_required
def Home(request):
    return render(request,'restaurant_admin/home.html')

@method_decorator(login_required, name='dispatch')
class FoodCategoryCreateView(CreateView):
    template_name = 'restaurant_admin/FoodCategorycreate.html'
    model = models.FoodCategory
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class FoodCategoryUpdateView(UpdateView):
    template_name = 'restaurant_admin/FoodCategoryupdate.html'
    model = models.FoodCategory
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class FoodCategoryDetailView(DetailView):
    template_name = 'restaurant_admin/FoodCategorydetail.html'
    model = models.FoodCategory
    fields = '__all__'

'''
@method_decorator(login_required, name='dispatch')
class FoodCategoryHomeDetailView(FormView, ListView):
    template_name = 'restaurant_admin/FoodCategoryHomedetail.html'
    form_class = forms.InputForm
    model = models.FoodCategory
    fields='__all__
'''
@method_decorator(login_required, name='dispatch')
class FoodCategoryHomeDetailView(View):
    template_name = 'restaurant_admin/FoodCategoryHomedetail.html'
    #form_class = forms.InputForm
    model = models.FoodCategory
    fields='__all__'
    chosen_object=None
    update_form=None
    queryset= models.FoodCategory.objects.all()

    def get(self,*args,**kwargs):
        self.queryset=self.model.objects.all()
        return render(self.request, 'restaurant_admin/FoodCategoryHomedetail.html',context={'object_list':self.queryset,
                                                                                      'chosen_object': self.chosen_object,
                                                                                      'update_form': self.update_form})
    def post(self,*args,**kwargs):
        postvalues = self.request.POST
        print(postvalues)
        if postvalues.get('foodcategory_id', None):
            id = self.request.POST.get('foodcategory_id')
            self.chosen_object= self.model.objects.get(pk=id)
            #print(self.chosen_object.name)

        if self.chosen_object != None:
            self.update_form=forms.FoodCategoryForm(instance=self.chosen_object)

        if postvalues.get('edit',None):
            self.chosen_object=self.model.objects.get(pk=postvalues['pk'])
            self.update_form=forms.FoodCategoryForm(self.request.POST,instance=self.chosen_object)
            if self.update_form.is_valid():
                foodcategory=self.update_form.save()
                print('yesk')
                foodcategory.save()
                self.queryset= models.FoodCategory.objects.all()
                self.chosen_object=self.model.objects.get(pk=foodcategory.pk)
                self.update_form=forms.FoodCategoryForm(instance=self.chosen_object)

        return render(self.request,'restaurant_admin/FoodCategoryHomedetail.html',context={'object_list':self.queryset,
                                                                                      'chosen_object': self.chosen_object,
                                                                                      'update_form': self.update_form})



@method_decorator(login_required, name='dispatch')
class FoodCategoryDeleteView(DeleteView):
    template_name = 'restaurant_admin/FoodCategorydelete.html'
    model = models.FoodCategory
    fields = '__all__'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_success_url(self):
        return reverse('restaurant_admin:FoodCategoryHome_detail')

@method_decorator(login_required, name='dispatch')
class FoodCategoryListView(ListView):
    template_name = 'restaurant_admin/FoodCategorylist.html'
    model = models.FoodCategory
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class FoodCreateView(CreateView):

    model = models.Food
    fields = '__all__'
    template_name = 'restaurant_admin/Foodcreate.html'

    def form_valid(self, form):
        food_category = form.cleaned_data['food_category']
        food = form.save(commit=False)
        food.food_category= food_category
        food.save()
        return super(FoodCreateView, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class FoodUpdateView(UpdateView):

    model = models.Food
    fields = '__all__'
    template_name = 'restaurant_admin/Foodupdate.html'

    def form_valid(self, form):
        food_category = form.cleaned_data['food_category']
        food = form.save(commit=False)
        food.food_category= food_category
        food.save()
        return super(FoodUpdateView, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class FoodDetailView(DetailView):
    template_name = 'restaurant_admin/Fooddetail.html'
    model = models.Food
    fields = '__all__'
'''
@method_decorator(login_required, name='dispatch')
class FoodHomeDetailView(FormView, ListView):
    template_name = 'restaurant_admin/FoodHomedetail.html'
    form_class = forms.InputForm
    model = models.Food
    fields='__all__'
'''


@method_decorator(login_required, name='dispatch')
class FoodHomeDetailView(View):
    template_name = 'restaurant_admin/FoodHomedetail.html'
    #form_class = forms.InputForm
    model = models.Food
    fields='__all__'
    chosen_object=None
    update_form=None
    queryset= models.Food.objects.all()

    def get(self,*args,**kwargs):
        self.queryset=self.model.objects.all()
        return render(self.request, 'restaurant_admin/FoodHomedetail.html',context={'object_list':self.queryset,
                                                                                      'chosen_object': self.chosen_object,
                                                                                      'update_form': self.update_form})
    def post(self,*args,**kwargs):
        postvalues = self.request.POST

        if postvalues.get('food_id', None):
            id = self.request.POST.get('food_id')
            self.chosen_object= self.model.objects.get(pk=id)
            #print(self.chosen_object.name)

        if self.chosen_object != None:
            self.update_form=forms.FoodForm(instance=self.chosen_object)

        if postvalues.get('edit',None):
            self.chosen_object=self.model.objects.get(pk=postvalues['pk'])
            self.update_form=forms.FoodForm(self.request.POST,instance=self.chosen_object)
            if self.update_form.is_valid():
                food=self.update_form.save()
                food.save()
                self.queryset= models.Food.objects.all()
                self.chosen_object=self.model.objects.get(pk=food.pk)
                self.update_form=forms.FoodForm(instance=self.chosen_object)

        return render(self.request,'restaurant_admin/FoodHomedetail.html',context={'object_list':self.queryset,
                                                                                      'chosen_object': self.chosen_object,
                                                                                      'update_form': self.update_form})

@method_decorator(login_required, name='dispatch')
class FoodDeleteView(DeleteView):
    template_name = 'restaurant_admin/Fooddelete.html'
    model = models.Food
    fields = '__all__'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_success_url(self):
        return reverse('restaurant_admin:FoodHome_detail')

@method_decorator(login_required, name='dispatch')
class FoodListView(ListView):
    template_name = 'restaurant_admin/Foodlist.html'
    model = models.Food
    fields = '__all__'


@method_decorator(login_required, name='dispatch')
class WorkerCreateView(CreateView):
    template_name = 'restaurant_admin/Workercreate.html'
    model = models.Worker
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class WorkerUpdateView(UpdateView):
    template_name = 'restaurant_admin/Workerupdate.html'
    model = models.Worker
    fields = '__all__'


@method_decorator(login_required, name='dispatch')
class WorkerDetailView(DetailView):
    template_name = 'restaurant_admin/Workerdetail.html'
    model = models.Worker
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class WorkerHomeDetailView(View):
    template_name = 'restaurant_admin/WorkerHomedetail.html'
    #form_class = forms.InputForm
    model = models.Worker
    fields='__all__'
    chosen_object=None
    update_form=None
    queryset= models.Worker.objects.all()

    def get(self,*args,**kwargs):
        self.queryset=self.model.objects.all()
        return render(self.request, 'restaurant_admin/WorkerHomedetail.html',context={'object_list':self.queryset,
                                                                                      'chosen_object': self.chosen_object,
                                                                                      'update_form': self.update_form})
    def post(self,*args,**kwargs):
        postvalues = self.request.POST

        if postvalues.get('worker_id', None):
            id = self.request.POST.get('worker_id')
            self.chosen_object= self.model.objects.get(pk=id)
            #print(self.chosen_object.name)

        if self.chosen_object != None:
            self.update_form=forms.WorkerForm(instance=self.chosen_object)

        if postvalues.get('edit',None):
            self.chosen_object=self.model.objects.get(pk=postvalues['pk'])
            self.update_form=forms.WorkerForm(self.request.POST,instance=self.chosen_object)
            if self.update_form.is_valid():
                worker=self.update_form.save()
                worker.save()
                self.queryset= models.Worker.objects.all()
                self.chosen_object=self.model.objects.get(pk=worker.pk)
                self.update_form=forms.WorkerForm(instance=self.chosen_object)

        return render(self.request,'restaurant_admin/WorkerHomedetail.html',context={'object_list':self.queryset,
                                                                                      'chosen_object': self.chosen_object,
                                                                                      'update_form': self.update_form})

@method_decorator(login_required, name='dispatch')
class WorkerDeleteView(DeleteView):
    #template_name = 'restaurant_admin/Workerdelete.html'
    model = models.Worker
    fields = '__all__'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_success_url(self):
        return reverse('restaurant_admin:WorkerHome_detail')

@method_decorator(login_required, name='dispatch')
class WorkerListView(ListView):
    template_name = 'restaurant_admin/Workerlist.html'
    model = models.Worker
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class TableCreateView(CreateView):
    template_name = 'restaurant_admin/Tablecreate.html'
    model = models.Table
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class TableDetailView(DetailView):
    template_name = 'restaurant_admin/Tabledetail.html'
    model = models.Table
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class TableHomeDetailView(FormView, ListView):
    template_name = 'restaurant_admin/TableHomedetail.html'
    form_class = forms.InputForm
    model = models.Table
    fields='__all__'

@method_decorator(login_required, name='dispatch')
class TableDeleteView(DeleteView):
    #template_name = 'restaurant_admin/Tabledelete.html'
    model = models.Table
    fields = '__all__'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_success_url(self):
        return reverse('restaurant_admin:TableHome_detail')


@method_decorator(login_required, name='dispatch')
class TableListView(ListView):
    template_name = 'restaurant_admin/Tablelist.html'
    model = models.Table
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class CostCreateView(CreateView):
    template_name = 'restaurant_admin/Costcreate.html'
    model = models.Cost
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class CostUpdateView(UpdateView):
    template_name = 'restaurant_admin/Costupdate.html'
    model = models.Cost
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class CostDetailView(DetailView):
    template_name = 'restaurant_admin/Costdetail.html'
    model = models.Cost
    fields = '__all__'


@method_decorator(login_required, name='dispatch')
class CostHomeDetailView(FormView, ListView):
    template_name = 'restaurant_admin/CostHomedetail.html'
    form_class = forms.InputForm
    model = models.Cost
    fields='__all__'

@method_decorator(login_required, name='dispatch')
class CostDeleteView(DeleteView):
    template_name = 'restaurant_admin/Costdelete.html'
    model = models.Cost
    fields = '__all__'

    def get_success_url(self):
        return reverse('restaurant_admin:CostHome_detail')

@method_decorator(login_required, name='dispatch')
class CostListView(ListView):
    template_name = 'restaurant_admin/Costlist.html'
    model = models.Cost
    fields = '__all__'
