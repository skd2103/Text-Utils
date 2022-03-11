# this file created by sanjay
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

    # Analyzed the text
def analyzer(request):
    # Get the text
    dj_text=request.POST.get('text', "default")

    check_remove_punc=request.POST.get('removepunc', 'Off')
    check_upper_case=request.POST.get('fullcap', 'off')
    check_new_line_remover=request.POST.get('newlineremover', 'off')
    extra_space_remover=request.POST.get('extraspaceremover', 'off')
    count_all_character=request.POST.get('countallcharacter', 'off')

    if (check_remove_punc == "on"):
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in dj_text:
            if char not in punctuation:
                analyzed=analyzed+char
        params={'purpose':'Remove Punctuation', 'analyzed_text':analyzed}
        dj_text = analyzed

    if (check_upper_case == 'on'):
        analyzed=""
        for char in dj_text:
            analyzed=analyzed + char.upper()
        params = {'purpose': 'Change To UpperCase', 'analyzed_text': analyzed}
        dj_text = analyzed

    if(check_new_line_remover =="on"):
        analyzed=""
        for char in dj_text:
            if char != '\n' and char!= '\r':
                analyzed=analyzed+char
        params = {'purpose': 'Remove NewLines', 'analyzed_text': analyzed}
        dj_text = analyzed

    if(extra_space_remover=='on'):
        analyzed=" "
        length=len(dj_text)
        for index, char in enumerate(dj_text):
            if not (dj_text[index]==" " and dj_text[index+1]==" "):
                analyzed=analyzed+char
        params = {'purpose': 'Remove Extra Space', 'analyzed_text': analyzed}
        dj_text = analyzed

    if(count_all_character=='on'):
        count=0
        for char in dj_text:
            count = count + 1
        analyzed= f"{dj_text}  '\n' Total number of character you are entered in text area :-{count}"
        params = {'purpose': 'Count All Character', 'analyzed_text': analyzed}

    if(check_remove_punc != "on" and check_upper_case != 'on' and check_new_line_remover !="on" and extra_space_remover !='on' and count_all_character !='on'):
        return HttpResponse("Please select some opretion with text")
    return render(request, 'analyze.html', params)

# def cap_first(response):
#     return HttpResponse("Capitalize First")
#
# def new_line_remove(response):
#     return HttpResponse("New Line Remove")
#
# def space_remove(response):
#     return HttpResponse("Space Remove <a href='/'> Back </a>")
#
# def char_count(response):
#     return HttpResponse("Character Count")

# def home(response):
#     return HttpResponse(''' Home
#     <a href="http://127.0.0.1:8000/about"> <button> Visit About us </button> </a>
#     <a href="http://127.0.0.1:8000/removepunc"> <input type="button" value="Remove Punctuation"/> </a>
#     <a href="http://127.0.0.1:8000/capitalizefirst"> <input type="button" value="Capitalize First"/> </a>
#     <a href="http://127.0.0.1:8000/newlineremove"> <input type="button" value="New Line Remove"/> </a>
#     <a href="http://127.0.0.1:8000/spaceremove"> <input type="button" value="Space Remove"/> </a>
#     <a href="http://127.0.0.1:8000/charcount"> <input type="button" value="Character Count"/> </a>
#     ''')
# def about(response):
#     return HttpResponse("Hello TextUtils Thos is About Page")
#
# def filedata(response):
#     return HttpResponse("get_file_data")
#
# def myurls(response):
#     return HttpResponse('''<a href="https://www.sanjaytechtalk.com/"> Sanjay Techtalk </a>''')