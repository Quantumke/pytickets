from adlink.models import *
from django.contrib.auth.models import User
class ActivateAccount():
	def run(data, email):
		#instance =User.objects.filter(id=id)
		User.objects.filter(email=email).update(is_active='TRUE')
		print(email)

