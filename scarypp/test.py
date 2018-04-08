import urllib.response
import urllib.request
import urllib.error

def download(url) :
    print("download:", url)
    try:
        response = urllib.request.urlopen(url)
        hh = response.read()
    except urllib.error as e:
        print("download error:", e.reason)
        hh = None
    return hh