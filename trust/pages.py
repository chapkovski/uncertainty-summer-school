from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Send(Page):
    form_model = 'group'
    form_fields = ['send']

    def is_displayed(self) -> bool:
        return self.player.role() == 'trustor'


class WaitTrustorWP(WaitPage):
    pass


class SendBack(Page):
    form_model = 'group'
    form_fields = ['send_back']

    def is_displayed(self) -> bool:
        return self.player.role() == 'trustee'


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    pass


page_sequence = [
    Send,
    WaitTrustorWP,
    SendBack,
    ResultsWaitPage,
    Results
]
