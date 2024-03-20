import asyncio
import os

from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart

from bot_messages.bot_answer import start, construct_proj_design_start, construct, sale_biz_invest, take_invest_proj, \
    biz_consultation, sale_biz_learn_more, my_condition, how_i_sale_biz, service_price, price_condition, struct_work, \
    where_office, where_look_product, which_quality, how_pay, project_design, \
    how_price_project, what_is_project, there_ready_variants, how_long, where_meeting, price_design, design_content, \
    how_long_design, what_exactly_help, send_request, my_social_network, who_i_am, contact_handler, \
    write_manager, inline_start, delete_message, send_request_continue, consultation

from bot_messages import bot_answer
from bot_commands.commands import set_commands
from callbacks.callback_filter import MyCallback
from utils.states.main_state import MainState
from utils.tech_function import bot_logger


async def dev_message_startup(bot: Bot):
    await bot.send_message(977249859, 'Бот Конкрит запущен')


async def dev_message_shutdown(bot: Bot):
    await bot.send_message(977249859, 'Бот Конкрит остановлен')


async def start_bot():
    load_dotenv()
    token = os.getenv('DEV_TOKEN')
    bot = Bot(token=token, default=DefaultBotProperties(parse_mode='MarkdownV2'))
    await set_commands(bot)
    dp = Dispatcher()
    loger = bot_logger.bot_logger()
    # Уведомления разработчику о включении и выключении бота
    dp.startup.register(dev_message_startup)
    dp.shutdown.register(dev_message_shutdown)

    # Старт
    dp.message.register(start, CommandStart())  # CommandStart - Команда обрабатывающая команду /start
    dp.callback_query.register(inline_start, MyCallback.filter(F.foo == 'start')) # Отработка по инлайн кнопке

    # Старт >> Продажа бизнеса и поиск инвестиций
    dp.callback_query.register(sale_biz_invest, MyCallback.filter(F.foo == 'sale_biz'))

    # Старт >> Продажа бизнеса и поиск инвестиций >> Узнать больше
    dp.callback_query.register(sale_biz_learn_more, MyCallback.filter(F.foo == 'learn_more'))

    # Старт >> Продажа бизнеса и поиск инвестиций >> Узнать больше >> Мои обязательные условия
    dp.callback_query.register(my_condition, MyCallback.filter(F.foo == 'my_condition'))

    # Старт >> Продажа бизнеса и поиск инвестиций >> Узнать больше >> Как я продаю готовые бизнесы
    dp.callback_query.register(how_i_sale_biz, MyCallback.filter(F.foo == 'how_i_sale_biz'))

    # Старт >> Продажа бизнеса и поиск инвестиций >> Узнать больше >> Стоимость услуг
    dp.callback_query.register(service_price, MyCallback.filter(F.foo == 'service_price'))
    # __________________________________________________________________________________________________________________

    # Старт >> Подбор инвест. проекта
    dp.callback_query.register(take_invest_proj, MyCallback.filter(F.foo == 'find_invest'))

    # Старт >> Подбор инвест. проекта >> Цены и условия работы
    dp.callback_query.register(price_condition, MyCallback.filter(F.foo == 'price_condition'))

    # Старт >> Подбор инвест. проекта >> Структура работы
    dp.callback_query.register(struct_work, MyCallback.filter(F.foo == 'struct_work'))
    # __________________________________________________________________________________________________________________

    # Старт >> Строительство, проекты, дизайн
    dp.callback_query.register(construct_proj_design_start, MyCallback.filter(F.foo == 'bild_proj'))

    # Старт >> Строительство, проекты, дизайн >> Стройматериалы
    dp.callback_query.register(construct, MyCallback.filter(F.foo == 'construct'))

    # Старт >> Строительство, проекты, дизайн >> Стройматериалы >> Где офис?
    dp.callback_query.register(where_office, MyCallback.filter(F.foo == 'where_office'))

    # Старт >> Строительство, проекты, дизайн >> Стройматериалы >> Где посмотреть товар?
    dp.callback_query.register(where_look_product, MyCallback.filter(F.foo == 'where_look_product'))

    # Старт >> Строительство, проекты, дизайн >> Стройматериалы >> Качество товаров
    dp.callback_query.register(which_quality, MyCallback.filter(F.foo == 'which_quality'))

    # Старт >> Строительство, проекты, дизайн >> Стройматериалы >> Как оплатить?
    dp.callback_query.register(how_pay, MyCallback.filter(F.foo == 'how_pay'))

    # Старт >> Строительство, проекты, дизайн >> Проектирование и дизайн интерьера
    dp.callback_query.register(project_design, MyCallback.filter(F.foo == 'project_design'))

    # Старт >> Строительство, проекты, дизайн >> Проектирование и дизайн интерьера >> Сколько стоит проект?
    dp.callback_query.register(how_price_project, MyCallback.filter(F.foo == 'how_price_project'))

    # Старт >> Строительство, проекты, дизайн >> Проектирование и дизайн интерьера >> Из чего состоит проект?
    dp.callback_query.register(what_is_project, MyCallback.filter(F.foo == 'what_is_project'))

    # Старт >> Строительство, проекты, дизайн >> Проектирование и дизайн интерьера >> Как долго делается?
    dp.callback_query.register(how_long, MyCallback.filter(F.foo == 'how_long'))

    # Старт >> Строительство, проекты, дизайн >> Проектирование и дизайн интерьера >> Где встретиться переговорить?
    dp.callback_query.register(where_meeting, MyCallback.filter(F.foo == "where_meeting"))

    # Старт >> Строительство, проекты, дизайн >> Проектирование и дизайн интерьера >> Сколько стоит дизайн?
    dp.callback_query.register(price_design, MyCallback.filter(F.foo == "price_design"))

    # Старт >> Строительство, проекты, дизайн >> Проектирование и дизайн интерьера >> Из чего состоит дизайн?
    dp.callback_query.register(design_content, MyCallback.filter(F.foo == "design_content"))

    # Старт >> Строительство, проекты, дизайн >> Проектирование и дизайн интерьера >> Как долго делается дизайн?
    dp.callback_query.register(how_long_design, MyCallback.filter(F.foo == "how_long_design"))

    # Старт >> Строительство, проекты, дизайн >> Проектирование и дизайн интерьера >> Есть ли готовые варианты проектов?
    dp.callback_query.register(there_ready_variants, MyCallback.filter(F.foo == 'there_ready_variants'))
    # _________________________________________________________________________________________________________________

    # Старт >> Бизнес консультации
    dp.callback_query.register(biz_consultation, MyCallback.filter(F.foo == 'biz_cunsultation'))
    dp.message.register(what_exactly_help, MainState.field_activity)
    dp.message.register(send_request, MainState.which_help)
    dp.callback_query.register(send_request_continue, MyCallback.filter(F.foo == 'continue')) # В случае если клиент заполнил анкету не первый раз

    # Старт >> Бизнес консультации >> Мои соц. Сети
    dp.callback_query.register(my_social_network, MyCallback.filter(F.foo == 'my_social_network'))

    # Старт >> Бизнес консультации >> Кто я и чем могу быть полезен
    dp.callback_query.register(who_i_am, MyCallback.filter(F.foo == 'who_i_am'))

    # Старт >> Бизнес консультации (Удалить предыдущее сообщение)
    dp.callback_query.register(delete_message, MyCallback.filter(F.foo == 'delete_message'))
    # _________________________________________________________________________________________________________________

    # Отправить номер телефона
    dp.message.register(contact_handler, F.contact)

    # Написать менеджеру
    dp.message.register(write_manager, F.text == 'Написать менеджеру')

    # Консультация
    dp.callback_query.register(consultation, MyCallback.filter(F.foo == 'consultation'))

    # Сообщение без контекста
    dp.message.register(bot_answer.say_something)

    await bot.delete_webhook(drop_pending_updates=True)  # Удаляем сообщения, которые получил бот до запуска
    try:
        await dp.start_polling(bot)
    except Exception as e:
        loger.error("An error occurred: ", exc_info=True)

    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start_bot())
