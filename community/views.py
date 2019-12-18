from django.shortcuts import render, get_object_or_404
from community.models import Agenda, Reply
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
 
# Create your views here.

def index(request):
    agenda_list = Agenda.objects.all().order_by('-pub_date')
    context = {'agenda_list': agenda_list}
    return render(request, 'community/index.html', context)

def detail(request, agenda_id):
    agenda = Agenda.objects.get(pk=agenda_id)
    reply = Reply.objects.filter(agenda=agenda_id)
    context = {'agenda': agenda, 'reply': reply}
    return render(request, 'community/detail.html', context)

def write(request):
    return render(request, 'community/write.html')

def submit(request):
    rows = Agenda.objects.order_by('pub_date').last()
    Agenda.objects.create(agenda_text = request.POST['title'], agenda_detail = request.POST['detail'] ,pub_date=datetime.datetime.now(), agenda_num=(rows.agenda_num)+1).save()
    return HttpResponseRedirect(reverse('community:index'))

def replysubmit(request, agenda_id):
    ob = Agenda.objects.get(agenda_num=agenda_id)
    Reply.objects.create(reply_text = request.POST['reply'], pub_date=datetime.datetime.now(), agenda=ob ).save
    return HttpResponseRedirect(reverse('community:detail', kwargs={'agenda_id':agenda_id}))