from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic import ListView,DeleteView,UpdateView
from .models import StudData
from .forms import form

# Create your views here.

'''class dataform(CreateView,SuccessMessageMixin):
    model = StudData
    fields = "__all__"
    template_name = "stud.html"
    success_url = "/suc/"
    success_message = "Jai tara"'''


class DataDeleteView(DeleteView,SuccessMessageMixin):
    model = StudData
    success_url = "/kaka/"
    template_name = "delete.html"

    context_object_name = "form"








'''class DataFilterView(ListView):
    template_name = "list.html"
    context_object_name = "kaka"
    model = StudData
    def get_queryset(self):
        qs=super().get_queryset()
        return qs.filter(roll=self.request.GET['kaka'])'''



class NameFilterView(ListView):
    template_name = "list.html"
    model = StudData
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        self.rll=self.request.GET["name"]
        context['q']=StudData.objects.filter(name=self.rll)
        return context

def DatafilterView(request):



    r=request.GET['kaka']
    qs=StudData.objects.filter(roll=r)
    context={"q":qs}
    return render(request,"list.html",context)


class DataListView(ListView):
    template_name = "list.html"
    context_object_name = "q"
    model = StudData
    queryset = StudData.objects.all()
    ordering = ["roll"]



class DataUpdateView(UpdateView):
    success_url = "/kaka/"
    template_name = "update.html"
    model = StudData
    fields = "__all__"


class DataForm(View):

    form_class =form


    def get(self,request):

        return render(request,"stud.html",{"form":form})

    def post(self,request):

        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Submitted")

            return redirect("/")










