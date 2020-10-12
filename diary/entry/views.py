from django.shortcuts import render,redirect
from entry.forms import EntryForm
from django.http import HttpResponse
from .models import entry
#home page form
def home(request):
	if request.method=="POST":
		entry=EntryForm(request.POST)
		if entry.is_valid():
			entry.save()
			return HttpResponse("success")
		
	else:
		entry=EntryForm()
		return render(request,"index.html",{'form':entry})
		
#displays all posts
def show(request):
	entries=entry.objects.all()
	context={'entries':entries}
	return render(request,"show.html",context)

#....def edit(request,id):
#	entries=entry.objects.get(id=id)
#	form=EntryForm(instance=entries)
#	context={'form':form}
#	return render(request,"edit.html",context)
#deletes posts	
def delete(request,id):
	entries=entry.objects.get(id=id)
	entries.delete()
	return redirect("/show/")
#updates posts
def edit(request,id):
	entries=entry.objects.get(id=id)
	form=EntryForm(instance=entries)
	context={'form':form}
	if request.method=='POST':
		form=EntryForm(request.POST,instance=entries)
		if form.is_valid():
			form.save()
			return redirect("/show/")
	return render(request,"edit.html",context)


	

	
		
		
		
	
	

# Create your views here.
