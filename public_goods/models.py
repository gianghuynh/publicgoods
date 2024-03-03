from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'public_goods'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    ENDOWMENT = cu(100)
    EFFICIENCY = 1.5


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total = models.CurrencyField()
    share = models.CurrencyField()
    def set_payoffs(self):
        self.total = sum([p.contribution for p in self.get_players()])
        self.share = self.total * C.EFFICIENCY / C.PLAYERS_PER_GROUP
        for p in self.get_players():
            p.payoff = C.ENDOWMENT - p.contribution + self.share


class Player(BasePlayer):
    contribution = models.CurrencyField(min=0,max=C.ENDOWMENT, label="How much will you contribute?")
    guess_contribution_other = models.FloatField(
        min=0, max=C.ENDOWMENT, label="How much do you think the other subject will invest"
    )
    age = models.IntegerField(min=18, label="Age:")
    gender = models.StringField(choices=['male','female','other'], label="Gender:")
