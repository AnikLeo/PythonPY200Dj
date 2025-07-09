from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.views.generic import FormView, TemplateView
from .forms import ContactForm



class LandingView(FormView):
    template_name = 'landing/index.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        form_data = form.cleaned_data

        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')

        user_agent = self.request.META.get('HTTP_USER_AGENT')

        return JsonResponse({
        'form_data': form.cleaned_data,
        'ip_address': ip,
        'user_agent': user_agent })


# class ContactView(TemplateView):
#     template_name = 'landing/index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = ContactForm()
#         return context
#
#     def post(self, request, *args, **kwargs):
#         form = ContactForm(request.POST)
#
#         if form.is_valid():
#             return self.form_valid(form)
#         return self.form_invalid(form)
#
#     def form_valid(self, form):
#         client_ip = self.get_client_ip()
#         return JsonResponse({
#             'form_data': form.cleaned_data,
#             'ip_address': client_ip,
#             'user_agent': self.request.META.get('HTTP_USER_AGENT')
#
#
