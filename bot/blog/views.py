from django.shortcuts import render

from .models import Event, IntroQuestion

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def event_list(request):
	events = Event.objects.all()
	return render(request, 'blog/index.html', context={'events': events})


def events_add_query(request):
	re = Event(text=request.POST["text_event"], body=request.POST["body_event"], post_date=request.POST["date_event"])
	re.save()
	return HttpResponseRedirect(reverse('events_page'))


def events_page(request):
	return render(request, 'blog/events_add.html')


def events_delete(request):
	event = Event.objects.get(text=request.POST["text_event"], post_date=request.POST["date_event"])
	event.delete()
	return HttpResponseRedirect(reverse('event_list_url'))

def events_delete_page(request):
	return render(request, 'blog/event_list_url.html')


def intro_question_list(request):
	questions = IntroQuestion.objects.all()
	return render(request, 'blog/question_list.html', context={'questions': questions})


def intro_add_query(request):
	re = IntroQuestion(text=request.POST["text_question"])
	re.save()
	return HttpResponseRedirect(reverse('intro_page'))


def intro_page(request):
	return render(request, 'blog/intro_add.html')