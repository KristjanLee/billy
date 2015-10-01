from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone

from .models import Message

def index(request):
    latest_message_list = Message.objects.order_by('-pub_date')[:5]
    context = {'latest_message_list': latest_message_list}

    try:
        name=request.POST['lname']
    except (KeyError, Message.DoesNotExist):
    	#print("except")
        # Redisplay the message voting form.
        return render(request, 'guestbook/index.html', {
            'error_message': "You didn't select a message.",
            'latest_message_list': latest_message_list, 
        })
    else:
        print("else")
        k = Message(name_text = name, message_text = request.POST['fname'], pub_date = timezone.now() )
        k.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return render(request, 'guestbook/index.html', context)

def detail(request, message_id):
    try:
        message = Message.objects.get(pk=message_id)
    except Message.DoesNotExist:
        raise Http404("Message does not exist")
    return render(request, 'guestbook/detail.html', {'message': message})


