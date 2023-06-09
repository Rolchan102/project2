from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from tgbot.handlers.onboarding.static_text import registration_button_text, game_button_text


def make_keyboard_for_start_command() -> InlineKeyboardMarkup:
    buttons = [[
        InlineKeyboardButton(registration_button_text, callback_data='start_registration'),
    ]]

    return InlineKeyboardMarkup(buttons)


def make_keyboard_for_comeback_command() -> InlineKeyboardMarkup:
    buttons = [[
        InlineKeyboardButton(game_button_text, callback_data='start_game'),
        # InlineKeyboardButton(secret_level_button_text, callback_data=f'{SECRET_LEVEL_BUTTON}')
    ]]

    return InlineKeyboardMarkup(buttons)
