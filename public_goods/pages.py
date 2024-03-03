from otree.api import *
# PAGES
class Introduction(Page):
    def is_displayed(self):
        return self.round_number ==1
class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution','guess_contribution_other']

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs_for_group'
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    pass

class Question(Page):
    form_model = 'player'
    form_fields = ['age','gender']

class Finished(Page):
    pass

page_sequence = [Introduction, Contribute, ResultsWaitPage, Results, Question, Finished]
