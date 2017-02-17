import scholarly
import urllib
import json

fileName = "Authors"
confList = ["KDD", "NIPS", "IJCAI", "ICML", "AAAI"]
nameIn = open(fileName + ".txt", 'r')
citationOut = open(fileName + ".out", 'w')
names = []
citation = {}
citation5year = {}
hIndex = {}
hIndex5year = {}
#paper = {}
maxCitation = 0
maxCitation5year = 0
maxHIndex = 0
maxHIndex5year = 0
#maxPaper = 0
sourceUrl = "http://dblp.uni-trier.de/search/publ/api?q="


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    page.close()
    return html

'''
def getPaper(name):
    if name == "Bo An":
        paper[name] = 20
        maxPaper = max(maxPaper, paper[name])
        return paper[name]
    elif name == "Yi Yang":
        paper[name] = 25
        maxPaper = max(maxPaper, paper[name])
        return paper[name]
    elif name == "Le Song":
        paper[name] = 48
        maxPaper = max(maxPaper, paper[name])
        return paper[name]
    elif name == "Ba Zhang":
        paper[name] = 0
        maxPaper = max(maxPaper, paper[name])
        return paper[name]
    global sourceUrl
    global maxPaper
    amount = 0
    for conf in confList:
        url = sourceUrl + name + " venue%3A" + conf + "%3A&h=1000&format=json"
        html = getHtml(url)
        htmlJson = {}
        try:
            htmlJson = json.loads(html)
        except ValueError:
            pass
        count = 0
        try:
            count = int(htmlJson["result"]["hits"]["@total"])
        except KeyError:
            pass
        amount += count
    paper[name] = amount
    maxPaper = max(maxPaper, amount)
    return amount
'''


def getCitation(name):
    global maxCitation
    global maxCitation5year
    global maxHIndex
    global maxHIndex5year
    query = scholarly.search_author(name)
    author = next(query)
    url_citations = scholarly._CITATIONAUTH.format(author.id)
    url = '{0}&pagesize={1}'.format(url_citations, scholarly._PAGESIZE)
    soup = scholarly._get_soup(scholarly._HOST + url)
    index = soup.find_all('td', class_='gsc_rsb_std')
    cit = int(index[0].text)
    cit5 = int(index[1].text)
    h = int(index[2].text)
    h5 = int(index[3].text)
    citation[name] = cit
    citation5year[name] = cit5
    hIndex[name] = h
    hIndex5year[name] = h5
    maxCitation = max(maxCitation, cit)
    maxCitation5year = max(maxCitation5year, cit5)
    maxHIndex = max(maxHIndex, h)
    maxHIndex5year = max(maxHIndex5year, h5)
    return cit, cit5, h, h5


def main():
    for name in nameIn:
        name = name.strip()
        names.append(name)
    length = len(names)
    counter = 0
    for name in names:
        try:
            (cit, cit5, h, h5) = getCitation(name)
            #paperAmount = getPaper(name)
            print name.strip(), ": ", cit, cit5, h, h5,
        except StopIteration:
            print "** " + name.strip() + " Not found!",
            citation[name] = 0
            pass
        counter += 1
        print "\tNo." + str(counter) + '/' + str(length)
#        if counter == 5:
#            break
    for name in names:
        try:
            mark = (1.0 * citation[name] / maxCitation + 1.0 * citation5year[name] / maxCitation5year + 1.0 * hIndex[name] / maxHIndex + 1.0 * hIndex5year[name] / maxHIndex5year) / 4
            citationOut.write("%s\t%d\t%d\t%d\t%d\t%d\t%lf\n" % (name, citation[name], citation5year[name], hIndex[name], hIndex5year[name], mark))
        except KeyError:
            citationOut.write("%s\n" % name)
            pass


if __name__ == "__main__":
    main()
