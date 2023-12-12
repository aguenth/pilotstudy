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

    ev_prob_benefits1 = make_field('...considerably reduce my expenses.')
    ev_prob_benefits2 = make_field('...considerably increase my independence.')
    ev_prob_benefits3 = make_field('...considerably decrease my impact on the climate.')
    ev_prob_benefits4 = make_field('...be part of a collective action.')

    ev_prob_risks1 = make_field('...high initial costs.')
    ev_prob_risks2 = make_field('...too low a return of investment.')

    ev_perceived_risk1 = make_field('Buying an electric vehicle is a risk for me.')
    ev_perceived_risk2 = make_field('I find buying an electric vehicle too risky.')
    ev_perceived_benefit1 = make_field('Buying an electric vehicle is good for me.')
    ev_perceived_benefit2 = make_field('I find that buying an electric vehicle brings many advantages.')

    neighborhood1 = make_field('I am interested in what my neighbors are doing.')
    neighborhood2 = make_field('I enjoy meeting and chatting with my neighbors.')
    neighborhood3 = make_field('It is easy to make friends with my neighbors.')
    neighborhood4 = make_field('In my neighborhood, we often borrow things from each other.')

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


class probability(Page):
    form_model = 'player'
    form_fields = ['ev_prob_benefits1', 'ev_prob_benefits2', 'ev_prob_benefits3', 'ev_prob_benefits4',
                   'ev_prob_risks1', 'ev_prob_risks2']


class risks(Page):
    form_model = 'player'
    form_fields = ['ev_perceived_risk1', 'ev_perceived_risk2', 'ev_perceived_benefit1', 'ev_perceived_benefit2']


class neighbors(Page):
    form_model = 'player'
    form_fields = ['neighborhood1', 'neighborhood2', 'neighborhood3', 'neighborhood4']


# Page sequence
page_sequence = [
    probability,
    risks,
    neighbors,
    cc_concern,
    pol_orientation,
    end
]
