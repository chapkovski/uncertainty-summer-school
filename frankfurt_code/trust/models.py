from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'trust'
    players_per_group = None
    num_rounds = 1
    endowment = 10
    coef = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    send = models.CurrencyField(doc='amount sent by trustor')
    send_back = models.CurrencyField(doc='amount sent back by trustee')

    def set_payoffs(self):
        trustor = self.get_player_by_role('trustor')
        trustee = self.get_player_by_role('trustee')
        trustor.payoff = Constants.endowment - self.amount_sent + self.amount_sent_back
        trustee.payoff = Constants.endowment + self.amount_sent * Constants.coef - self.amount_sent_back


class Player(BasePlayer):

    def role(self) -> str:
        if self.id_in_group == 1:
            return 'trustor'
        return 'trustee'
