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
    players_per_group = 2
    num_rounds = 1
    endowment = c(10)
    coef = 3
    role_desc = {'trustor': 'A',
                 'trustee': 'B'}


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    send = models.CurrencyField(doc='amount sent by trustor',
                                label=f'How much money you would like to send to'
                                f' your partner (from 0 to {Constants.endowment})?',
                                min=0, max=Constants.endowment)
    send_back = models.CurrencyField(doc='amount sent back by trustee',
                                     label='How much money you would like to send back?', min=0)

    def send_back_max(self):
        return self.send * Constants.coef

    def set_payoffs(self):
        trustor = self.get_player_by_role('trustor')
        trustee = self.get_player_by_role('trustee')
        trustor.payoff = Constants.endowment - self.send + self.send_back
        trustee.payoff = Constants.endowment + self.send * Constants.coef - self.send_back


class Player(BasePlayer):
    def get_role_desc(self):
        return Constants.role_desc[self.role()]

    def role(self) -> str:
        if self.id_in_group == 1:
            return 'trustor'
        return 'trustee'

    def get_other(self):
        return self.get_others_in_group()[0]
