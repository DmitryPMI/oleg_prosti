from django.urls import path

from .views import *

urlpatterns = [
	path('', event_list, name='event_list_url'),
	path('add', events_page, name='events_page'),
	path('add_query', events_add_query, name='events_add'),
	path('intro', intro_question_list, name='intro_question_list_url'),
	path('intro_add', intro_page, name='intro_page'),
	path('intro_add_query', intro_add_query, name='intro_add')
]