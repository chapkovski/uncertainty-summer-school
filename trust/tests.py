from otree.api import Currency as c, currency_range
from .pages import *
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):

    def play_round(self):
        yield Intro
        if self.player.role() == 'trustor':
            yield Send, {'send': random.randint(0, Constants.endowment)}
        else:
            yield SendBack, {'send_back': random.randint(0, self.group.send*Constants.coef)}
        yield Results
