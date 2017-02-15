import scholarly
from operator import itemgetter

nameIn = open('Researchers', 'r')
names = []
citation = {}
counter = 0
for name in nameIn:
    name = name.strip()
    names.append(name)
length = len(names)
for name in names:
    query = scholarly.search_author(name)
    try:
        author = next(query)
        print name.strip() + ": " + str(author.citedby),
        citation[name] = author.citedby
    except StopIteration:
        print "** " + name.strip() + " Not found!",
        citation[name] = 0
        pass
    counter += 1
    print "\tNo." + str(counter) + '/' + str(length)
citationSorted = sorted(citation.items(), key=itemgetter(1), reverse=True)
print citationSorted
