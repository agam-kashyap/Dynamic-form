from django.shortcuts import render, redirect, get_object_or_404
from .models import Team
from .forms import TeamMaking
# from dynamic import forms
# Create your views here.

def create_team(request) :
    t = get_object_or_404(Team, pk=1)
    extra_member = get_members(request)    
    if request.method == 'POST':

        form = TeamMaking(request.POST or None, extra=extra_member)
        
        if form.is_valid():
            for n in form.extra_name():
                save_name(request,n)
            return redirect("create_team_success")

    return render("backend/templates/form.html", {'t' : t ,'form' : form})

def get_members(request):
    return 2
