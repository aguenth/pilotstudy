import random
from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'questionnaire'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def make_field(label):
        return models.IntegerField(
            choices=[['6', 'Agree completely (6)'], ['5', '5'], ['4', '4'],
                     ['3', '3'], ['2', '2'], ['1', 'Completely disagree (1)']],
            label=label,
            widget=widgets.RadioSelectHorizontal,
        )

    # questionnaire
    conservative_liberal = models.IntegerField(widget=widgets.RadioSelect,
                                               choices=[['1', 'extremely liberal (1)'], ['2', '2'], ['3', '3'],
                                                        ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7'], ['8', '8'],
                                                        ['9', '9'], ['10', 'extremely conservative (10)']])
    climate_change_concern1 = make_field('I worry about the climate´s state.')
    climate_change_concern2 = make_field('Climate protection is important for our future.')
    climate_change_concern3 = make_field('We must protect the climate´s delicate equilibrium.')
    climate_change_concern4 = make_field('Climate change has severe consequences for humans and nature.')

    EVreason = models.StringField(
            label='If you said you would not want to buy an EV, what was the reason?',
            choices=[['I would buy a gasoline car instead', 'I would buy a gasoline car instead'],
                     ['I would not buy any car', 'I would not buy any car'],
                     ['I would buy a different kind of car (e.g., Hybrid)',
                      'I would buy a different kind of car (e.g., Hybrid)']],
            widget=widgets.RadioSelect,
        )


# FUNCTIONS
# PAGES

class cc_concern(Page):
    form_model = 'player'
    form_fields = ['climate_change_concern1', 'climate_change_concern2', 'climate_change_concern3',
                   'climate_change_concern4']


class pol_orientation(Page):
    form_model = 'player'
    form_fields = ['conservative_liberal']


class end(Page):
    form_model = 'player'
    form_fields = []


class EVreason(Page):
    form_model = 'player'
    form_fields = ['EVreason']


# Page sequence
page_sequence = [
    EVreason,
    cc_concern,
    pol_orientation,
    end
]
