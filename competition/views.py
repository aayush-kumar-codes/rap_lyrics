from django.shortcuts import render


def list_all_competition(request):
    return render(request=request, template_name='competition/competition.html')
