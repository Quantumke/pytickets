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
def homepage(request):
	context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
	header_events1=Event.objects.latest('id')
	f1l1= header_events1.title
	id=header_events1.pk
	f1l1= list(f1l1)
	f1l1= f1l1[0]

	header_events2=Event.objects.get(id=id-1)
	f2l1= header_events2.title
	f2l1= list(f2l1)
	f2l1= f2l1[0]

	header_events3=Event.objects.get(id=id-2)
	f3l1= header_events3.title
	f3l1= list(f3l1)
	f3l1= f3l1[0]
	header_events4=Event.objects.get(id=id-3)
	f4l1= header_events4.title
	f4l1= list(f4l1)
	f4l1= f4l1[0]
	upcomming_events=Event.objects.filter(featured=True)[:4]
	featured_upcomming=Event.objects.filter(featured=True)[:4]
	leisure_events=Event.objects.filter(category=1)
	cultural_events=Event.objects.filter(category=2)
	balls=Event.objects.filter(category=3)
	awards_and_gallas=Event.objects.filter(category=4)

	return render_to_response('home.html',{
		'header_events1':header_events1,
		'f1l1':f1l1,
		'header_events2':header_events2,
		'f2l1':f2l1,
		'header_events3':header_events3,
		'f3l1':f3l1,
		'header_events4':header_events4,
		'f4l1':f4l1,
		'upcomming_events':upcomming_events,
		'featured_upcomming':featured_upcomming,
		'leisure_events':leisure_events,
		'cultural_events':cultural_events,
		'balls':balls,
		'awards_and_gallas':awards_and_gallas,




		}, context_instance=context)

def view_more(request, slug):
	header_events1=Event.objects.latest('id')
	f1l1= header_events1.title
	id=header_events1.pk
	f1l1= list(f1l1)
	f1l1= f1l1[0]

	header_events2=Event.objects.get(id=id-1)
	f2l1= header_events2.title
	f2l1= list(f2l1)
	f2l1= f2l1[0]

	header_events3=Event.objects.get(id=id-2)
	f3l1= header_events3.title
	f3l1= list(f3l1)
	f3l1= f3l1[0]
	header_events4=Event.objects.get(id=id-3)
	f4l1= header_events4.title
	f4l1= list(f4l1)
	f4l1= f4l1[0]
	current_obj=Event.objects.get(slug=slug)
	title=current_obj.title
	title=list(title)
	title= title[0]
	suggestion=Event.objects.all()[:4]
	now = datetime.now().date()
	event_date=current_obj.event_date
	hours= now-event_date
	a= hours.total_seconds()
	b= a/3600
	days= b/24
	days=int(days)
	days=days * -1
	sec= a * -1




	return render_to_response('single-event.html',{
	'object':get_object_or_404(Event, slug=slug),

		'header_events1':header_events1,
		'f1l1':f1l1,
		'header_events2':header_events2,
		'f2l1':f2l1,
		'header_events3':header_events3,
		'f3l1':f3l1,
		'header_events4':header_events4,
		'f4l1':f4l1,
		'title':title,
		'suggestion':suggestion,
		'days':days,
		'sec':sec,

	},RequestContext(request))

def add_to_cart(request):
	context=RequestContext(request)
	if request.method=='POST':
		select_event=request.POST['select_event']
		quantity=request.POST['quantity']
		eventid=request.POST['eventid']
		price=request.POST['price']
		product=Event.objects.get(id=eventid)
		total_price= int(quantity) * int(price)
		cart=Cart(request)
		cart.add(product, price, quantity)
		email = request.user
		email= email.email
		return HttpResponseRedirect('/checkout')




	return render_to_response('single-event.html',{}, context_instance=context)
