#created by Saurabh Zingade

from django.http import HttpResponse
from django.shortcuts import render

'''
def index(request):
    return HttpResponse("Hello Zincsy")

def about(request):
    return HttpResponse("Hello About")'''

# def nav(request):
#     return HttpResponse('''<h1><a href="https://www.google.com">Click for google</a></h1>''')

def index(request):
    params={'Name':'Saurabh','Place':'PUNE'}
    return render(request,'index.html',params)
    #return HttpResponse("Home")

def analyze(request):
    djtext = request.POST.get('text','default')


    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    spaceremove = request.POST.get('spaceremove','off')
    charactercounter=request.POST.get('charactercounter','off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''


    if(removepunc=="on"):
        anayzed=""
        for char in djtext:
            if char not in punctuations:
                anayzed = anayzed+char

        params={'purpose':"Remove punctuations",
                'analyzed_text':anayzed}
        djtext=anayzed
        #return render(request,'analyze.html',params)
    if(fullcaps=="on"):
        anayzed = ""
        for char in djtext:
            anayzed =anayzed+char.upper()
        params = {'purpose': "Changed to uppertext",
                  'analyzed_text': anayzed}
        djtext=anayzed
        #return render(request, 'analyze.html', params)
    if(newlineremover=="on"):
        anayzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                anayzed=anayzed + char
        params = {'purpose': "Removed New line",
                  'analyzed_text': anayzed}
        djtext = anayzed
        #return render(request, 'analyze.html', params)
    if(spaceremove=="on"):
        anayzed = ""
        for index,char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1]==" ":
                pass
            else:
                anayzed = anayzed + char
        params = {'purpose': "Removed The space",
                  'analyzed_text': anayzed}
        djtext=anayzed
        #return render(request, 'analyze.html', params)
    elif(charactercounter=="on"):
        char_count=0
        for i in djtext:
            if i!=" ":
                char_count+=1
        params = {'purpose': "Character Counter",
                  'analyzed_text':anayzed+ "Number of characters is "+str(char_count)}

        #return render(request, 'analyze.html', params)
    if(removepunc!="on" and newlineremover!="on" and fullcaps!="on" and spaceremove!="on" and charactercounter!="on" ):
        return HttpResponse("No option selected")

    return render(request, 'analyze.html', params)

# def removePunc(request):
#     #get the text and analysis
#     djtext = request.GET.get('text','default')
#     print(djtext)
#     return HttpResponse("Remove punc")

# def capfirst(request):
#     return HttpResponse("Capitalize")
#
# def newlineremove(request):
#     return HttpResponse("Capitalize")
#
# def spaceremove(request):
#     return HttpResponse("Space Remove <a href='/'>Click here to go to Index</a>")
#
# def charcount(request):
#     return HttpResponse("Character counter")

