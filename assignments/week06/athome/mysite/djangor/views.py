from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.models import entries



def doLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            url = reverse('add', args=[pk, ])

        else:
            messages.add_message(request, messages.INFO,
                                 "Oops! Invalid credentials - Please enter username and password")
            url = reverse('login')
    else:
        messages.add_message(request, messages.INFO,
                                 "Oops! Invalid credentials - Please enter username and password")
        url = reverse('login')
        
    return HttpResponseRedirect(url)