import pytest
from wtforms import Form, StringField, SelectField


GENDERS = [(1, 'Male'), (2, 'Female')]


def int_or_none(value):
    try:
        return int(value)
    except:
        return None


class Player(Form):
    gender = SelectField('Gender', choices=GENDERS)


class PlayerCoerceInt(Form):
    gender = SelectField('Gender', coerce=int, choices=GENDERS)


class PlayerCoerceCustom(Form):
    gender = SelectField('Gender', coerce=int_or_none, choices=GENDERS)


@pytest.mark.parametrize('Player,data,value', [
    (Player, {'gender': 1}, '1'),
    (Player, {'gender': None}, 'None'),
    (PlayerCoerceInt, {'gender': '1'}, 1),
    (PlayerCoerceInt, {'gender': None}, None),
    (PlayerCoerceCustom, {'gender': 1}, 1),
    (PlayerCoerceCustom, {'gender': '1'}, 1),
    (PlayerCoerceCustom, {'gender': ''}, None),
    (PlayerCoerceCustom, {'gender': None}, None),
])
def test_coerce(Player, data, value):
    # https://wtforms.readthedocs.io/en/stable/fields.html#wtforms.fields.SelectField
    player = Player(data=data)
    assert player.gender.data == value


# vi:et:ts=4:sw=4:cc=80
