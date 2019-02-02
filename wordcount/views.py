from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter


def home(request):
    return render(request, "home.html")

def counts(request):
    fulltext = request.GET["fulltext"] #fulltext comes from the html after submitting
    wordlist = fulltext.split()
    words = []
    for word in wordlist:
        lowerword = word.lower()
        words.append(lowerword)
    words2 = Counter(words)
    mostfreq = words2.most_common(1)[0][0]



    return render(request, "counts.html", {"fulltext":fulltext, "count":len(wordlist), \
    "frequent":mostfreq})

def about(request):
    return render(request, "about.html")
