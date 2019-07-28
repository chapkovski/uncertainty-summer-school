from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Q(Page):
    form_model = 'player'
    form_fields = ['gender', 'politics']

    def before_next_page(self):
        self.participant.vars['gender'] = self.player.get_gender_display()
        self.participant.vars['politics'] = self.player.get_politics_display()


page_sequence = [
    Q
]
