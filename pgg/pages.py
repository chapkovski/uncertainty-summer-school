from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    def is_displayed(self) -> bool:
        return self.round_number == 1


class Contribution(Page):
    form_model = 'player'
    form_fields = ['contribution']

    def vars_for_template(self) -> dict:
        return {'contribution_label': f'How much you would like to contribute (from 0 to {self.player.endowment})'}


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    pass


class FinalResults(Page):
    def is_displayed(self) -> bool:
        return self.round_number == Constants.num_rounds


page_sequence = [
    Intro,
    Contribution,
    ResultsWaitPage,
    Results,
    FinalResults,
]
