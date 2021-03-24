from django.shortcuts import render


def requirement(request):

    return render(request, 'br/requirement/edit.html')
