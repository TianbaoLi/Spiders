import scholarly

nameIn = open('Researchers', 'r')
for name in nameIn:
    query = scholarly.search_author(name)
    try:
        author = next(query)
        print name.strip() + ": " + str(author.citedby)
    except StopIteration:
        print "**" + name.strip() + " Not found!"
        pass

