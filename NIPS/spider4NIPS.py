import urllib
import re

sourceHtml = "https://papers.nips.cc/"


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getlink(html):
    reg = r'<li><a href="/book.+?">'
    linkByYear = re.compile(reg)
    for link in linkByYear.findall(html):
        link = link.split("\"")[1]
        link = sourceHtml + link
        print link


def main():
    html = getHtml(sourceHtml)
    getlink(html)


if __name__ == '__main__':
    main()
