from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
    'use_browser_bots': False
}

SESSION_CONFIGS = [
    {
        'name': 'trust',
        'display_name': "Trust game",
        'num_demo_participants': 2,
        'app_sequence': ['trust'],
    },
    {
        'name': 'pgg',
        'display_name': "Public goods - fixed endowment",
        'num_demo_participants': 3,
        'app_sequence': ['pgg'],
        'hetero_endowment': False,
    },
    {
        'name': 'pgghetero',
        'display_name': "Public goods - random endowment",
        'num_demo_participants': 3,
        'app_sequence': ['pgg'],
        'hetero_endowment': True,
    },
    {
        'name': 'q',
        'display_name': "Questionnaire",
        'num_demo_participants': 1,
        'app_sequence': ['q'],

    },
    {
        'name': 'pggmatch',
        'display_name': "PGG Match",
        'num_demo_participants': 3,
        'app_sequence': ['q', 'pggmatch'],
        'random': True,
        'gender': False,
        'polity': False,
    },
    {
        'name': 'pggmatchgender',
        'display_name': "PGG Random Match by gender",
        'num_demo_participants': 3,
        'app_sequence': ['q', 'pggmatch'],
        'random': False,
        'gender': True,
        'politics': False,
    },
    {
        'name': 'pggmatchpolity',
        'display_name': "PGG Match by political preferences",
        'num_demo_participants': 3,
        'app_sequence': ['q', 'pggmatch'],
        'random': True,
        'gender': False,
        'politics': True,
    },
    {
        'name': 'pggfg',
        'display_name': "PGG with Punishment",
        'num_demo_participants': 3,
        'app_sequence': ['pggfg'],
        'punishment_round': 2,

    },
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '%8#onc=--=$r)n-qiw%1u82^ujpeb$0iw6w!rwz%y-pjfafvul'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
