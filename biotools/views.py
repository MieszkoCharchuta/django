from django.shortcuts import render

def seqcontent_view(request):
    return render(request, 'biotools/seqcontent.html')
