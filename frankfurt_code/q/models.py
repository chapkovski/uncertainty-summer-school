from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'q'
    players_per_group = None
    num_rounds = 1
    GENDER_CHOICES = [(0, 'Male'), (1, 'Female')]
    POLITY_CHOICES = [(0, 'Donald Trump'), (1, 'Joe Biden'), (2, 'Another candidate')]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    gender = models.IntegerField(label='Please indicate your gender', choices=Constants.GENDER_CHOICES,
                                 widget=widgets.RadioSelectHorizontal)
    politics = models.IntegerField(label='Who you are going to vote fore at 2020 elections?',
                                   choices=Constants.POLITY_CHOICES,
                                   widget=widgets.RadioSelect)
