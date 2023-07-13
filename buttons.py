from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

timeform_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
timeform_kb.add(
    KeyboardButton('Present'),
    KeyboardButton('Past'),
    KeyboardButton('Future')
)

continuation_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
continuation_kb.add(
    KeyboardButton('Simple'),
    KeyboardButton('Continuous'),
    KeyboardButton('Perfect'),
    KeyboardButton('Perfect Continuous'), KeyboardButton('restart')
)

choose_help_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
choose_help_kb.add(
    KeyboardButton('Структура'),
    KeyboardButton('Примеры'), KeyboardButton('restart')
)
