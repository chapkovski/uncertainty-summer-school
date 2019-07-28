class Constants(BaseConstants):
    POLITY_CHOICES = [(0, 'Donald Trump'), (1, 'Joe Biden'), (2, 'Another candidate')]


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            choices = Constants.POLITY_CHOICES.copy()
            random.shuffle(choices)
            p.participant.vars['politics_choices'] = choices
            p.politics_set = str(choices)


class Player(BasePlayer):
    politics = models.IntegerField(widget=widgets.RadioSelect)
    politics_set = models.StringField()

    def politics_choices(self):
        return self.participant.vars['politics_choices']
