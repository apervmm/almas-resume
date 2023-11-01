from django.contrib.auth.models import User

def context(request):
    return {"me": User.objects.first()}