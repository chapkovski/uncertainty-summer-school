class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()

    def set_payoffs(self):
        contribs = [p.contribution for p in self.get_players()]
        self.total_contribution = sum(contribs)
        self.individual_share = self.total_contribution * Constants.coef / Constants.players_per_group
        for p in self.get_players():
            p.payoff = p.endowment - p.contribution + self.individual_share