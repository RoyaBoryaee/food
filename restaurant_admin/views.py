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


class SpecialView(View):

    def get(self,*args,**kwargs):

        self.queryset=self.model.objects.all()
        return render(self.request, self.template_name,context={'object_list':self.queryset,
                                                             'chosen_object': self.chosen_object,
                                                             'update_form': self.update_form,
                                                             'create_form':self.create_form,
                                                             'create_bool':self.create_bool})
    def post(self,*args,**kwargs):
        postvalues = self.request.POST
        print('post values {}'.format(postvalues))
        if postvalues.get('id', None):
            print('id')
            id = self.request.POST.get('id')
            self.chosen_object= self.model.objects.get(pk=id)

        if self.chosen_object != None:
            print('this')
            self.queryset=self.model.objects.all()
            self.update_form=self.form(instance=self.chosen_object)
            return render(self.request,self.template_name,context={'object_list':self.queryset,
                                                                    'chosen_object': self.chosen_object,
                                                                    'update_form': self.update_form})

        if postvalues.get('edit',None):
            print('yes')
            self.chosen_object=self.model.objects.get(pk=postvalues['pk'])
            self.update_form=self.form(self.request.POST,  self.request.FILES,instance=self.chosen_object)
            print(self.update_form)
            if self.update_form.is_valid():
                print('this')
                cost=self.update_form.save()
                cost.save()
                self.queryset= self.model.objects.all()
                #self.chosen_object=self.model.objects.get(pk=cost.pk)
                #self.update_form=self.form(instance=self.chosen_object)
                return render(self.request,self.template_name,context={'object_list':self.queryset,
                                                                       #'chosen_object': self.chosen_object,
                                                                       #'update_form': self.update_form
                                                                       })
            else:
                self.queryset= self.model.objects.all()
                return render(self.request,self.template_name,context={'object_list':self.queryset,
                                                                        'update_form':self.update_form,
                                                                        'chosen_object':self.chosen_object})

        if postvalues.get('create', None):
            self.create_bool=True
            self.create_form=self.form()
            self.queryset= self.model.objects.all()
            return render(self.request,self.template_name,context={'object_list':self.queryset,
                                                                    'create_form':self.create_form,
                                                                    'create_bool':self.create_bool})

        if postvalues.get('create_1',None):
            self.create_form=self.form(self.request.POST, self.request.FILES)
            print(self.create_form.errors)
            print('((((((()))))))')
            print(self.create_form)
            if self.create_form.is_valid():
                print('yes this is valid')
                cost= self.create_form.save()
                cost.save()
                self.queryset= self.model.objects.all()
                return render(self.request,self.template_name,context={'object_list':self.queryset})
            else:
                self.create_bool=True
                self.queryset= self.model.objects.all()

                return render(self.request,self.template_name,context={'object_list':self.queryset,'create_form':self.create_form,
                                                                        'create_bool':self.create_bool})



@method_decorator(login_required, name='dispatch')
class FoodCategoryDetailView(DetailView):
    template_name = 'restaurant_admin/FoodCategorydetail.html'
    model = models.FoodCategory
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class FoodCategoryHomeDetailView(SpecialView):
    template_name = 'restaurant_admin/FoodCategoryHomedetail.html'
    form=forms.FoodCategoryForm
    model = models.FoodCategory
    fields='__all__'
    create_form= None
    update_form= None
    chosen_object=None
    create_bool = False


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
class FoodDetailView(DetailView):
    template_name = 'restaurant_admin/Fooddetail.html'
    model = models.Food
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class FoodHomeDetailView(SpecialView):
    template_name = 'restaurant_admin/FoodHomedetail.html'
    form=forms.FoodForm
    model = models.Food
    fields='__all__'
    chosen_object=None
    update_form=None
    create_bool=False
    create_form=None


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
class WorkerDetailView(DetailView):
    template_name = 'restaurant_admin/Workerdetail.html'
    model = models.Worker
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class WorkerHomeDetailView(SpecialView):
    template_name = 'restaurant_admin/WorkerHomedetail.html'
    form=forms.WorkerForm
    model = models.Worker
    fields='__all__'
    chosen_object=None
    update_form=None
    create_bool=False
    create_form=None


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
class TableDetailView(DetailView):
    template_name = 'restaurant_admin/Tabledetail.html'
    model = models.Table
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class TableHomeDetailView(SpecialView):
    template_name = 'restaurant_admin/TableHomedetail.html'
    form= forms.TableForm
    model = models.Table
    fields='__all__'
    create_form=None
    create_bool = False
    update_form=None
    chosen_object=None

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
class CostDetailView(DetailView):
    template_name = 'restaurant_admin/Costdetail.html'
    model = models.Cost
    fields = '__all__'

@method_decorator(login_required, name='dispatch')

class CostHomeDetailView(SpecialView):
    template_name = 'restaurant_admin/CostHomedetail.html'
    form= forms.CostForm
    create_form= None
    update_form= None
    chosen_object=None
    create_bool = False
    model = models.Cost
    fields='__all__'

@method_decorator(login_required, name='dispatch')
class CostDeleteView(DeleteView):
    template_name = 'restaurant_admin/Costdelete.html'
    model = models.Cost
    fields = '__all__'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_success_url(self):
        return reverse('restaurant_admin:CostHome_detail')
