"""
Данный пакет создан, чтобы разместить все клавиатуры для пункта - Стройматериалы
"""

from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from callbacks.callback_filter import MyCallback


def start_construct():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text='1️⃣ Где офис ?',
            callback_data=MyCallback(foo='where_office').pack())
    )
    builder.row(
        InlineKeyboardButton(
            text='2️⃣ Где посмотреть товар?',
            callback_data=MyCallback(foo='where_look_product').pack())
    )
    builder.row(
        InlineKeyboardButton(
            text='3️⃣ Какое качество?',
            callback_data=MyCallback(foo='which_quality').pack())
    )
    builder.row(
        InlineKeyboardButton(
            text='4️⃣ как оплатить?',
            callback_data=MyCallback(foo='how_pay').pack())
    )
    builder.row(
        InlineKeyboardButton(
            text='Назад',
            callback_data=MyCallback(foo='bild_proj').pack()
        )
    )

    return builder.as_markup()


def one():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text='2️⃣ Где посмотреть товар?',
            callback_data=MyCallback(foo='where_look_product').pack())
    )
    builder.row(
        InlineKeyboardButton(
            text='3️⃣ Какое качество?',
            callback_data=MyCallback(foo='which_quality').pack())
    )
    builder.row(
        InlineKeyboardButton(
            text='4️⃣ как оплатить?',
            callback_data=MyCallback(foo='how_pay').pack())
    )
    builder.row(
        InlineKeyboardButton(
            text='Назад',
            callback_data=MyCallback(foo='bild_proj').pack()
        )
    )

    return builder.as_markup()


def two():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text='1️⃣ Где офис ?',
            callback_data=MyCallback(foo='where_office').pack())
    )
    builder.row(
        InlineKeyboardButton(
            text='3️⃣ Какое качество?',
            callback_data=MyCallback(foo='which_quality').pack())
    )
    builder.row(
        InlineKeyboardButton(
            text='4️⃣ как оплатить?',
            callback_data=MyCallback(foo='how_pay').pack())
    )
    builder.row(
        InlineKeyboardButton(
            text='Назад',
            callback_data=MyCallback(foo='bild_proj').pack()
        )
    )

    return builder.as_markup()


def three():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text='1️⃣ Где офис ?',
            callback_data=MyCallback(foo='where_office').pack())
    )
    builder.row(
        InlineKeyboardButton(
            text='2️⃣ Где посмотреть товар?',
            callback_data=MyCallback(foo='where_look_product').pack())
    )
    builder.row(
        InlineKeyboardButton(
            text='4️⃣ как оплатить?',
            callback_data=MyCallback(foo='how_pay').pack())
    )
    builder.row(
        InlineKeyboardButton(
            text='Назад',
            callback_data=MyCallback(foo='bild_proj').pack()
        )
    )

    return builder.as_markup()


def four():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text='1️⃣ Где офис ?',
            callback_data=MyCallback(foo='where_office').pack())
    )
    builder.row(
        InlineKeyboardButton(
            text='2️⃣ Где посмотреть товар?',
            callback_data=MyCallback(foo='where_look_product').pack())
    )
    builder.row(
        InlineKeyboardButton(
            text='3️⃣ Какое качество?',
            callback_data=MyCallback(foo='which_quality').pack())
    )
    builder.row(
        InlineKeyboardButton(
            text='Назад',
            callback_data=MyCallback(foo='bild_proj').pack()
        )
    )

    return builder.as_markup()