from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

# def imgflip(request):
#     response = request.get('https://api.imgflip.com/get_memes')
#     imgdata = response.json()
#     return render(request,'welcome.html',{
#         'data':imgdata['data']
#     })
def geo(request):
    from django.contrib.sites import requests
    response = request.get('http://freegeoip.net/json/')
    geodata = response.json()
    return render(request, 'welcome.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name']
    })

def api(requests):
    response = requests.get('https://api.imgflip.com/get_memes').json()['data']['memes']
    return render(requests, 'welcome.html', {'memes': response})
