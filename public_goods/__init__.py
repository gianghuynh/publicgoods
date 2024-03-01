from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'public_goods'
    PLAYERS_PER_GROUP = 10
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

# PAGES
class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    pass


page_sequence = [Contribute, ResultsWaitPage, Results]
