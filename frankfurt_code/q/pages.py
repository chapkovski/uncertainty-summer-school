from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Q(Page):
    form_model = 'player'

    def get_form_fields(self):
        fields = ['gender', 'politics']
        random.shuffle(fields)
        return fields

    def before_next_page(self):
        self.participant.vars['gender'] = self.player.get_gender_display()
        self.participant.vars['politics'] = self.player.get_politics_display()


page_sequence = [
    Q
]
