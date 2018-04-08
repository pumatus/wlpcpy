import itertools
import urllib.request
import urllib.error

def download(url, user_agent='wswp', num_retries=2):
    print("Download:", url)
    headers = {"User-agent": user_agent}
    request = urllib.request.Request(url, headers=headers)
    try:
        html = urllib.request.urlopen(request).read()
    except urllib.error.URLError as e:
        print("Download error:", e.reason)
        html = None

        if num_retries > 0:
            if hasattr(e, "code") and 500 <= e.code < 600:
                return download(url, user_agent, num_retries-1)


max_errors = 5
num_errors = 0
for page in itertools.count(1):
    url = 'http://example.webscraping.com/view/-%d' % page
    html = download(url)
    if html is None:
        num_errors +=1
        if num_errors == max_errors:
            break
    else:
        # success
        num_errors = 0