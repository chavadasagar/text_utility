from django.shortcuts import render
from django.http import HttpResponse
import string


def index(request):
    return render(request, "index.html")


def result(request):
    result = request.POST.get("text", default="Nothing")
    is_pun = request.POST.get("is_pun", default="off")
    is_upper = request.POST.get("is_upper", default="off")
    is_lower = request.POST.get("is_lower", default="off")

    ans = ""
    no_of_space = 0
    no_of_pun = 0
    no_of_upper = 0
    no_of_lower = 0

    # remove the puncation
    if is_pun == "on":
        for char in result:
            if char not in string.punctuation:
                ans += char

    # convert upper case
    if is_upper == "on":
        ans = result.upper()

    # convert lower case
    if is_lower == "on":
        ans = result.lower()

    # remove puncation ans convert uppercase
    if is_upper == "on" and is_pun == "on":
        for char in result:
            if char not in string.punctuation:
                ans += char.upper()

    # remove puncation ans convert lowercase
    if is_lower == "on" and is_pun == "on":
        for char in result:
            if char not in string.punctuation:
                ans += char.lower()

    # count space , puncation ,uppercase ,lowercase
    for char in result:
        if char in ' ':  # space
            no_of_space += 1
        if char.islower():  # lower
            no_of_lower += 1
        if char.isupper():  # upper
            no_of_upper += 1
    
    for char in result:
        if char in string.punctuation:
            no_of_pun += 1

    data = {
        "is_pun": is_pun,
        "is_lower": is_lower,
        "is_upper": is_upper,
        "ans": ans,
        "orignal_text": result,
        "no_of_space": no_of_space,
        "no_of_upper": no_of_upper,
        "no_of_lower": no_of_lower,
        "no_of_pun": no_of_pun,
        "length": len(result)
    }
    return render(request, "result.html", data)
