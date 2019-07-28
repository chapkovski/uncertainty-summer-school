from otree.api import Currency as c, currency_range
from .pages import *
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):

    def play_round(self):
        gender = random.choice([i[0] for i in Constants.GENDER_CHOICES])
        politics = random.choice([i[0] for i in Constants.POLITY_CHOICES])
        yield Q, {'gender': gender, 'politics': politics}
