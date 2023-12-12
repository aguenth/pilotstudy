from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'demographics'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Demographics fields (age, gender, education, income, car)
    age = models.IntegerField(label='What is your <b>age</b>?', min=18, max=99)
    gender = models.StringField(
        label='What is your <b>gender</b>?',
        choices=[['Male', 'Male'],
                 ['Female', 'Female'],
                 ['Prefer not to answer/ non-binary', 'Prefer not to answer/ non-binary']],
        widget=widgets.RadioSelect,
    )
    education = models.StringField(
        label='What is your <b>highest education</b>?',
        choices=[['No formal education', 'No formal education'],
                 ['Compulsory education', 'Compulsory education (secondary school)'],
                 ['Further education', 'Further education'],
                 ['Higher education (Bachelor, Master, PhD)', 'Higher education (Bachelor, Master, PhD)']],
        widget=widgets.RadioSelect,
    )
    income = models.StringField(
        label='How high is your <b>yearly personal income before tax</b>?',
        choices=[['< $30,000', '< $30,000'],
                 ['$30,000 to $50,000', '$30,000 to $50,000'],
                 ['$50,001 to $75,000', '$50,001 to $75,000'],
                 ['$75,001 to $100,000', '$75,001 to $100,000'],
                 ['> $100,001', '> $100,001']],
        widget=widgets.RadioSelect,
    )
    household = models.StringField(
        label='How many people live in your household?',
        choices=[['1', 'Just me'],
                 ['2', '2 people'],
                 ['3', '3 people'],
                 ['4', '4 people'],
                 ['5', 'More than 5 people']],
        widget=widgets.RadioSelect,
    )
    region = models.StringField(
        label='In which type of region do you live?',
        choices=[['1', 'Urban'],
                 ['2', 'Suburban'],
                 ['3', 'Rural']],
        widget=widgets.RadioSelect,
    )

    drivers_license = models.StringField(
        label="Do you currently hold a valid driver's license?",
        choices=[['Yes', 'Yes'],
                 ['No', 'No'],
                 ['Process', 'In the process of obtaining a license']],
        widget=widgets.RadioSelect,
    )
    own_car = models.StringField(
        label='Does your household own a car (or lease a car)?',
        choices=[['No', 'No'],
                 ['Yes', 'Yes']],
        widget=widgets.RadioSelect,
    )
    car_type = models.StringField(
        label='What kind of car is your main car you use for daily trips?',
        choices=[['gasoline', 'Gasoline car'],
                 ['ev', 'Electric car'],
                 ['hev', 'Hybrid car']],
        widget=widgets.RadioSelect,
        blank=True,
    )
    car_model = models.StringField(
        label='What size is that car?',
        choices=[['Small', 'Small car (e.g., Toyota Yaris, Fiat 500, Dacia Sandero)'],
                 ['Medium', 'Medium sized car (e.g., VW Golf, Audi A6)'],
                 ['Luxury', 'Luxury car / Sports car / SUV (e.g., Range Rover, Porsche, Mercedes-Benz S-Class)']],
        widget=widgets.RadioSelect,
        blank=True,
    )
    car_number = models.StringField(
        label='How many cars does your household own in total?',
        choices=[['1', '1 car'],
                 ['2', '2 cars'],
                 ['3', '3 cars'],
                 ['4', 'More than 3 cars']],
        widget=widgets.RadioSelect,
        blank=True,
    )
    car_age = models.IntegerField(label='How old is your main car (in years)?', min=0, max=30, blank=True)
    car_replace = models.StringField(
        label='How often do you replace your car?',
        choices=[['every year', 'Every year'],
                 ['every four years', 'Every 4 years'],
                 ['every eight years', 'Every 8 years'],
                 ['every twelve years', 'Every 12 years']],
        widget=widgets.RadioSelect,
        blank=True,
    )
    car = models.StringField(
        label='Whether or not you currently own a car, envisioning a scenario where you are purchasing a new one, '
              'what size of car would you find most appealing for your daily journeys?',
        choices=[['Small', 'Small car (e.g., Toyota Yaris, Fiat 500, Dacia Sandero)'],
                 ['Medium', 'Medium sized car (e.g., VW Golf, Audi A6)'],
                 ['Luxury', 'Luxury car / Sports car / SUV (e.g., Range Rover, Porsche, Mercedes-Benz S-Class)']],
        widget=widgets.RadioSelect,
    )
    km_week = models.IntegerField(label='How many miles do you drive in a typical week?', min=0, max=500, blank=True)

    wom_owner = models.StringField(
        label='If someone you know asks you for your opinion on your electric car, do you give... ',
        choices=[['neutral', 'a neutral response'],
                 ['positive', 'a positive response'],
                 ['negative', 'a negative response'],
                 ['mixed', 'a mixed response']],
        widget=widgets.RadioSelect,
        blank=True,
    )
    wom_number = models.IntegerField(label='How many people do you know who own an electric vehicle?',
                                     min=0, max=50)
    wom_positive = models.StringField(
        label='In the past month, how often have you heard <b>positive</b> comments about electric vehicles?',
        choices=[['every day', 'More than once a week'],
                 ['once week', 'Once a week'],
                 ['once month', 'Once a month'],
                 ['never', 'Never']],
        widget=widgets.RadioSelect,
        )
    wom_negative = models.StringField(
        label='In the past month, how often have you heard <b>negative</b> comments about electric vehicles?',
        choices=[['every day', 'More than once a week'],
                 ['once week', 'Once a week'],
                 ['once month', 'Once a month'],
                 ['never', 'Never']],
        widget=widgets.RadioSelect,
        )

    affect_ev = models.IntegerField(widget=widgets.RadioSelect,
                                               choices=[['1', ''], ['2', '2'], ['3', '3'],
                                                        ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7'], ['8', '8'],
                                                        ['9', '9'], ['10', '10']])

    # Consent fields
    dataScience = models.BooleanField(initial=False)
    dataTeach = models.BooleanField(initial=False)

    # Additional fields for Tracker_demo
    def store_tracking_data(self, payload):
        HoverEvent.create(
            player=self,
            element_id=payload["element_id"],
            enter_time=payload["enter_time"],
            leave_time=payload["leave_time"],
            duration=payload["duration"],
            attributeType=payload["attributeType"],
            attributeValue=payload["attributeValue"],
        )

    teacher = models.StringField(
        choices=["Marketing", "Philosophy", "Spanish"],
        widget=widgets.RadioSelectHorizontal,
    )


