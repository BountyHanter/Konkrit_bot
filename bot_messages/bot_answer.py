import json
import os
import time

from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, InputFile, FSInputFile, ReplyKeyboardMarkup, KeyboardButton

from bot_messages.bot_answer_text import const_proj_des_starttext1, const_proj_des_starttext2, start_text1, \
    start_text2, construct_text, sale_biz_invest_text1, sale_biz_invest_text2, take_invest_proj2, take_invest_proj1, \
    biz_consult_text1, biz_consult_text2, sale_biz_learn_more_text, my_condition_text, how_i_sale_text, \
    service_price_text, price_condition_text, struct_work_text, where_office_text, where_look_product_text, \
    which_quality_text, is_product_text, how_much_deliver_text, how_pay_text, project_design_text, \
    how_price_project_text, feedback_text, what_is_project_text, there_ready_variants_text, how_long_text, \
    where_meeting_text, price_design_text, design_content_text, how_long_design_text, project_examples_text, \
    send_request_text, my_social_network_text, who_i_am_text, how_much_services_text
from keyboards.buttons import main_kb
from keyboards.all_inline_buttons import start_buttons, build_proj_des_buttons, sale_biz_find_invest_buttons, \
    take_inv_proj_buttons, \
    sale_biz_learn_more_buttons, my_conslusion_back_buttons, how_i_sale_biz_buttons, project_design_btns, \
    proj_design_feedback_buttons, biz_consultation_buttons, who_i_am_buttons
from keyboards import construct_inline_buttons as const_btns
from utils.states.class_for_state import Info
from utils.states.main_state import MainState


# Сообщение без контекста
async def say_something(message: Message):
    """
    Функция обработки сообщений без контекста\n
    Это функция обработки входящих сообщений, которая активируется, когда бот не выполняет никаких других команд или
    функций.
    """
    await message.answer('*Извините, я еще не умею понимать простой текст*\.')


# Старт
async def start(message: Message):
    """
    Функция обработки команды /start
    """
    await message.answer(start_text1, reply_markup=main_kb)  # Отправляем первое сообщение с клавиатурой
    await message.answer(start_text2, reply_markup=start_buttons())  # Отправляем второе с inline клавиатурой


# Старт >> Продажа бизнеса и поиск инвестиций
async def sale_biz_invest(query: CallbackQuery):
    """
    Функция реагирующая на каллбек - sale_biz, когда пользователь жмёт на inline-кнопку - Продажа бизнеса и поиск инвестиций

    Функция пишет первое сообщение, отправляет файл с перечню правил, через 3 секунды отправляет второе сообщение и соответствующие
    кнопки

    :param query: Использую query потому что функция регистрируется по каллбэку плюс могу отправлять файлы через query
    :return:
    """
    await query.message.answer(sale_biz_invest_text1)
    document = FSInputFile(r'bot_logs.json', filename='Имя файла')
    await query.message.answer_document(document=document)
    time.sleep(1)  # !!!!!!!!!!!!!!!ИСПРАВИТЬ НА 3!!!!!!!!!!!!!!!
    await query.message.answer(sale_biz_invest_text2, reply_markup=sale_biz_find_invest_buttons())


# Старт >> Продажа бизнеса и поиск инвестиций >> Узнать больше
async def sale_biz_learn_more(query: CallbackQuery):
    await query.message.answer(sale_biz_learn_more_text, reply_markup=sale_biz_learn_more_buttons())


# Старт >> Продажа бизнеса и поиск инвестиций >> Узнать больше >> Мои обязательные условия
async def my_condition(query: CallbackQuery):
    await query.message.answer(my_condition_text, reply_markup=my_conslusion_back_buttons())


# Старт >> Продажа бизнеса и поиск инвестиций >> Узнать больше >> Как я продаю готовые бизнесы
async def how_i_sale_biz(query: CallbackQuery):
    await query.message.answer(how_i_sale_text, reply_markup=how_i_sale_biz_buttons())


# Старт >> Продажа бизнеса и поиск инвестиций >> Узнать больше >> Стоимость услуг
async def service_price(query: CallbackQuery):
    await query.message.answer(service_price_text)  # Здесь кнопки не удаляем так как маленький текст


# ______________________________________________________________________________________________________________________

# Старт >> Подбор инвест. проекта
async def take_invest_proj(query: CallbackQuery):
    await query.message.answer(take_invest_proj1)
    document = FSInputFile(r'bot_logs.json', filename='Имя файла')
    await query.message.answer_document(document=document)
    time.sleep(3)
    await query.message.answer(take_invest_proj2, reply_markup=take_inv_proj_buttons())


