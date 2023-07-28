from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from core.forms import ContactForm
from django.contrib import messages
from django.views.generic import CreateView
from .models import Contact
from django.utils.translation import gettext_lazy as _
from core.tasks import export_data

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

# def contact(request):
#     form = ContactForm()
#     if request.method == 'POST':
#         form = ContactForm(data=request.POST)
#         if form.is_valid():
#             print('valid')
#             form.save()
#             messages.add_message(request, messages.SUCCESS, "Successfully sent")
#             return redirect(reverse_lazy('contact'))
#     context = {
#         'form' : form
#     }
#     return render(request, 'contact.html', context)


class ContactView(CreateView):
    template_name = 'contact.html'
    success_url = reverse_lazy('contact')
    form_class = ContactForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.add_message(self.request, messages.SUCCESS, _("Successfully sent"))
        return super().form_valid(form)
    

def export_view(request):
    export_data.delay()
    return HttpResponse('success')