from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from django.urls import reverse_lazy
from .form import ContactForm
from .models import Post
from django.contrib import messages
from django.core.mail import EmailMessage

class IndexView(TemplateView):
    template_name = 'index.html'
    
    
    
class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('scheduleapp:contact')
    
    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']

        subject = 'お問い合わせ: {}'.format(title)
        
        message = \
            '送信者名: {0}\nメールアドレス: {1}\n タイトル:{2}\n メッセージ:\n{3}' \
            .format(name, email, title, message)
            
        from_email = 'toru6187@gmail.com'
        to_list = ['toru6187@gmail.com']
        
        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list,)
        
        message.send()
        messages.success(self.request, 'お問い合わせ送信完了')
        return super().form_valid(form)
    
class PostView(FormView):
    form_class = Post
    template_name = "post.html"
    
    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)