# Старт >> Подбор инвест. проекта >> Цены и условия работы
async def price_condition(query: CallbackQuery):
    await query.message.answer(price_condition_text)  # не удаляем кнопку и не добавляем так как текст маленький


# Старт >> Подбор инвест. проекта >> Структура работы
async def struct_work(query: CallbackQuery):
    await query.message.answer(struct_work_text)


# Старт >> Строительство, проекты, дизайн
async def construct_proj_design_start(query: CallbackQuery):
    """
    Функция реагирующая на каллбек - bild_proj, когда пользователь жмёт на inline-кнопку - Строительство, проекты, дизайн.

    Функция пишет первое сообщение, отправляет файл-методичку, через 3 секунды отправляет второе сообщение и соответствующие
    кнопки.
    :param query: Использую query потому что функция регистрируется по каллбэку плюс могу отправлять файлы через query
    """
    # Удаляем кнопку в сообщении которое запустило эту функцию
    # await bot.edit_message_reply_markup(query.from_user.id, query.message.message_id)
    await query.message.answer(const_proj_des_starttext1)
    document = FSInputFile(r'bot_logs.json', filename='Имя файла')
    await query.message.answer_document(document=document)
    time.sleep(3)
    await query.message.answer(const_proj_des_starttext2, reply_markup=build_proj_des_buttons())


# Старт >> Строительство, проекты, дизайн >> Строительство

async def construct(query: CallbackQuery):
    await query.message.answer(construct_text, reply_markup=const_btns.start_construct())


# Старт >> Строительство, проекты, дизайн >> Стройматериалы >> Где офис?
async def where_office(query: CallbackQuery):
    await query.message.answer(where_office_text, reply_markup=const_btns.one())


# Старт >> Строительство, проекты, дизайн >> Стройматериалы >> Где посмотреть товар?
async def where_look_product(query: CallbackQuery):
    await query.message.answer(where_look_product_text, reply_markup=const_btns.two())


# Старт >> Строительство, проекты, дизайн >> Стройматериалы >> Есть ли товар в наличии, если нет сколько ждать
async def is_product(query: CallbackQuery):
    await query.message.answer(is_product_text, reply_markup=const_btns.three())


# Старт >> Строительство, проекты, дизайн >> Стройматериалы >> Сколько стоит доставка
async def how_much_deliver(query: CallbackQuery):
    await query.message.answer(how_much_deliver_text, reply_markup=const_btns.four())


# Старт >> Строительство, проекты, дизайн >> Стройматериалы >> Качество товаров
async def which_quality(query: CallbackQuery):
    await query.message.answer(which_quality_text, reply_markup=const_btns.five())


# Старт >> Строительство, проекты, дизайн >> Стройматериалы >> Как оплатить?
async def how_pay(query: CallbackQuery):
    await query.message.answer(how_pay_text, reply_markup=const_btns.six())


# Старт >> Строительство, проекты, дизайн >> Проектирование и дизайн интерьера
async def project_design(query: CallbackQuery):
    await query.message.answer(project_design_text, reply_markup=project_design_btns())


# Старт >> Строительство, проекты, дизайн >> Проектирование и дизайн интерьера >> Сколько стоит проект?
async def how_price_project(query: CallbackQuery):
    await query.message.answer(how_price_project_text+feedback_text, reply_markup=proj_design_feedback_buttons())


# Старт >> Строительство, проекты, дизайн >> Проектирование и дизайн интерьера >> Из чего состоит проект?
async def what_is_project(query: CallbackQuery):
    await query.message.answer(what_is_project_text+feedback_text, reply_markup=proj_design_feedback_buttons())


# Старт >> Строительство, проекты, дизайн >> Проектирование и дизайн интерьера >> Есть ли готовые варианты проектов?
async def there_ready_variants(query: CallbackQuery):
    await query.message.answer(there_ready_variants_text+feedback_text, reply_markup=proj_design_feedback_buttons())


# Старт >> Строительство, проекты, дизайн >> Проектирование и дизайн интерьера >> Как долго делается?
async def how_long(query: CallbackQuery):
    await query.message.answer(how_long_text+feedback_text, reply_markup=proj_design_feedback_buttons())


# Старт >> Строительство, проекты, дизайн >> Проектирование и дизайн интерьера >> Где встретиться переговорить?
async def where_meeting(query: CallbackQuery):
    await query.message.answer(where_meeting_text+feedback_text, reply_markup=proj_design_feedback_buttons())


# Старт >> Строительство, проекты, дизайн >> Проектирование и дизайн интерьера >> Сколько стоит дизайн?
async def price_design(query: CallbackQuery):
    await query.message.answer(price_design_text+feedback_text, reply_markup=proj_design_feedback_buttons())


