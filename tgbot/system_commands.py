from typing import Dict

from telegram import Bot, BotCommand

from tgbot.main import bot


def set_up_commands(bot_instance: Bot) -> None:

    langs_with_commands: Dict[str, Dict[str, str]] = {
        'en': {
            'start': 'Start bot 🚀',
            'registration': 'Registration in the game 🎮',
            'start_game': 'Start the game ☕',
            # 'stats': 'Statistics of bot 📊',
            # 'admin': 'Show admin info ℹ️',
            # 'ask_location': 'Send location 📍',
            # 'broadcast': 'Broadcast message 📨',
            # 'export_users': 'Export users.csv 👥',
        },
        'ru': {
            'start': 'Запустить бота 🚀',
            'registration': 'Регистрация в игре 🎮',
            'start_game': 'Начать игру ☕',
            # 'stats': 'Статистика бота 📊',
            # 'admin': 'Показать информацию для админов ℹ️',
            # 'broadcast': 'Отправить сообщение 📨',
            # 'ask_location': 'Отправить локацию 📍',
            # 'export_users': 'Экспорт users.csv 👥',
        }
    }

    bot_instance.delete_my_commands()
    for language_code in langs_with_commands:
        bot_instance.set_my_commands(
            language_code=language_code,
            commands=[
                BotCommand(command, description) for command, description in langs_with_commands[language_code].items()
            ]
        )


set_up_commands(bot)
