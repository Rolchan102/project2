from typing import Union, Optional, Dict, List

import telegram
from telegram import MessageEntity, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater

from dtb.settings import TELEGRAM_TOKEN
from users.models import User


def from_celery_markup_to_markup(celery_markup: Optional[List[List[Dict]]]) -> Optional[InlineKeyboardMarkup]:
    markup = None
    if celery_markup:
        markup = []
        for row_of_buttons in celery_markup:
            row = []
            for button in row_of_buttons:
                row.append(
                    InlineKeyboardButton(
                        text=button['text'],
                        callback_data=button.get('callback_data'),
                        url=button.get('url'),
                    )
                )
            markup.append(row)
        markup = InlineKeyboardMarkup(markup)
    return markup


def from_celery_entities_to_entities(celery_entities: Optional[List[Dict]] = None) -> Optional[List[MessageEntity]]:
    entities = None
    if celery_entities:
        entities = [
            MessageEntity(
                type=entity['тип'],
                offset=entity['отступ'],
                length=entity['длина'],
                url=entity.get('url'),
                language=entity.get('язык'),
            )
            for entity in celery_entities
        ]
    return entities


def send_one_message(
    user_id: Union[str, int],
    text: str,
    parse_mode: Optional[str] = "HTML",
    reply_markup: Optional[List[List[Dict]]] = None,
    reply_to_message_id: Optional[int] = None,
    disable_web_page_preview: Optional[bool] = None,
    entities: Optional[List[MessageEntity]] = None,
    tg_token: str = TELEGRAM_TOKEN,
) -> bool:
    updater = Updater(tg_token)
    bot = updater.bot
    try:
        m = bot.send_message(
            chat_id=user_id,
            text=text,
            parse_mode=parse_mode,
            reply_markup=reply_markup,
            reply_to_message_id=reply_to_message_id,
            disable_web_page_preview=disable_web_page_preview,
            entities=entities,
        )
    except telegram.error.Unauthorized:
        print(f"Не могу отправить сообщение {user_id}. Причина: Бот остановлен.")
        User.objects.filter(user_id=user_id).update(is_blocked_bot=True)
        success = False
    else:
        success = True
        User.objects.filter(user_id=user_id).update(is_blocked_bot=False)
    return success
