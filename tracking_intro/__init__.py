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
        choices=[['Male', 'Male'], ['Female', 'Female'], ['Prefer not to answer/ non-binary', 'Prefer not to answer/ non-binary']],
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

    own_car = models.StringField(
        label='Does your household own a car (or lease a car)?',
        choices=[['No', 'No'],
                 ['gasoline', 'Yes, a gasoline car'],
                 ['hybrid', 'Yes, a hybrid electric vehicle'],
                 ['ev', 'Yes, an electric vehicle']],
        widget=widgets.RadioSelect,
    )

    car_model = models.StringField(
        label='What size car does your household own / lease?',
        choices=[['Small', 'Small car (e.g., Toyota Yaris, Fiat 500, Dacia Sandero)'],
                 ['Medium', 'Medium sized car (e.g., VW Golf, Audi A6)'],
                 ['Luxury', 'Luxury car / Sports car / SUV (e.g., Range Rover, Porsche, Mercedes-Benz S-Class)']],
        widget=widgets.RadioSelect,
        blank=True,
    )

    car_number = models.StringField(
        label='How many cars do you own?',
        choices=[['1', 'One'],
                 ['2', 'Two'],
                 ['3', 'Three']],
        widget=widgets.RadioSelect,
        blank=True,
    )

    car_age = models.StringField(
        label='When have you bought the main car you are using?',
        choices=[['Less than 5 years ago', 'Less than 5 years ago'],
                 ['Less than 10 years ago', 'Less than 10 years ago'],
                 ['More than 10 years ago', 'More than 10 years ago']],
        widget=widgets.RadioSelect,
        blank=True,
    )

    car = models.StringField(
        label='Whether or not you currently own a car, envisioning a scenario where you are purchasing a new one, what size of car would you find most appealing for your daily journeys?',
        choices=[['Small', 'Small car (e.g., Toyota Yaris, Fiat 500, Dacia Sandero)'],
                 ['Medium', 'Medium sized car (e.g., VW Golf, Audi A6)'],
                 ['Luxury', 'Luxury car / Sports car / SUV (e.g., Range Rover, Porsche, Mercedes-Benz S-Class)']],
        widget=widgets.RadioSelect,
    )

    drivers_license = models.StringField(
        label="Do you currently hold a valid driver's license?",
        choices=[['Yes', 'Yes'],
                 ['No', 'No'],
                 ['Process', 'In the process of obtaining a license']],
        widget=widgets.RadioSelect,
    )

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
    yield ["session", "participant_code", "round_number", "id_in_group", "element_id", "enter_time", "leave_time", "duration", "attributeType", "attributeValue", "buyEV"]
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


# Demographics Page class
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'education', 'income']


class Car_questions(Page):
    form_model = 'player'
    form_fields = ['drivers_license', 'own_car', 'car_model', 'car', 'car_number', 'car_age']

    def before_next_page(player: Player, timeout_happened):
        # Store car value in participant.vars
        player.participant.vars['car'] = player.car

        # Add console log statement
        print(f"DEBUG: Car value stored - {player.participant.vars['car']}")


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
    instructions,
    Tracker_demo,
    practice_completed_template
]
