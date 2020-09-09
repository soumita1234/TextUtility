# I have created this file

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')

    # checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')
    print(removepunc)
    print(djtext)

    # check with checkbox is on
    # punctuation removal function
    if removepunc == "on":
        # analyzed = djtext
        punctuations = '''!()-{}[];:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed


    # capitalization function
    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed


    # newline remover function
    if (newlineremove == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
               analyzed = analyzed + char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed

    # extra space remover
    if extraspaceremove == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra Space', 'analyzed_text': analyzed}
        djtext = analyzed

    # character count
    if (charcount == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if len(djtext) > 0:
                analyzed = len(djtext)
        params = {'purpose': 'Character Counter', 'analyzed_text': analyzed}



    if(removepunc != "on" and fullcaps != "on" and newlineremove != "on" and extraspaceremove != "on" and charcount != "on"):
        return HttpResponse("Error! Select Any Option.")

    #return
    return render(request, 'analyze.html', params)
