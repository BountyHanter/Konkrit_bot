from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Оставить номер телефона', request_contact=True),
         KeyboardButton(text='Написать менеджеру')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
