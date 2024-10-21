import random
import urllib.request

from django.shortcuts import render

# Create your views here.
def home_view(request):
    number = random.randint(6, 13)
    some_list = [
      random.randint(1, 100),
      random.randint(1, 100),
      random.randint(1, 100),
    ]
    context = {
      'your_number': number,
      'bool_item': True,
      'some_list': some_list,
      'some_dict': {'A': 1, 'B': 2, 'C': 3}
    }
    return render(request, 'myapp/index.html', context)


def about_view(request):
    mytech = [
        {
          'name': 'HTML',
          'url': 'https://www.w3schools.com/html/',
          'level': 'beginner'
        },
        {
          'name': 'CSS',
          'url': 'https://www.w3schools.com/css/',
          'level': 'beginner'
        },
        {
          'name': 'Bootstrap',
          'url': 'https://getbootstrap.com',
          'level': 'beginner'
        },
        {
          'name': 'Python',
          'url': 'https://www.python.org',
          'level': 'intermediate'
        },
        {
          'name': 'Django',
          'url': 'https://www.djangoproject.com',
          'level': 'beginner'      
        },    
    ]
    context = {
        'lucky_number': random.randint(1, 10),
        'unlucky_number': random.randint(1, 10),
        'mytech': mytech, 
    }
    return render(request, 'myapp/about.html', context)


def contact_view(request):
    return render(request, 'myapp/contact.html')


def genbank_view(request):
    URL = 'ftp://ftp.ncbi.nlm.nih.gov/genbank/README.genbank'
    response = urllib.request.urlopen(URL)
    context = {}
    for line in response:
        line = line.decode('utf-8').strip()
        if line.startswith('GenBank Flat File Release'):
            context['version'] = line.split()[-1]
        elif line.startswith('Target Release Date'):
            context['date'] = line.split(':')[-1]
            break
    return render(request, 'myapp/genbank.html', context)