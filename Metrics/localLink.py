import requests

from Metrics.metric import metric

def localLink(g_onto, liste_map, g_map, raw_data, g_link) : #Fait
    points = 0
    nbPossible = 0
    result = metric()
    result['name'] = "Use of local links"
    set_URIs = set()
    links = set()
    for s, _, _ in g_map.triples((None, None, None)) :
        set_URIs.add(s)
    for elt in set_URIs :
        deb = elt.split('$')[0]
        fin = elt.split('$(')[1].split(')')[0]
        if elt != deb:
            for elements in raw_data:
                link = deb + str(elements['fields'][fin])
                links.add(link)
    for link in links:
        nbPossible = nbPossible + 1
        a = requests.get(link)
        try :
            a.raise_for_status()
        except:
            points = points + 1
    if nbPossible == 0:
        result['score'] = 1
    else :
        result['score'] = 1-points/nbPossible
    return result
