import datetime

# session information available from http://azleg.gov/xml/sessions.asp

metadata = dict(
    name='Arizona',
    abbreviation='az',
    legislature_name='Arizona Legislature',
    lower_chamber_name='House of Representatives',
    upper_chamber_name='Senate',
    lower_chamber_title='Representative',
    upper_chamber_title='Senator',
    lower_chamber_term=2,
    upper_chamber_term=2,
    terms=[
        {'name': 'Forty-ninth Legislature',
         'start_year': 2009, 'end_year': 2010,
         'sessions': [
                'Forty-ninth Legislature - First Regular Session',
                'Forty-ninth Legislature - First Special Session',
                'Forty-ninth Legislature - Second Special Session',
                'Forty-ninth Legislature - Third Special Session',
                'Forty-ninth Legislature - Fourth Special Session',
                'Forty-ninth Legislature - Fifth Special Session',
                'Forty-ninth Legislature - Sixth Special Session',
                'Forty-ninth Legislature - Seventh Special Session',
                'Forty-ninth Legislature - Eighth Special Session',
                'Forty-ninth Legislature - Second Regular Session',
                #'Forty-ninth Legislature - Ninth Special Session',
         ]
        },
    ],
    session_details={
        'Forty-ninth Legislature - First Regular Session':
            {'type': 'primary', 'session_id': 87,
             'start_date': datetime.date(2009,1,12),
             'end_date': datetime.date(2009,7,1)},
        'Forty-ninth Legislature - First Special Session':
            {'type': 'special', 'session_id': 89,
             'start_date': datetime.date(2009,1,28),
             'end_date': datetime.date(2009,1,31)},
        'Forty-ninth Legislature - Second Special Session':
            {'type': 'special', 'session_id': 90,
             'start_date': datetime.date(2009,5,21),
             'end_date': datetime.date(2009,5,27)},
        'Forty-ninth Legislature - Third Special Session':
            {'type': 'special', 'session_id': 91,
             'start_date': datetime.date(2009,7,6),
             'end_date': datetime.date(2009,8,25)},
        'Forty-ninth Legislature - Fourth Special Session':
            {'type': 'special', 'session_id': 92,
             'start_date': datetime.date(2009,11,17),
             'end_date': datetime.date(2009,11,23)},
        'Forty-ninth Legislature - Fifth Special Session':
            {'type': 'special', 'session_id': 94,
             'start_date': datetime.date(2009,12,17),
             'end_date': datetime.date(2009,12,19)},
        'Forty-ninth Legislature - Sixth Special Session':
            {'type': 'special', 'session_id': 95,
             'start_date': datetime.date(2010,2,1),
             'end_date': datetime.date(2010,2,11)},
        'Forty-ninth Legislature - Seventh Special Session':
            {'type': 'special', 'session_id': 96,
             'start_date': datetime.date(2010,3,8),
             'end_date': datetime.date(2010,3,16)},
        'Forty-ninth Legislature - Eighth Special Session':
            {'type': 'special', 'session_id': 101,
             'start_date': datetime.date(2010,3,29),
             'end_date': datetime.date(2010,4,1)},
        'Forty-ninth Legislature - Second Regular Session':
            {'type': 'primary', 'session_id': 93,
             'start_date': datetime.date(2010,1,11),
             'end_date': datetime.date(2010,4,29)},
    }
)
