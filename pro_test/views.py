from django.shortcuts import render

person = [
    {
        'name':'tuyisabe pacifique',
        'status':'married',
        'career':'programmer',
        'location':'kimihurura'
    },
    {
        'name':'Muzehe kai',
        'status':'single',
        'career':'accountant',
        'location':'kicukiro'
    }
]
    
def fortest(request):
    contex = {
        'person': person
    }

    return render(request, 'test1.html', contex)
