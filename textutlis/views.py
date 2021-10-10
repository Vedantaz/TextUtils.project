
# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request,"about.html" )



def analyze(request):
    djtext = request.POST.get('text', 'default')

                                                # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

                                                 #Check which checkbox is on
    if (removepunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char  
        
        params = {'purpose': 'Removed Extraspaces', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")
    

    return render(request, 'analyze.html', params)

    # if (removepunc == "on" and newlineremover =="on"):
    #     punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    #     analyzed=""
    #     for char in djtext:
    #         if char != "\n" and char!="\r" and char not in punctuations:
    #             analyzed=analyzed + char
                
    #     params = {'purpose': 'Removed punctuations and Removed NewLines', 'analyzed_text': analyzed}

    # if (removepunc == "on" and extraspaceremover =="on"):
    #         punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    #         analyzed=""
    #         for index,char in enumerate(djtext):
    #           if char not in(djtext[index] == " " and djtext[index+1]==" ") and char not in punctuations  :
    #             analyzed=analyzed + char
                
    #         params = {'purpose': 'Removed punctuations and Removed Extraspaces', 'analyzed_text': analyzed}

    # if (removepunc == "on" and fullcaps =="on"):
    #         punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    #         analyzed=""
    #         for char in djtext:
    #           if char not in punctuations :
    #             analyzed=analyzed + char.upper()
                
    #         params = {'purpose': 'Removed punctuations and Removed NewLines', 'analyzed_text': analyzed}

    # if (fullcaps == "on" and extraspaceremover =="on"):
    #         analyzed=""
    #         for index,char in enumerate(djtext):
    #           if char != "\n" and char!="\r" and  not(djtext[index] == " " and djtext[index+1]==" "):
    #             analyzed=analyzed + char.upper()
                
    #         params = {'purpose': 'Removed punctuations and Removed NewLines', 'analyzed_text': analyzed}

    # if (fullcaps == "on" and newlineremover =="on"):
    #         analyzed=""
    #         for index,char in enumerate(djtext):
    #           if char != "\n" and char!="\r" :
    #             analyzed=analyzed + char.upper()
                
    #         params = {'purpose': 'Removed punctuations and Removed NewLines', 'analyzed_text': analyzed}


    # if (extraspaceremover == "on" and newlineremover =="on"):
    #         analyzed=""
    #         for index,char in enumerate(djtext):
    #           if char != "\n" and char!="\r" and  not(djtext[index] == " " and djtext[index+1]==" ") :
    #             analyzed=analyzed + char
                
    #         params = {'purpose': 'Removed punctuations and Removed NewLines', 'analyzed_text': analyzed}













def ex1(request):
    s=''' <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>iMPORTANT LINKS AND SOMETHING BONUSES...</title>
</head>
<body>
<div class="container">
        <nav class="navbar" style="       align-items: center;
        display: flex;
        justify-content: center;
        font-size: 22px;
        color: orangered;
        background-color: aqua;
        height: 53px;">
        <h1>Navigations to the Free-Resource :)> </h1>
        </nav>
        <div class="healthylinks" style="    height: 485px;
    background-color: antiquewhite;
    display: flex;
    align-items: center;">
        <h1 style=" 
          height: 205px;
    width: 659px;
    padding: 26px;
    padding-top: 144px;
    border: 2px solid black;
">Best free resources for learning of Modern: Web & Superb Technologies-> 
        <a href="https://www.w3schools.com/" style="   display: flex;
        justify-content: center;
        color: #0af60a;
        padding: 25px;
        font-size: 19px;">W3 schools</a></h1>
        <h1 style=" 
            height: 205px;
    width: 659px;
    padding: 26px;
    padding-top: 144px;
    border: 2px solid black;">Get to learn Web, Mobile dev,Javascripts else:IN VIDEO TUTORIAL FOR FREE ->
        <a href="https://www.codewithharry.com/" style="    display: flex;
        justify-content: center;    color: red;
        font-size: 22px; padding: 25px;
       ">CodeWithHarry</a></h1>
        <h1 style=" 
          height: 205px;
    width: 659px;
    padding: 26px;
    padding-top: 144px;
    border: 2px solid black;">To get to know about cloud services , Create a free account and explore here ->
    <a href="https://aws.amazon.com/free/?trk=ps_a134p000003yhlXAAQ&trkCampaign=acq_paid_search_brand&sc_channel=ps&sc_campaign=acquisition_IN&sc_publisher=google&sc_category=core-main&sc_country=IN&sc_geo=APAC&sc_outcome=Acquisition&sc_detail=aws&sc_content=Brand_Core_aws_e&sc_matchtype=e&sc_segment=453325184782&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Core-Main|Core|IN|EN|Text&s_kwcid=AL!4422!3!453325184782!e!!g!!aws&ef_id=CjwKCAjwtfqKBhBoEiwAZuesiNxORJZwJShUX7gS6rQNa0-MxICz7dp1QTBBv3f-H1yrCSXuoqUiixoC1iYQAvD_BwE:G:s&s_kwcid=AL!4422!3!453325184782!e!!g!!aws&all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all" style="    display: flex;
        justify-content: center; color: blue;
        font-size: 21px;  padding: 25px;
        ">AWS services- Try for free</a></h1>
    </div>
        </div>
    </body>
    </html>
'''
    return HttpResponse(s)