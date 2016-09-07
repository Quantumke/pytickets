from .logs import  *
class GetUserDetails():
	def run(request_user, request_profile, data):
		data['user_data']=GetUserDetails.user_data(request_user)
		data['profile_data']=GetUserDetails.get_profile_data(request_profile)
		#print(request_user, request_profile)
		logger.info("STEP 1: get form data-SUCCESS")

	def user_data(request_user):
		user_data={}
		user_data['username']=request_user.get('username')
		user_data['password']=request_user.get('password')
		user_data['email']=request_user.get('email')
		user_data['first_name']=request_user.get('first_name')
		user_data['last_name']=request_user.get('last_name')
		return user_data

	def get_profile_data(request_profile):
		profile_data={}
		profile_data['company']=request_profile.get('company')
		profile_data['email']=request_profile.get('email')
		profile_data['gender']=request_profile.get('gender')
		profile_data['dob']=request_profile.get('dob')
		profile_data['alt_email']=request_profile.get('alt_email')
		profile_data['phone']=request_profile.get('phone')
		profile_data['alt_phone']=request_profile.get('alt_phone')
		profile_data['rep_name']=request_profile.get('rep_name')
		profile_data['rep_number']=request_profile.get('rep_number')
		profile_data['rep_email']=request_profile.get('rep_email')
		return profile_data
