from django.shortcuts import  render

def base(request):
    if request.user.is_authenticated():
        return views.start(request)
    else:
        return render(request, 'login.html')