# Старт >> Строительство, проекты, дизайн >> Проектирование и дизайн интерьера >> Из чего состоит дизайн?
async def design_content(query: CallbackQuery):
    await query.message.answer(design_content_text+feedback_text, reply_markup=proj_design_feedback_buttons())


# Старт >> Строительство, проекты, дизайн >> Проектирование и дизайн интерьера >> Как долго делается дизайн?
async def how_long_design(query: CallbackQuery):
    await query.message.answer(how_long_design_text+feedback_text, reply_markup=proj_design_feedback_buttons())


# Старт >> Строительство, проекты, дизайн >> Проектирование и дизайн интерьера >> Есть примеры работ по дизайну?
async def project_examples(query: CallbackQuery):
    await query.message.answer(project_examples_text, reply_markup=proj_design_feedback_buttons())


# Старт >> Бизнес консультации
async def biz_consultation(query: CallbackQuery, state: FSMContext):
    info = Info()
    await state.update_data(info=info)  # Переносим экземпляр в машину состояний
    await query.message.answer(biz_consult_text1)
    document = FSInputFile(r'bot_logs.json', filename='Имя файла')
    await query.message.answer_document(document=document)
    time.sleep(3)
    await query.message.answer(biz_consult_text2)
    await state.set_state(MainState.field_activity)
    await query.message.answer('Какая у вас сфера деятельности?')


async def what_exactly_help(message: Message, state: FSMContext):
    """
    Здесь я использую машину состояний.
    В начале я обновляю параметр в машине состояний field_activity, я присваиваю ему то что отправляет пользователь.
    Далее я создаю переменную get_data и помещаю в нее класс state.
    Создаю параметр info и помещаю туда экземпляр класса, он находится в info в классе машины состояний.
    Потом я помещаю в параметр класса field_activity данные из класса машины состояний с аналогичным названием.
    Обновляю экземпляр класса в машине состояний.
    Переключаю машину состояний на следующий элемент
    """
    await state.update_data(field_activity=message.text)
    get_data = await state.get_data()
    info = get_data.get('info')
    info.field_activity = get_data.get('field_activity')
    await state.update_data(info=info)  # обновляем info в state
    await state.set_state(MainState.which_help)
    await message.answer('Понял, а с чем именно нужна помощь?')


async def send_request(message: Message, state: FSMContext):
    """
    То же самое что и в предыдущей функции.
    """
    await state.update_data(which_help=message.text)
    get_data = await state.get_data()
    info = get_data.get('info')
    info.which_help = get_data.get('which_help')
    await state.update_data(info=info)  # обновляем info в state
    await message.answer(f"Это сфера деятельности \- {info.field_activity}, а это с чем нужна помощь \- {info.which_help}")
    await message.answer(send_request_text, reply_markup=biz_consultation_buttons())


# Старт >> Бизнес консультации >> Мои соц. Сети
async def my_social_network(query: CallbackQuery):
    await query.message.answer(my_social_network_text)


# Старт >> Бизнес консультации >> Кто я и чем могу быть полезен
async def who_i_am(query: CallbackQuery):
    await query.message.answer(who_i_am_text, reply_markup=who_i_am_buttons())


# Старт >> Бизнес консультации >> Сколько стоят услуги
async def how_much_services(query: CallbackQuery):
    await query.message.answer(how_much_services_text)


# Получаем номер телефона
async def contact_handler(message: Message):
    if message.contact is not None:
        # Получаем номер телефона
        phone_number = message.contact.phone_number
        await message.answer(f"Спасибо\! Мы получили ваш номер телефона: {phone_number}")
    else:
        await message.answer("Простите, бот не смог получить ваш номер телефона, обратитесь к администрации")

        """    file_path = 'clients_data.json'
            # Проверяем, существует ли файл
            if os.path.exists(file_path):
                # Файл существует, проверяем, не пустой ли он
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        # Пытаемся загрузить данные из файла
                        data = json.load(file)
                        # Проверяем, не пустой ли список данных
                        if data:
                            # Если список не пустой, добавляем данные
                            data.append(data_to_add)
                        else:
                            # Если список пустой, создаем список с данными
                            data = [data_to_add]
                except json.JSONDecodeError:
                    # Если файл пустой или содержит невалидный JSON, начинаем с новым списком
                    data = [data_to_add]
                except Exception as e:
                    print(f"Произошла ошибка при чтении файла: {e}")
                    data = [data_to_add]
            else:
                # Файл не существует, начинаем с новым списком
                data = [data_to_add]

            # Сохраняем обновленные данные обратно в файл
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)"""


# Написать менеджеру
async def write_manager(message: Message):
    await message.answer('Хорошо, вот контакты менеджера \- \@Vindma2903')


