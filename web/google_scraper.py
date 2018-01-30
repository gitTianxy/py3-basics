# encoding=utf-8
"""
analyze links from google search result
------------------------------------------------
"""
import requests
from bs4 import BeautifulSoup
from pprint import pprint


def google(query, page=1):
    query_para = query.replace(' ', '+')
    url = 'https://www.google.com/search?q=%s&start=%s' % (query_para, 10 * (page - 1))
    return get_link_content(url)


def pickout_links(html):
    links = []
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.select('h3.r a'):
        links.append(item.get('href').replace('/url?q=', ''))
    return links


def get_link_content(link):
    proxies = {
        "http": "http://localhost:1080",
        "https": "http://localhost:1080",
    }
    print '*** query:', link
    r = requests.get(link, proxies=proxies)
    if r.status_code != 200:
        print 'status: %s, reason: %s' % (r.status_code, r.reason)
        return None
    return r.content


def content_analysis(topic):
    pass


def retrieve_data_with_lib(html, link):
    topic = None
    content = []
    for item in link_lib:
        if item['title'] in link:
            soup = BeautifulSoup(html, "html.parser")
            # get topic
            for topic_dom in soup.select(item['topic_container']):
                if topic_dom.find(item['topic_dom'], attrs={item['topic_attr_key']: item['topic_attr_val']}):
                    topic = topic_dom.get_text()
                    break
            # get content
            content.extend(soup.select(item['content_dom']))
    return dict(topic=topic, content=content)


link_lib = [
    {
        'title': 'stackoverflow.com',
        'topic_container': 'div#question-header',
        'topic_dom': 'h1',
        'topic_attr_key': 'itemprop',
        'topic_attr_val': 'name',
        'content_dom': 'div.accepted-answer'
    },
    {
        'title': 'github.com',
        'topic_container': 'h1.public',
        'topic_dom': 'strong',
        'topic_attr_key': 'itemprop',
        'topic_attr_val': 'name',
        'content_dom': 'div.repository-content'
    },
    {
        'title': 'www.youtube.com',
        'topic_container': 'div.ytd-video-primary-info-renderer',
        'topic_dom': 'h1',
        'topic_attr_key': 'class',
        'topic_attr_val': 'title',
        'content_dom': 'div.repository-content'
    },
]


if __name__ == '__main__':
    results = []
    key_words = 'python google links'
    for page in range(1, 5):
        html = google(query=key_words, page=page)
        print '--------------------------'
        links = pickout_links(html)
        for l in links:
            c = get_link_content(l)
            if c is None:
                continue
            results.append(retrieve_data_with_lib(c, l))
    # display
    print '======== RESULT ======='
    pprint(results, indent=4)
