from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


def random(request):
    
    if not "attempts" in request.session:
        request.session['attempts'] = 0
    
    else:
        
        request.session['attempts'] += 1



    content = {
        'ranwords': get_random_string(length=32)
    }
    return render(request, 'random_word/random.html', content)

    
def generate(request):
    print 'hello'
    request.session['attempts'] = 1
    return redirect ("/")

def reset(request):
    request.session.clear()
    return redirect("/random_word")