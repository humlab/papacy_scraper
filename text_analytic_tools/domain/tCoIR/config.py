
DEFAULT_PERIOD_GROUPS = [
    {
        'id': 'years_1919-1972',
        'title': '1919-1972',
        'column': 'signed_year',
        'type': 'range',
        'periods': list(range(1919, 1973))
    },
    {
        'id': 'default_division',
        'title': 'Default division',
        'column': 'signed_period',
        'type': 'divisions',
        'periods': [ (1919, 1939), (1940, 1944), (1945, 1955), (1956, 1966), (1967, 1972) ]
    },
    {
        'id': 'alt_default_division',
        'title': 'Alt. division',
        'column': 'signed_period_alt',
        'type': 'divisions',
        'periods': [ (1919, 1944), (1945, 1955), (1956, 1966), (1967, 1972) ]
    },
    {
        'id': 'years_1945-1972',
        'title': '1945-1972',
        'column': 'signed_year',
        'type': 'range',
        'periods': list(range(1945, 1973))
    }
]

PERIOD_GROUPS_ID_MAP = { x['id']: x for x in DEFAULT_PERIOD_GROUPS }

DEFAULT_TOPIC_GROUPS = {
    '7CULT, 7SCIEN, and 7EDUC': {
        '7CULT': ['7CULT', '7CORR'],
        '7SCIEN': ['7SCIEN'],
        '7EDUC': ['7EDUC']
    },
    '7CULT, 7SCI, and 7EDUC+4EDUC': {
        '7CULT': ['7CULT', '7CORR'],
        '7SCIEN': ['7SCIEN'],
        '7EDUC+4EDUC': ['7EDUC', '4EDUC']
    },
    '7CULT + 1AMITY': {
        '7CULT': ['7CULT', '7CORR'],
        '1AMITY': ['1AMITY']
    },
    '7CULT + 1ALLY': {
        '7CULT': ['7CULT', '7CORR'],
        '1ALLY': ['1ALLY']
    },
    '7CORR + 1DIPLOMACY': {
        '7CORR': ['7CORR'],
        'DIPLOMACY': ['1ALLY', '1AMITY', '1ARMCO', '1CHART', '1DISPU', '1ESTAB', '1HEAD', '1OCCUP', '1OPTC', '1PEACE', '1RECOG', '1REPAR', '1STATU', '1TERRI', '1TRUST']
    },
    '7CULT + 1DIPLOMACY': {
        '7CULT': ['7CULT', '7CORR'],
        'DIPLOMACY': ['1ALLY', '1AMITY', '1ARMCO', '1CHART', '1DISPU', '1ESTAB', '1HEAD', '1OCCUP', '1OPTC', '1PEACE', '1RECOG', '1REPAR', '1STATU', '1TERRI', '1TRUST']
    },
    '7CULT + 2WELFARE': {
        '7CULT': ['7CULT', '7CORR'],
        '2WELFARE': [ '2HEW', '2HUMAN', '2LABOR', '2NARK', '2REFUG', '2SANIT', '2SECUR', '2WOMEN' ]
    },
    '7CULT + 3ECONOMIC': {
        '7CULT': ['7CULT', '7CORR'],
        'ECONOMIC': ['3CLAIM', '3COMMO', '3CUSTO', '3ECON', '3INDUS', '3INVES', '3MOSTF', '3PATEN', '3PAYMT', '3PROD', '3TAXAT', '3TECH', '3TOUR', '3TRADE', '3TRAPA']
    },
    '7CULT + 4AID': {
        '7CULT': ['7CULT', '7CORR'],
        '4AID': ['4AGRIC', '4AID', '4ATOM', '4EDUC', '4LOAN', '4MEDIC', '4MILIT', '4PCOR', '4RESOU', '4TECA', '4UNICE']
    },
    '7CULT + 5TRANSPORT': {
        '7CULT': ['7CULT', '7CORR'],
        '5TRANSPORT': ['5AIR', '5LAND', '5TRANS', '5WATER']
    },
    '7CULT + 6COMMUNICATIONS': {
        '7CULT': ['7CULT', '7CORR'],
        '6COMMUNICATIONS': ['6COMMU', '6MEDIA', '6POST', '6TELCO']
    },
    '7CULTURE': {
        '7CORR': ['7CORR'],
        '7CULT': ['7CULT'],
        '7EDUC': ['7EDUC'],
        '7RELIG': ['7RELIG'],
        '7SCIEN': ['7SCIEN'],
        '7SEMIN': ['7SEMIN'],
        '7SPACE': ['7SPACE']
    },
    '7CORR': {
        '7CORR': ['7CORR']
    },
    '7CULT': {
        '7CULT': ['7CULT', '7CORR']
    },
    '7CULT + 8RESOURCES': {
        '7CULT': ['7CULT', '7CORR'],
        '8RESOURCES': ['8AGRIC', '8CATTL', '8ENERG', '8ENVIR', '8FISH', '8METAL', '8WATER', '8WOOD']
    },
    '7CULT + 9ADMINISTRATION': {
        '7CULT': ['7CULT', '7CORR'],
        '9ADMINISTRATION': ['9ADMIN', '9BOUND', '9CITIZ', '9CONSU', '9LEGAL', '9MILIT', '9MILMI', '9PRIVI', '9VISAS', '9XTRAD' ]
    },
}

TOPIC_GROUP_MAPS = {
    group_name: {
        v: k for k in DEFAULT_TOPIC_GROUPS[group_name].keys() for v in DEFAULT_TOPIC_GROUPS[group_name][k]
    } for group_name in DEFAULT_TOPIC_GROUPS.keys()
}

parties_of_interest = ['FRANCE', 'GERMU', 'ITALY', 'GERMAN', 'UK', 'GERME', 'GERMW', 'INDIA', 'GERMA' ]

TREATY_FILTER_OPTIONS = {
    'Is Cultural': 'is_cultural',
    'Topic is 7CULT': 'is_7cult',
    'No filter': ''
}

TREATY_FILTER_TOOLTIPS = [
    'Include ONLY treaties marked as "is cultural"',
    'Include all treaties where topic is 7CULT (disregard "is cultural" flag)',
    'Include ALL treaties (no topic filter)'
]

PARTY_NAME_OPTIONS = {
    'WTI Code': 'party',
    'WTI Name': 'party_name',
    'WTI Short': 'party_short_name',
    'Country': 'party_country'
}

PARTY_PRESET_OPTIONS = {
    'PartyOf5': parties_of_interest,
    'Germany (all)': [ 'GERMU', 'GERMAN', 'GERME', 'GERMW', 'GERMA' ],
    'Select all': [ 'SELECT_ALL', 'ALL_PARTIES', 'ALL' ],
    'Unselect all': [ ]
}
