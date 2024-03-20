from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from callbacks.callback_filter import MyCallback
from keyboards.manager_link import user_link


# Старт
def start_buttons():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text='Продажа бизнеса и поиск инвестиций',
            callback_data=MyCallback(foo='sale_biz').pack())
    )
    builder.row(
        InlineKeyboardButton(
            text='Подбор инвест. проекта',
            callback_data=MyCallback(foo='find_invest').pack())
        )
    builder.row(
        InlineKeyboardButton(
            text='Строительство, проекты, дизайн',
            callback_data=MyCallback(foo='bild_proj').pack()),
        )
    builder.row(
        InlineKeyboardButton(
            text='Бизнес консультации',
            callback_data=MyCallback(foo='biz_cunsultation').pack()),
        )

    return builder.as_markup()


# Старт >> Продажа бизнеса и поиск инвестиций
def sale_biz_find_invest_buttons():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text='Узнать больше',
            callback_data=MyCallback(foo='learn_more').pack())
    )
    builder.row(
        InlineKeyboardButton(
            text='Назад',
            callback_data=MyCallback(foo='start').pack()
        )
    )

    return builder.as_markup()


# Старт >> Продажа бизнеса и поиск инвестиций >> Узнать больше
def sale_biz_learn_more_buttons():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text='Мои обязательные условия',
            callback_data=MyCallback(foo='my_condition').pack())
    )
    builder.row(
        InlineKeyboardButton(
            text='Как я продаю готовые бизнесы',
            callback_data=MyCallback(foo='how_i_sale_biz').pack())
    )
    builder.row(
        InlineKeyboardButton(
            text='Стоимость услуг',
            callback_data=MyCallback(foo='service_price').pack())
    )
    builder.row(
        InlineKeyboardButton(
            text='Консультация',
            callback_data=MyCallback(foo='consultation').pack())
    )
    builder.row(
        InlineKeyboardButton(
            text='Назад',
            callback_data=MyCallback(foo='sale_biz').pack()
        )
    )


    return builder.as_markup()


# Старт >> Продажа бизнеса и поиск инвестиций >> Узнать больше >> Мои обязательные условия
def my_conslusion_back_buttons():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text='Консультация',
            callback_data=MyCallback(foo='consultation').pack())
    )
    builder.row(
        InlineKeyboardButton(
            text='Назад',
            callback_data = MyCallback(foo='learn_more').pack())
    )

    return builder.as_markup()


# Старт >> Подбор инвест. проекта
def take_inv_proj_buttons():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text='Цены и условия работы',
            callback_data=MyCallback(foo='price_condition').pack())
    )
    builder.row(
        InlineKeyboardButton(
            text='Структура работы',
            callback_data=MyCallback(foo='struct_work').pack())
    )
    builder.row(
        InlineKeyboardButton(
            text='Консультация',
            callback_data=MyCallback(foo='consultation').pack())
    )
    builder.row(
        InlineKeyboardButton(
            text="Назад",
            callback_data=MyCallback(foo='start').pack()
        )
    )

    return builder.as_markup()


# Старт >> Строительство, проекты, дизайн
def build_proj_des_buttons():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text='Стройматериалы',
            callback_data=MyCallback(foo='construct').pack())
        )
    builder.row(
        InlineKeyboardButton(
            text='Проектирование и дизайн интерьера',
            callback_data=MyCallback(foo='project_design').pack())
        )
    builder.row(
        InlineKeyboardButton(
            text='Консультация',
            callback_data=MyCallback(foo='consultation').pack())
    )
    builder.row(
        InlineKeyboardButton(
            text='Назад',
            callback_data=MyCallback(foo='start').pack()
        )
    )

    return builder.as_markup()


# Старт >> Строительство, проекты, дизайн >> Стройматериалы
# Создаю структуру из клавиатур в отдельном файле - cunstruct_keyboards


# Старт >> Строительство, проекты, дизайн >> Проектирование и дизайн интерьера
def project_design_btns():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text='1️⃣ Сколько стоит проект?',
            callback_data=MyCallback(foo='how_price_project').pack())
        )
    builder.row(
        InlineKeyboardButton(
            text='2️⃣ Из чего состоит проект?',
            callback_data=MyCallback(foo='what_is_project').pack())
        )
    builder.row(
        InlineKeyboardButton(
            text='3️⃣ Есть ли готовые варианты?',
            callback_data=MyCallback(foo='there_ready_variants').pack())
        )
    builder.row(
        InlineKeyboardButton(
            text='4️⃣ Как долго делается?',
            callback_data=MyCallback(foo='how_long').pack())
        )
    builder.row(
        InlineKeyboardButton(
            text='5️⃣ Где встретиться переговорить?',
            callback_data=MyCallback(foo='where_meeting').pack())
        )
    builder.row(
        InlineKeyboardButton(
            text='6️⃣ Сколько стоит дизайн?',
            callback_data=MyCallback(foo='price_design').pack())
        )
    builder.row(
        InlineKeyboardButton(
            text='7️⃣ Из чего состоит дизайн?',
            callback_data=MyCallback(foo='design_content').pack())
        )
    builder.row(
        InlineKeyboardButton(
            text='8️⃣ Как долго делается дизайн?',
            callback_data=MyCallback(foo='how_long_design').pack())
        )
    builder.row(
        InlineKeyboardButton(
            text='Назад',
            callback_data=MyCallback(foo='bild_proj').pack()
        )
    )

    return builder.as_markup()

# УДАЛИТЬ ЕСЛИ НЕ ПОПРОСЯТ ВЕРНУТЬ
# Старт >> Строительство, проекты, дизайн >> Проектирование и дизайн интерьера >> Сколько стоит проект?
def proj_design_feedback_buttons():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text='Назад',
            callback_data=MyCallback(foo='project_design').pack())
        )
    builder.row(
        InlineKeyboardButton(
            text='Написать менеджеру',
            url=user_link)
        )

    return builder.as_markup()


# Старт >> Бизнес консультации
def biz_consultation_buttons():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text='Мои соц.сети',
            callback_data=MyCallback(foo='my_social_network').pack())
        )
    builder.row(
        InlineKeyboardButton(
            text='Кто я и чем могу быть полезен',
            callback_data=MyCallback(foo='who_i_am').pack())
        )
    builder.row(
        InlineKeyboardButton(
            text='Консультация',
            callback_data=MyCallback(foo='consultation').pack())
    )
    builder.row(
        InlineKeyboardButton(
            text='Назад',
            callback_data=MyCallback(foo='start').pack())
    )

    return builder.as_markup()


# Юзер не в первый раз заполняет анкету
def biz_consultation_answer_buttons():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text='Продолжить',
            callback_data=MyCallback(foo='continue').pack())
    )

    return builder.as_markup()


# Старт >> Бизнес консультации (удалить сообщение)
def delete_message_buttons():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text='Назад',
            callback_data=MyCallback(foo='delete_message').pack()
        )
    )
    builder.row(
        InlineKeyboardButton(
            text='Консультация',
            callback_data=MyCallback(foo='consultation').pack())
    )

    return builder.as_markup()


# Отправить номер телефона
def send_phone():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text='Телеграм канал',
            url='https://web.telegram.org/k/#@concretov19'
        )
    )

    return builder.as_markup()

