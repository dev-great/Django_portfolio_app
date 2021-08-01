from django.shortcuts import render

from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'index.html', context)
