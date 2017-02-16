import scholarly
from operator import itemgetter

fileName = "Authors"
nameIn = open(fileName + ".txt", 'r')
citationOut = open(fileName + ".out", 'w')
names = []
citation = {}
hIndex = {}
counter = 0
for name in nameIn:
    name = name.strip()
    names.append(name)
length = len(names)
for name in names:
    query = scholarly.search_author(name)
    try:
        author = next(query)
        url_citations = scholarly._CITATIONAUTH.format(author.id)
        url = '{0}&pagesize={1}'.format(url_citations, scholarly._PAGESIZE)
        soup = scholarly._get_soup(scholarly._HOST + url)
        index = soup.find_all('td', class_='gsc_rsb_std')
        h = int(index[2].text)
        print name.strip() + ": " + str(author.citedby), h,
        citation[name] = author.citedby
        hIndex[name] = h
    except StopIteration:
        print "** " + name.strip() + " Not found!",
        citation[name] = 0
        pass
    counter += 1
    print "\tNo." + str(counter) + '/' + str(length)
    break
#citationSorted = sorted(citation.items(), key=itemgetter(1), reverse=True)
#citation = sorted(citation)
for name in names:
    try:
        citationOut.write("%s\t%s\t%s\n" % (name, citation[name], hIndex[name]))
    except KeyError:
        pass
