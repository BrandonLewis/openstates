import datetime

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
    sesssion_details={
        'Forty-ninth Legislature - First Regular Session':
            {'type': 'primary', 'session_id': 87},
        'Forty-ninth Legislature - First Special Session':
            {'type': 'special', 'session_id': 89},
        'Forty-ninth Legislature - Second Special Session':
            {'type': 'special', 'session_id': 90},
        'Forty-ninth Legislature - Third Special Session':
            {'type': 'special', 'session_id': 91},
        'Forty-ninth Legislature - Fourth Special Session':
            {'type': 'special', 'session_id': 92},
        'Forty-ninth Legislature - Fifth Special Session':
            {'type': 'special', 'session_id': 94},
        'Forty-ninth Legislature - Sixth Special Session':
            {'type': 'special', 'session_id': 95},
        'Forty-ninth Legislature - Seventh Special Session':
            {'type': 'special', 'session_id': 96},
        'Forty-ninth Legislature - Eighth Special Session':
            {'type': 'special', 'session_id': 101},
        'Forty-ninth Legislature - Second Regular Session':
            {'type': 'primary', 'session_id': 93},
    }
)
