import urllib
import re
from operator import itemgetter

sourceUrl = "https://papers.nips.cc/"
authorRecord = {}


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getLink(html):
    reg = r'<li><a href="/book.+?">'
    linkByYear = re.compile(reg)
    for link in linkByYear.findall(html):
        link = link.split("\"")[1]
        link = sourceUrl + link
        print "Fetching " + link + "......"
        getAuthor(link)


def getAuthor(url):
    html = getHtml(url)
    reg = r'class="author">.+?</a>,'
    authors = re.compile(reg)
    for author in authors.findall(html):
        author = author.split('<')[0].split('>')[1]
        authorRecord[author] = authorRecord.get(author, 0) + 1


def main():
    html = getHtml(sourceUrl)
    getLink(html)
    authorRecordSortedbyTimes = sorted(authorRecord.items(), key=itemgetter(1))
    print authorRecordSortedbyTimes


if __name__ == '__main__':
    main()
