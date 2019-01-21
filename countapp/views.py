from django.shortcuts import render
import collections

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    text_list = text.split()
    text_dic = {}

    for word in text_list:
        if word in text_dic:
            text_dic[word] += 1
        else:
            text_dic[word] = 1

    sort_dic = collections.OrderedDict(sorted(text_dic.items()))

    return render(request, 'result.html',{
        'fulltext':text,
        'length':len(text_list),
        'dictionary' : text_dic.items(),
        'sort_dic' : sort_dic.items()
        })