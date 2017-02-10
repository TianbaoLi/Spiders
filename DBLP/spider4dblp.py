import urllib
import re
import json
from operator import itemgetter

sourceUrl = "http://dblp.uni-trier.de/search/publ/api?"
conference = "NIPS"
years = range(2012, 2017)
authorRecord = {}


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    page.close()
    return html


def getLink():
    for year in years:
        link = sourceUrl + "q=" + conference + " venue%3A" + conference + "%3A year%3A" + year.__str__() + "%3A&h=1000&format=json"
        print "Fetching " + link + "......",
        getAuthor(link)


def getAuthor(url):
    html = getHtml(url)
    htmlJson = json.loads(html)
    hits = htmlJson["result"]["hits"]["hit"]
    print hits.__len__()
    for hit in hits:
        try:
            authors = hit["info"]["authors"]["author"]
        except KeyError:
            pass
        for author in authors:
            if len(author) < 4:
                continue
            authorRecord[author] = authorRecord.get(author, 0) + 1


def main():
    getLink()
    authorRecordSortedbyTimes = sorted(authorRecord.items(), key=itemgetter(1))
    print authorRecordSortedbyTimes


if __name__ == '__main__':
    main()