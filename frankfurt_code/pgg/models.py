from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'pgg'
    players_per_group = 3
    num_rounds = 1
    coef = 2
    endowment = 20  # an endowment for fixed endowment treatment
    lb = 10  # lower and upper boundaries for variable endowment treatment
    ub = 30


class Subsession(BaseSubsession):
    def creating_session(self):
        hetero_endowment = self.session.config['hetero_endowment']
        for p in self.get_players():
            if hetero_endowment:
                if self.round_number == 1:
                    p.endowment = random.randint(Constants.lb, Constants.ub)
                else:
                    p.endowment = p.in_round(1).endowment
            else:
                p.endowment = Constants.endowment


class Group(BaseGroup):
    total_contribution = models.CurrencyField(doc='Total contribution of all group members')
    individual_share = models.CurrencyField(doc='pie from a group project for each member')

    def set_payoffs(self):
        contribs = [p.contribution for p in self.get_players()]
        self.total_contribution = sum(contribs)
        self.individual_share = self.total_contribution * Constants.coef / Constants.players_per_group
        for p in self.get_players():
            p.payoff = p.endowment - p.contribution + self.individual_share


class Player(BasePlayer):
    endowment = models.CurrencyField(doc='individual endowment for each player')
    contribution = models.CurrencyField(doc='to store individual contributions',
                                        label='How much you would like to invest to the common project')

    def contribution_max(self):
        return self.endowment
