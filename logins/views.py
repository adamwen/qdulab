# Create your views here.
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from logins.forms import UserForm, UserProfileForm


def user_login(request):

    def render_form(form, error=False):
        return render_to_response(
                'logins/login.html',
                {'login_form': form, 'error': error},
                context_instance=RequestContext(request))

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if not form.is_valid() and form.get_user() is None:
            return render_form(form, error=True)
        user = form.get_user()
        login(request, user)
        return redirect('index')

    return render_form(AuthenticationForm())

@login_required(login_url='/account/login')
def user_logout(request):
    logout(request)
    return redirect('index')


def user_register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('index')
    if request.method == 'POST':
        uf = UserForm(request.POST, prefix='user')
        upf = UserProfileForm(request.POST, prefix='userprofile')
        if uf.is_valid() and upf.is_valid():
            user = uf.save()
            userprofile = upf.save(commit=False)
            userprofile.user = user
            userprofile.save()
            return redirect('index')
    #HTTP GET METHOD
    uf = UserForm(prefix='user')
    upf = UserProfileForm(prefix='userprofile')
    #form.fields['email'].required = True
    var = {'user_form': uf, 'userprofile_form': upf}
    return render_to_response(
            'logins/register.html', var,
            context_instance=RequestContext(request))
