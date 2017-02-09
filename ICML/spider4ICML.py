import urllib
import re
from operator import itemgetter

sourceUrl = "http://dblp.uni-trier.de/db/conf/icml/"
years = range(2016, 2004, -1)
authorRecord = {}


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    page.close()
    return html


def getLink():
    for year in years:
        link = "http://dblp.uni-trier.de/db/conf/icml/icml" + year.__str__() + ".html"
        print "Fetching " + link + "......",
        getAuthor(link)


def getAuthor(url):
    html = getHtml(url)
    reg = r'span itemprop="name">.+?</span>'
    authors = re.compile(reg)
    authorList = authors.findall(html)
    print authorList.__len__()
    for author in authorList:
        author = author.split('<')[0].split('>')[1]
        authorRecord[author] = authorRecord.get(author, 0) + 1


def main():
    getLink()
    authorRecordSortedbyTimes = sorted(authorRecord.items(), key=itemgetter(1))
    print authorRecordSortedbyTimes


if __name__ == '__main__':
    main()
