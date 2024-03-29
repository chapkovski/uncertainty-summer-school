from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants, Player
import random
from django.core import validators


class Intro(Page):
    template_name = 'pggfg/Introduction.html'

    def is_displayed(self):
        return self.subsession.round_number == 1


class IntroPunishment(Page):
    def is_displayed(self) -> bool:
        return self.round_number == self.session.config['punishment_round']


class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']

    def vars_for_template(self):
        label = f'How much you would like to contribute to the common project (from 0 to {self.player.endowment})?'
        return {'label': label, }

    def contribution_max(self):
        return self.player.endowment


class AfterContribWP(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_pd_payoffs()


class Punishment(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.subsession.punishment

    def get_form_fields(self):
        return ['pun{}'.format(p.id_in_group) for p in self.player.get_others_in_group()]

    def vars_for_template(self):
        others = self.player.get_others_in_group()
        form = self.get_form()
        data = zip(others, form)
        return {'data': data}

    def error_message(self, values):
        tot_pun = sum([int(i) for i in values.values()])
        if tot_pun > self.player.punishment_endowment:
            return f'You cannot spend  more than {self.player.punishment_endowment} on deduction'


class AfterPunishmentWP(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_final_payoffs()


class Results(Page):
    pass


class FinalResults(Page):
    def is_displayed(self) -> bool:
        return self.round_number == Constants.num_rounds

    def vars_for_template(self) -> dict:
        return {'real_payoff': self.participant.payoff.to_real_world_currency(self.session)}


page_sequence = [

    Intro,
    IntroPunishment,
    Contribute,
    AfterContribWP,
    Punishment,
    AfterPunishmentWP,
    Results,
    FinalResults,
]
