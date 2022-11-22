from django.http import HttpResponse
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# Create your views here.
def home_view(request):
    return render(request,'index.html')

def convert_view(request):
    url = "https://open.spotify.com/playlist/5TvErm3igW1P9e3OqBkkSm"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # songs = soup.findAll("a", class_="EntityRowV2__AnchorLink-sc-ayafop-8 cGeiev", href=True)
    # artists = soup.findAll("span", class_="Type__StyledComponent-sc-1ell6iv-0 Mesto-sc-1e7huob-0 Row__Subtitle-sc-brbqzp-1 fGDcfx fMlCXO")

    html = soup.findAll("div", class_="Row__Container-sc-brbqzp-0 exvfxo")

    songs_html = []
    songs = []
    for text in html:
        songs_html.append(text)
    
    for song in songs_html:
        songs.append(song.get_text())
    return render(request, "converted.html", {'songs': songs})



