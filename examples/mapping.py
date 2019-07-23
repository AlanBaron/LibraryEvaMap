YARRRML_MAPPING = '''mappings:
    match:
        source: dataset-source
        subject: https://example.org/$(home_team)-$(away_team)
        predicateobjects:
        - [a, 'https://www.bbc.co.uk/ontologies/sport#terms_Match']
        - ['https://www.bbc.co.uk/ontologies/sport#terms_home_goal',$(home_goal),'http://www.w3.org/2001/XMLSchema#integer']
        - ['https://www.bbc.co.uk/ontologies/sport#terms_away_goal',$(away_goal),'http://www.w3.org/2001/XMLSchema#integer']
        - ['https://www.bbc.co.uk/ontologies/sport#terms_awayCompetitor',$(away_team)]
        - ['https://www.bbc.co.uk/ontologies/sport#terms_homeCopetitor',$(home_team)]
        - ['https://www.bbc.co.uk/ontologies/sport#terms_isMatchOf',$(name),'http://www.w3.org/2001/XMLSchema#integer']
    round:
        source: dataset-source
        subject: https://example.org/$(name)
        predicateobjects:
        - [a, 'https://www.bbc.co.uk/ontologies/sport#terms_Round']
        - ['https://www.bbc.co.uk/ontologies/sport#terms_hasMatch',$(home_team)-$(away_team))]
        - ['http://dbpedia.org/ontology/startDate',$(start_date)]
        - ['http://dbpedia.org/ontology/endDate',$(end_date)]
    homeTeam:
        source: dataset-source
        subject: https://example.org/$(name)-$(home_team)
        predicateobjects:
        - [a, 'http://dbpedia.org/ontology/SportsTeam']
    awayTeam:
        source: dataset-source
        subject: https://example.org/$(name)-$(away_team)
        predicateobjects:
        - [a, 'http://dbpedia.org/ontology/SportsTeam']
sources:
    dataset-source: [data.json~jsonpath, '$.records.[*].fields']'''
