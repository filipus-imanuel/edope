from django.shortcuts import render
from django.utils.html import mark_safe
# Create your views here.

def welcome(request, extra_context={}):
	var_halo = "Nama Saya: "+str(request.user.is_authenticated)

	extra_context.update({
		'halo': var_halo,
	})
	return render(request, "welcome.html", extra_context)