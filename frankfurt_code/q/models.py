from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

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
    def creating_session(self):
        for p in self.get_players():
            choices = Constants.POLITY_CHOICES.copy()
            random.shuffle(choices)
            p.participant.vars['politics_choices'] = choices
            p.politics_set = str(choices)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    gender = models.IntegerField(label='Please indicate your gender', choices=Constants.GENDER_CHOICES,
                                 widget=widgets.RadioSelectHorizontal)
    politics = models.IntegerField(label='Who you are going to vote fore at 2020 elections?',
                                   widget=widgets.RadioSelect)
    politics_set = models.StringField(doc='To store the order political preferences are shown')

    def politics_choices(self):
        return self.participant.vars['politics_choices']
