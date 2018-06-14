from django.shortcuts import render

# Create your views here.
def signup(request):
    if request.method == 'POST':
        print("huehue")
        return render(request, 'useraccounts/signup.html')
    else:
        return render(request, 'useraccounts/signup.html')
