from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    pass


class Send(Page):
    form_model = 'group'
    form_fields = ['send']

    def is_displayed(self) -> bool:
        return self.player.role() == 'trustor'


class BeforeSendBackWP(WaitPage):

    def vars_for_template(self):
        return {'body_text': f'Please wait for Participant {self.player.get_other().get_role_desc()}'}


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
    Intro,
    Send,
    BeforeSendBackWP,
    SendBack,
    ResultsWaitPage,
    Results
]
