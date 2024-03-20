from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

new_user_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Оставить мой номер телефона', request_contact=True),
         KeyboardButton(text='Написать менеджеру')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
remove_kb = ReplyKeyboardRemove()
user_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
         KeyboardButton(text='Написать менеджеру')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
