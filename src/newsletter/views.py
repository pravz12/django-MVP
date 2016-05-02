from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import SignUpForm, ContactForm
from .models import SignUp

# Create your views here.
def home(request):
	title = "SignUp Now"

	form = SignUpForm(request.POST)
	#if request.user.is_authenticated ():
		#title = "MyTitle %s" %(request.user)

	#if request.method =="POST":
		#print request.POST
	context = {
		"title" : title,
		"form" : form
	}
	   
	if form.is_valid():
		#form.save()
		#print request.POST['email'] #not recommended
		instance = form.save(commit=False)

		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "Random"
		instance.full_name = full_name
		#if not instance.full_name:
			#nstance.full_name = ""unknown"
		instance.save()
		#print instance.email 
		#print instance.timestamp
		context ={
			"title" :"Thank you"
		}
	if request.user.is_authenticated() and request.user.is_staff:
		#print (SignUp.objects.all())
		#i = 1
		#for instance in SignUp.objects.all():
			#print i
			#print (instance.full_name)
			#i+=1
		queryset = SignUp.objects.all().order_by('-timestamp')

		context ={
			"queryset" : queryset
		}

	return render(request, "home.html", context)
 

def contact(request): 
	title = "Contact Us"
	form = ContactForm(request.POST)
	if form.is_valid():
		#for key,value in form.cleaned_data.iteritems():
			#print key, value
			#print form.cleaned_data.get(key)
		form_email = form.cleaned_data.get("email")
		form_full_name = form.cleaned_data.get("full_name")
		form_message = form.cleaned_data.get("message")
		#print email, full_name, message
		subject = 'Site_Contact_Form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'praveen.praxis12@gmail.com']
		contact_message = "%s: %s via %s" %(
				form_full_name, 
				form_message, 
				form_email)

		some_html_message = """

		<h1> hello send_mail</h1>
		"""
		

		send_mail(subject,
				contact_message,
				from_email,
				to_email,
				html_message = some_html_message,
				fail_silently = True)
	

	context = {
		"form" : form,
		"title":title
	}

	return render(request, "forms.html", context)


 