class HoverEvent(models.ExtraModel):
    player = models.Link(Player)
    element_id = models.StringField()
    enter_time = models.FloatField()
    leave_time = models.FloatField()
    duration = models.IntegerField()
    attributeType = models.StringField()
    attributeValue = models.StringField()


def custom_export(players):
    yield ["session", "participant_code", "round_number", "id_in_group", "element_id", "enter_time", "leave_time",
           "duration", "attributeType", "attributeValue", "buyEV"]
    for player in players:
        for e in HoverEvent.filter(player=player):
            yield [
                player.session.code,
                player.participant.code,
                player.round_number,
                player.id_in_group,
                e.element_id,
                e.enter_time,
                e.leave_time,
                e.duration,
                e.attributeType,
                e.attributeValue,
                player.teacher,
            ]


class introduction_consent(Page):
    form_model = 'player'
    form_fields = ['dataScience', 'dataTeach']
    @staticmethod
    def vars_for_template(player: Player):
        return {
            "particpantlabel": player.participant.label,
        }  # add ?participant_label={{%PROLIFIC_PID%}} to link on prolific


# Demographics Page class
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'education', 'income', 'household', 'region']


class Car_questions(Page):
    form_model = 'player'
    form_fields = ['drivers_license', 'own_car', 'car_model', 'car', 'car_type', 'car_number', 'car_age', 'car_replace',
                   'km_week']

    def before_next_page(player: Player, timeout_happened):
        # Store car value in participant.vars
        player.participant.vars['car'] = player.car

        # Add console log statement
        print(f"DEBUG: Car value stored - {player.participant.vars['car']}")


class WoM(Page):
    form_model = 'player'
    form_fields = ['wom_owner', 'wom_number', 'wom_positive', 'wom_negative']


class affect(Page):
    form_model = 'player'
    form_fields = ['affect_ev']


class instructions(Page):
    form_model = 'player'


class Tracker_demo(Page):
    form_model = 'player'
    form_fields = ['teacher']


class practice_completed_template(Page):
    form_model = 'player'


# Page sequence
page_sequence = [
    introduction_consent,
    Demographics,
    Car_questions,
    WoM,
    affect,
    instructions,
    Tracker_demo,
    practice_completed_template
]
