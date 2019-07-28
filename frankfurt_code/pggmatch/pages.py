from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MatchingWP(WaitPage):
    group_by_arrival_time = True

    def is_displayed(self) -> bool:
        return self.round_number == 1

    def get_players_for_group(self, waiting_players):
        women = [p for p in waiting_players if p.participant.vars['gender'] == 'Female']
        men = [p for p in waiting_players if p.participant.vars['gender'] == 'Male']
        if len(women) >= Constants.players_per_group:
            return women[:Constants.players_per_group]
        if len(men) >= Constants.players_per_group:
            return men[:Constants.players_per_group]
        unmatched = [p for p in self.session.get_participants() if p.vars.get('matched') is not True]
        if len(unmatched) <= Constants.players_per_group and len(waiting_players) >= Constants.players_per_group:
            return waiting_players[:Constants.players_per_group]

    def after_all_players_arrive(self):
        for p in self.group.get_players():
            print(p.participant.vars.get('gender'))
            p.participant.vars['matched'] = True


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
    MatchingWP,
    Intro,
    Contribution,
    ResultsWaitPage,
    Results,
    FinalResults,
]
