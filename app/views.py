from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from datetime import datetime, timedelta
from django.utils.timezone import utc
from django.core.mail import send_mail, BadHeaderError
from django.core.servers.basehttp import FileWrapper






# Create your views here.
def landingpage(request):
	context = RequestContext(request)

	return render_to_response('index.html', {}, context_instance=context)

def howitworks(request):
	context = RequestContext(request)

	return render_to_response('howitworks.html', {}, context_instance=context)



def save_user(request):
	context = RequestContext(request)
	registerd=False
	if request.method=='POST':
		form= add_new_user(data=request.POST)
		if form.is_valid():
			user=form.save()
			user.set_password(user.password)
			user.save()
			registerd=True


		else:
			print "Error"

	return render_to_response('home.html', {}, context_instance=context)

def loginuser(request):
	context=RequestContext(request)
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		print username, password
		user= authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/home/')
			else:
				return HttpResponseRedirect('/')
		else:
			print "Ivalid username password"

	return render_to_response('home.html', {}, context_instance=context)
