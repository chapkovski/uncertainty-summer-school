from otree.api import Currency as c, currency_range
from .pages import *
from ._builtin import Bot
from .models import Constants
import random

class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield Intro
        yield Contribution, {'contribution': random.randint(0, self.player.endowment)}
        yield Results
        if self.round_number == Constants.num_rounds:
            yield FinalResults
