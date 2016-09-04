from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from datetime import datetime, timedelta
from django.utils.timezone import utc
from django.core.mail import send_mail, BadHeaderError
from django.core.servers.basehttp import FileWrapper
from reportlab.graphics.barcode import code39, code128, code93
from reportlab.graphics.barcode import eanbc, qr, usps
from reportlab.graphics.shapes import Drawing
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF
from django.contrib import messages
from app.models import *
from app.forms import *
from django.contrib.auth import authenticate, login
from django.http import *
from cart.cart import Cart
import  requests
import pesapal
import random
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from io import BytesIO


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
def remove_from_cart(request, event_id):
	product = Event.objects.get(id=event_id)
	print product
	cart = Cart(request)
	cart.remove(product)


def get_cart(request):
	context = RequestContext(request)

	return render_to_response('cart.html', dict(cart=Cart(request)), context_instance=context)

def request_payment(request):
	context = RequestContext(request)
	if request.method == 'POST':
		amount = request.POST['amount']
		client = pesapal.PesaPal(consumer_key, consumer_secret, True)
		request_data = {
			'Amount': str(1000),
			'Description': 'Purchase of tickets from karibupay',
			'Type': 'MERCHANT',
			'Reference': str(datetime.now()),
			'Email': 'nguruben@gmail.com'
		}
		post_params = {
			'oauth_callback': 'http://f79cbce8.ngrok.io/process_orders'
		}
		pesapal_request = client.postDirectOrder(post_params, request_data)

	return  render_to_response('pay.html',{'iframe_url': pesapal_request.to_url()}, context_instance=context)
def process_order(request):
	date = datetime.now()
	if not request.user.is_authenticated:
		return render(request, 'myapp/login_error.html')
	else:
		print request.user
	tracking_id = request.GET.get('pesapal_transaction_tracking_id', '')
	reference = request.GET.get('pesapal_merchant_reference', '')
	errors = ''
	msg = ''
	if tracking_id and reference:
		params = {
                    'pesapal_merchant_reference': reference,
                    'pesapal_transaction_tracking_id': tracking_id
                 }
		client = pesapal.PesaPal(consumer_key, consumer_secret, True)
		pesapal_request = client.queryPaymentStatus(params)
		url = pesapal_request.to_url()
		#print url
		pesapal_response = requests.get(url)
		pesapal_response_data = pesapal_response.text
		#print pesapal_response_data
		pesapal_status = pesapal_response_data.split('=')[1]
		#email = request.user
		#email = email.email
		confirmation_code=random.randint(1, 1000)
		if pesapal_status == 'COMPLETED':
			response = HttpResponse(content_type='application/pdf')
			response['Content-Disposition'] = 'inline; filename="barcode.pdf"'
			buffer = BytesIO()
			p = canvas.Canvas(buffer)
			p.setLineWidth(.3)
			p.setFont('Helvetica', 12)
			p.drawString(30, 750, 'KaribuPay Ticket')
			p.drawString(30, 735, 'Event Ticket')
			p.drawString(350, 750, str(date))
			barcode = code39.Extended39(str(confirmation_code), barWidth=0.5 * mm, barHeight=20 * mm)
			barcode.drawOn(p, 30, 600)
			p.showPage()
			p.save()
			pdf = buffer.getvalue()
			buffer.close()
			response.write(pdf)
			print confirmation_code

			msg = 'Transaction was successful'
			print 'Transaction was successful'
		else:
			msg = 'Transaction status is %s'%(pesapal_status)
			print 'Transaction status is %s'%(pesapal_status)
		p_ref = Pesapal(tracking_id=tracking_id, reference=reference, status=pesapal_status)
		#p_ref.save()
	else:
		errors ='Please Try again'
	return response


	#return render_to_response('process_pay.html', {'errors': errors, 'msg': msg, 'a':a}, context_instance=RequestContext(request))
def barcode(request):
	date=datetime.now()
	print date
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'inline; filename="barcode.pdf"'
	buffer = BytesIO()
	p = canvas.Canvas(buffer)
	p.setLineWidth(.3)
	p.setFont('Helvetica', 12)
	p.drawString(30, 750, 'KaribuPay Ticket')
	p.drawString(30, 735, 'Event Ticket')
	p.drawString(350, 750, str(date))
	barcode = code39.Extended39("123456789", barWidth=0.5 * mm, barHeight=20 * mm)
	barcode.drawOn(p, 30 , 600 )
	p.showPage()
	p.save()
	pdf = buffer.getvalue()
	buffer.close()
	response.write(pdf)
	return response
