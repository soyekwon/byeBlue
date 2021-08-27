from django.shortcuts import render

def list(request):
    content = {}
    if request.session.get("name"):
        content['name'] = request.session["name"]

    return render(request, 'mbti/mbti_list.html', content)
