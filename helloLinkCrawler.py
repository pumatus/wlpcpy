import re
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

def link_crawler(seed_url, link_regex):
    """
    Crawl from the given seed URL seed URL following links matched by link_regex
    """
    crawl_queue = [seed_url]
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)

        for link in get_links(html):
            if re.match(link_regex, link):
                crawl_queue.append(link)

def get_links(html):
    webpage_regex = re.compile("<a[^>]+href=['\"](.*?)['\"]", re.IGNORECASE)
    return webpage_regex.findall(html)