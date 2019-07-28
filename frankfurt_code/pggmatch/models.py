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
    name_in_url = 'pggmatch'
    players_per_group = 3
    num_rounds = 1
    coef = 2
    endowment = c(20)  # an endowment for fixed endowment treatment
    lb = c(10)  # lower and upper boundaries for variable endowment treatment
    ub = c(30)


class Subsession(BaseSubsession):
    politics = models.BooleanField()
    random = models.BooleanField()
    gender = models.BooleanField()
    def creating_session(self):
        self.politics = self.session.config.get('politics')
        self.gender = self.session.config.get('gender')
        self.random = self.session.config.get('random')
        if self.random:
            self.group_randomly()

        for p in self.get_players():
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
