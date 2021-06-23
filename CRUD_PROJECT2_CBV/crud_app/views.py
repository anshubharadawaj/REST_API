from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from django.views.generic.base import TemplateView, RedirectView
from django.views import View
# Create your views here.


#this class will add and show all items
class UserAddandShow(TemplateView):
    template_name= 'crud_app/addandshow.html'

    def get_context_data(self, *args, **kwargs):
        context=super().get_context_data(**kwargs)
        fm = StudentRegistration()
        std = User.objects.all
        context ={'stu':std,'form':fm}
        return context

    def post(self,request):
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ps = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=ps)
            reg.save()
            return HttpResponseRedirect('/')

#this class will update and edit
class UserUpdateView(View):
    def get(self,request,id):
        std = User.objects.get(pk=id)
        fm = StudentRegistration(instance=std)
        return render(request, 'crud_app/updatestudent.html', {'form': fm})

    def post(self,request,id):
        std = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST,instance=std)
        if fm.is_valid():
            fm.save()
        # return render(request, 'crud_app/updatestudent.html', {'form': fm})
        return HttpResponseRedirect('/')




#this class is used to delete
class UserdeleteView(RedirectView):
    url = '/'

    def get_redirect_url(self, *args, **kwargs):
        del_id= kwargs['id']
        User.objects.get(pk=del_id).delete()
        context=super().get_redirect_url(*args, **kwargs)
        return context

