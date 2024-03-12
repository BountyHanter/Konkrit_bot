import json
import os
import time

from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, FSInputFile

from bot_messages.bot_answer_text import const_proj_des_starttext1, const_proj_des_starttext2, start_text1, \
    start_text2, construct_text, sale_biz_invest_text1, sale_biz_invest_text2, take_invest_proj2, take_invest_proj1, \
    biz_consult_text1, biz_consult_text2, sale_biz_learn_more_text, my_condition_text, how_i_sale_text, \
    service_price_text, price_condition_text, struct_work_text, where_office_text, where_look_product_text, \
    which_quality_text, how_pay_text, project_design_text, \
    how_price_project_text, feedback_text, what_is_project_text, there_ready_variants_text, how_long_text, \
    where_meeting_text, price_design_text, design_content_text, how_long_design_text, \
    send_request_text, my_social_network_text, who_i_am_text
# from client_actions.client_actions import actions
from keyboards.buttons import new_user_kb, user_kb
from keyboards.all_inline_buttons import start_buttons, build_proj_des_buttons, sale_biz_find_invest_buttons, \
    take_inv_proj_buttons, \
    sale_biz_learn_more_buttons, my_conslusion_back_buttons, how_i_sale_biz_buttons, project_design_btns, \
    biz_consultation_buttons, delete_message_buttons, \
    biz_consultation_answer_buttons
from keyboards import construct_inline_buttons as const_btns
from scipt import insert_backslashes
from utils.states.class_for_state import Info
from utils.states.main_state import MainState


# Сообщение без контекста
async def say_something(message: Message):
    """
    Функция обработки сообщений без контекста\n
    Это функция обработки входящих сообщений, которая активируется, когда бот не выполняет никаких других команд или
    функций.
    """
    if message.chat.type == 'private':
        await message.answer('*Извините, я еще не умею понимать простой текст*\.')


# Старт
async def start(message: Message, bot: Bot, state: FSMContext):
    """
    Функция обработки команды /start
    """
    if message.chat.type == 'private': # Чтобы бот не отвечал в группе\чате
        await state.clear()
        photo = FSInputFile(r'data/vadim.jpeg')
        await bot.send_photo(message.chat.id, photo=photo, caption=start_text1, reply_markup=user_kb)
        await message.answer(start_text2, reply_markup=start_buttons())  # Отправляем второе с inline клавиатурой
        # actions("Старт", message.from_user.id)


# Отработка старта по инлайн кнопке
async def inline_start(query: CallbackQuery, bot: Bot):
    """
    Функция обработки стартовой команды если пользователь нажал назад в одном из сообщений на которые ведёт эта функция
    """
    await bot.edit_message_reply_markup(query.from_user.id, query.message.message_id)  # удаляем кнопку
    if query.message.chat.type == 'private': # Чтобы бот не отвечал в группе\чате
        await query.message.answer(start_text2, reply_markup=start_buttons())  # Отправляем второе с inline клавиатурой
        # actions("Старт", query.message.from_user.id)


# Старт >> Продажа бизнеса и поиск инвестиций
async def sale_biz_invest(query: CallbackQuery, bot: Bot):
    """
    Функция реагирующая на каллбек - sale_biz, когда пользователь жмёт на inline-кнопку - Продажа бизнеса и поиск инвестиций

    Функция пишет первое сообщение, отправляет файл с перечню правил, через 3 секунды отправляет второе сообщение и соответствующие
    кнопки

    :param bot: Нужен для удаления инлайн кнопки.
    :param query: Использую query потому что функция регистрируется по каллбэку плюс могу отправлять файлы через query
    :return:
    """
    # actions("Старт >> Продажа бизнеса и поиск инвестиций", query.from_user.id)
    await bot.edit_message_reply_markup(query.from_user.id, query.message.message_id)  # удаляем кнопку
    await query.message.answer(sale_biz_invest_text1)
    document = FSInputFile(r'bot_logs.json', filename='Имя файла')
    await query.message.answer_document(document=document)
    time.sleep(3)
    await query.message.answer(sale_biz_invest_text2, reply_markup=sale_biz_find_invest_buttons())


# Старт >> Продажа бизнеса и поиск инвестиций >> Узнать больше
async def sale_biz_learn_more(query: CallbackQuery, bot: Bot):
    await bot.edit_message_reply_markup(query.from_user.id, query.message.message_id)  # удаляем кнопку
    await query.message.answer(sale_biz_learn_more_text, reply_markup=sale_biz_learn_more_buttons())
    # actions("Старт >> Продажа бизнеса и поиск инвестиций >> Узнать больше", query.message.from_user.id)


# Старт >> Продажа бизнеса и поиск инвестиций >> Узнать больше >> Мои обязательные условия
async def my_condition(query: CallbackQuery, bot: Bot):
    await bot.edit_message_reply_markup(query.from_user.id, query.message.message_id)  # удаляем кнопку
    await query.message.answer(my_condition_text, reply_markup=my_conslusion_back_buttons())
    # actions("Старт >> Продажа бизнеса и поиск инвестиций >> Узнать больше >> Мои обязательные условия",
           # query.message.from_user.id)


# Старт >> Продажа бизнеса и поиск инвестиций >> Узнать больше >> Как я продаю готовые бизнесы
async def how_i_sale_biz(query: CallbackQuery, bot: Bot):
    await bot.edit_message_reply_markup(query.from_user.id, query.message.message_id)  # удаляем кнопку
    await query.message.answer(how_i_sale_text, reply_markup=how_i_sale_biz_buttons())
    #actions("Старт >> Продажа бизнеса и поиск инвестиций >> Узнать больше >> Как я продаю готовые бизнесы",
          #  query.from_user.id)


# Старт >> Продажа бизнеса и поиск инвестиций >> Узнать больше >> Стоимость услуг
async def service_price(query: CallbackQuery, bot: Bot):
    await bot.edit_message_reply_markup(query.from_user.id, query.message.message_id)  # удаляем кнопку
    await query.message.answer(service_price_text, reply_markup=how_i_sale_biz_buttons())
    #actions("Старт >> Продажа бизнеса и поиск инвестиций >> Узнать больше >> Стоимость услуг",
          #  query.from_user.id)


# ______________________________________________________________________________________________________________________

# Старт >> Подбор инвест. проекта
async def take_invest_proj(query: CallbackQuery, bot: Bot):
    await query.answer()
    await bot.edit_message_reply_markup(query.from_user.id, query.message.message_id)  # удаляем кнопку
    await query.message.answer(take_invest_proj1)
    document = FSInputFile(r'bot_logs.json', filename='Имя файла')
    await query.message.answer_document(document=document)
    time.sleep(3)
    await query.message.answer(take_invest_proj2, reply_markup=take_inv_proj_buttons())
   # actions("Старт >> Подбор инвест. проекта",
          #  query.from_user.id)


# Старт >> Подбор инвест. проекта >> Цены и условия работы
async def price_condition(query: CallbackQuery):
    await query.answer()
    await query.message.answer(price_condition_text, reply_markup=delete_message_buttons())  # не удаляем кнопки выше так как текст маленький
    #actions("Старт >> Подбор инвест. проекта >> Цены и условия работы",
          #  query.from_user.id)


# Старт >> Подбор инвест. проекта >> Структура работы
async def struct_work(query: CallbackQuery, bot: Bot):
    await query.answer()
    await query.message.answer(struct_work_text, reply_markup=delete_message_buttons())

#_______________________________________________________________________________________________________________________
# Старт >> Строительство, проекты, дизайн
async def construct_proj_design_start(query: CallbackQuery, bot: Bot):
    """
    Функция реагирующая на каллбек - bild_proj, когда пользователь жмёт на inline-кнопку - Строительство, проекты, дизайн.

    Функция пишет первое сообщение, отправляет файл-методичку, через 3 секунды отправляет второе сообщение и соответствующие
    кнопки.
    :param query: Использую query потому что функция регистрируется по каллбэку плюс могу отправлять файлы через query
    """
    # Удаляем кнопку в сообщении которое запустило эту функцию
    await bot.edit_message_reply_markup(query.from_user.id, query.message.message_id)  # удаляем кнопку
    # await bot.edit_message_reply_markup(query.from_user.id, query.message.message_id)
    await query.message.answer(const_proj_des_starttext1)
    document = FSInputFile(r'bot_logs.json', filename='Имя файла')
    await query.message.answer_document(document=document)
    time.sleep(3)
    await query.message.answer(const_proj_des_starttext2, reply_markup=build_proj_des_buttons())


# Старт >> Строительство, проекты, дизайн >> Стройматериалы

async def construct(query: CallbackQuery, bot: Bot):
    await bot.edit_message_reply_markup(query.from_user.id, query.message.message_id)  # удаляем кнопку
    await query.message.answer(construct_text, reply_markup=const_btns.start_construct())


# Старт >> Строительство, проекты, дизайн >> Стройматериалы >> Где офис?
async def where_office(query: CallbackQuery, bot: Bot):
    await bot.edit_message_reply_markup(query.from_user.id, query.message.message_id)  # удаляем кнопку
    await query.message.answer(where_office_text, reply_markup=const_btns.one())


# Старт >> Строительство, проекты, дизайн >> Стройматериалы >> Где посмотреть товар?
async def where_look_product(query: CallbackQuery, bot: Bot):
    await bot.edit_message_reply_markup(query.from_user.id, query.message.message_id)  # удаляем кнопку
    await query.message.answer(where_look_product_text, reply_markup=const_btns.two())

# Старт >> Строительство, проекты, дизайн >> Стройматериалы >> Качество товаров
async def which_quality(query: CallbackQuery, bot: Bot):
    await bot.edit_message_reply_markup(query.from_user.id, query.message.message_id)  # удаляем кнопку
    await query.message.answer(which_quality_text, reply_markup=const_btns.three())


# Старт >> Строительство, проекты, дизайн >> Стройматериалы >> Как оплатить?
async def how_pay(query: CallbackQuery, bot: Bot):
    await bot.edit_message_reply_markup(query.from_user.id, query.message.message_id)  # удаляем кнопку
    await query.message.answer(how_pay_text, reply_markup=const_btns.four())


# Старт >> Строительство, проекты, дизайн >> Проектирование и дизайн интерьера
async def project_design(query: CallbackQuery, bot: Bot):
    await query.answer()
    await bot.edit_message_reply_markup(query.from_user.id, query.message.message_id)  # удаляем кнопку
    await query.message.answer(project_design_text, reply_markup=project_design_btns())


# Старт >> Строительство, проекты, дизайн >> Проектирование и дизайн интерьера >> Сколько стоит проект?
async def how_price_project(query: CallbackQuery):
    await query.answer()
    await query.message.answer(how_price_project_text+feedback_text, reply_markup=delete_message_buttons()) # Здесь так же удаляем текст так как не стоит каждый раз выводить весь текст предыдущего сообщения заного, кнопки не удаляем


# Старт >> Строительство, проекты, дизайн >> Проектирование и дизайн интерьера >> Из чего состоит проект?
async def what_is_project(query: CallbackQuery):
    await query.answer()
    await query.message.answer(what_is_project_text+feedback_text, reply_markup=delete_message_buttons())


# Старт >> Строительство, проекты, дизайн >> Проектирование и дизайн интерьера >> Есть ли готовые варианты проектов?
async def there_ready_variants(query: CallbackQuery):
    await query.answer()
    await query.message.answer(there_ready_variants_text+feedback_text, reply_markup=delete_message_buttons())


# Старт >> Строительство, проекты, дизайн >> Проектирование и дизайн интерьера >> Как долго делается?
async def how_long(query: CallbackQuery):
    await query.answer()
    await query.message.answer(how_long_text+feedback_text, reply_markup=delete_message_buttons())


# Старт >> Строительство, проекты, дизайн >> Проектирование и дизайн интерьера >> Где встретиться переговорить?
async def where_meeting(query: CallbackQuery):
    await query.answer()
    await query.message.answer(where_meeting_text+feedback_text, reply_markup=delete_message_buttons())


# Старт >> Строительство, проекты, дизайн >> Проектирование и дизайн интерьера >> Сколько стоит дизайн?
async def price_design(query: CallbackQuery):
    await query.answer()
    await query.message.answer(price_design_text+feedback_text, reply_markup=delete_message_buttons())


# Старт >> Строительство, проекты, дизайн >> Проектирование и дизайн интерьера >> Из чего состоит дизайн?
async def design_content(query: CallbackQuery):
    await query.answer()
    await query.message.answer(design_content_text+feedback_text, reply_markup=delete_message_buttons())


# Старт >> Строительство, проекты, дизайн >> Проектирование и дизайн интерьера >> Как долго делается дизайн?
async def how_long_design(query: CallbackQuery):
    await query.answer()
    await query.message.answer(how_long_design_text+feedback_text, reply_markup=delete_message_buttons())


# Старт >> Бизнес консультации
async def biz_consultation(query: CallbackQuery, state: FSMContext, bot: Bot):
    """
    Сначала проверяем заполнял ли юзер анкету, если нет то отправляем на заполнение, если да то предлагаем выбор - заполнить заного или продолжить
    :param query:
    :param state:
    :return:
    """
    await bot.edit_message_reply_markup(query.from_user.id, query.message.message_id)  # удаляем кнопку
    new_user = True
    file_path = 'clients_data.json'
    with open(file_path, 'r', encoding='utf-8') as file:
        # Пытаемся загрузить данные из файла
        data = json.load(file)
        for i, key in enumerate(data):
            if key['user_id'] == query.from_user.id:
                if key['what_help_need'] is not None:
                    new_user = False
                    await query.message.answer('Вы уже заполняли анкету', reply_markup=biz_consultation_answer_buttons())
    if new_user is True:
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
    await message.answer(f"Это сфера деятельности \- {info.field_activity}, а это с чем нужна помощь \- {info.which_help}"
                         f"Спасибо за ваш ответ\.", reply_markup=new_user_kb)
    await state.clear()
    send_data_to_cache(user_id=message.from_user.id, sphere_activity=info.field_activity, what_help_need=info.which_help)
    await message.answer(send_request_text, reply_markup=biz_consultation_buttons())


# Отрабатывает когда пользователь уже заполнял анкету и не стал заполнять заного
async def send_request_continue(query: CallbackQuery, bot: Bot):
    await bot.edit_message_reply_markup(query.from_user.id, query.message.message_id)  # удаляем кнопку
    await query.message.answer(send_request_text, reply_markup=biz_consultation_buttons())


# Старт >> Бизнес консультации >> Мои соц. Сети
async def my_social_network(query: CallbackQuery):
    await query.answer()
    await query.message.answer(my_social_network_text, reply_markup=delete_message_buttons())


# Старт >> Бизнес консультации >> Кто я и чем могу быть полезен
async def who_i_am(query: CallbackQuery):
    await query.answer()
    await query.message.answer(who_i_am_text, reply_markup=delete_message_buttons())


# Старт >> Бизнес консультации (удалить сообщение)
async def delete_message(query: CallbackQuery, bot: Bot):
    await bot.delete_message(query.message.chat.id, query.message.message_id)


# Получаем номер телефона
async def contact_handler(message: Message, bot: Bot):
    if message.contact is not None:
        # Получаем номер телефона
        phone_number = message.contact.phone_number
        send_data_to_cache(user_id=message.from_user.id, telephone_number=phone_number)
        print('Отработано')
        file_path = 'clients_data.json'
        with open(file_path, 'r', encoding='utf-8') as file:
            # Пытаемся загрузить данные из файла
            data = json.load(file)
            for i, key in enumerate(data):
                if key['user_id'] == message.from_user.id:
                    if key['what_help_need'] is not None:
                        await bot.send_message(977249859,
                                               f'Пользователь с номером \+{key["telephone_number"]} запрашивает консультацию\. Его информация:\n'
                                               f'Сфера деятельности: {key["sphere_activity"]}\n'
                                               f'С чем нужна помощь: {key["what_help_need"]}')
                        await message.answer("Отлично, ваш номер получен, заявка отправлена", reply_markup=user_kb)
                        return
    else:
        await message.answer("Простите, бот не смог получить ваш номер телефона, обратитесь к администрации\. \!\!\!Не удаляйте переписку с ботом\!\!\!")


# Написать менеджеру
async def write_manager(message: Message):
    await message.answer('Хорошо, вот контакты менеджера \- \@HelperCompBot')
"""
# Порешать проблему когда чел уже заказывал консультацию он жмёт еще раз заказать консультацию и его пересылает в эту функцию а должно пересылать в send_order_consultation
# Заказать консультацию
async def take_field_activity_question(query: CallbackQuery, state: FSMContext):
    file_path = 'clients_data.json'
    with open(file_path, 'r', encoding='utf-8') as file:
        # Пытаемся загрузить данные из файла
        data = json.load(file)
        for i, key in enumerate(data):
            if key['user_id'] == query.from_user.id:
                if key['what_help_need'] is not None:
                    await query.message.answer('Вы уже отправили заявку, если что то случилось, нажмите кнопку \- Написать менеджеру и сообщите ему детали')
                    return
    info = Info()
    await state.update_data(info_phone=info)  # Переносим экземпляр в машину состояний
    await query.message.answer('Хорошо, для начала скажите, какая у вас сфера деятельности?\n')
    await state.set_state(MainState.field_activity_question) """


# Получили первый ответ
async def take_which_help_question(message: Message, state: FSMContext):
    fine_text = insert_backslashes(message.text)
    await state.update_data(field_activity_question=fine_text)
    get_data = await state.get_data()
    info = get_data.get('info_phone')
    info.field_activity_question = get_data.get('field_activity_question')
    await state.update_data(info_phone=info)
    await message.answer('Понял, а с чем именно вам нужна помощь?')
    await state.set_state(MainState.which_help_question)


# Получили второй ответ
async def send_order_consultation(message: Message, state: FSMContext, bot: Bot):
    fine_text = insert_backslashes(message.text)
    await state.update_data(which_help_question=fine_text)
    get_data = await state.get_data()
    info = get_data.get('info_phone')
    info.which_help_question = get_data.get('which_help_question')
    await state.update_data(info_phone=info)
    send_data_to_cache(user_id=message.from_user.id, sphere_activity=info.field_activity_question, what_help_need=info.which_help_question)
    """#await state.set_state(MainState.send_request)
    result_data = None
    file_path = 'clients_data.json'
    with open(file_path, 'r', encoding='utf-8') as file:
        # Пытаемся загрузить данные из файла
        data = json.load(file)
        for i, key in enumerate(data):
            if key['user_id'] == message.from_user.id:
                result_data = data[i]

    await bot.send_message(977249859, f'Пользователь с номером \+{result_data["telephone_number"]} запрашивает консультацию\. Его информация:\n'
                                       f'Сфера деятельности: {result_data["sphere_activity"]}\n'
                                       f'С чем нужна помощь: {result_data["what_help_need"]}')
    await message.answer(f'Отлично,{message.from_user.username}')"""


# Отправка информации в файл
def send_data_to_cache(*, user_id=None, telephone_number=None, sphere_activity=None, what_help_need=None, send_manager=False):
    file_path = 'clients_data.json'
    data_to_add = {'user_id': user_id, 'telephone_number': telephone_number, 'sphere_activity': sphere_activity, 'what_help_need': what_help_need, 'send_manager': send_manager}
    # Проверяем, существует ли файл
    if os.path.exists(file_path):
        # Файл существует, проверяем, не пустой ли он
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                # Пытаемся загрузить данные из файла
                data = json.load(file)
        except json.JSONDecodeError:
            # Если файл пустой или содержит невалидный JSON, начинаем с новым списком
            data = []
        except Exception as e:
            print(f"Произошла ошибка при чтении файла: {e}")
            data = []
    else:
        # Файл не существует, начинаем с новым списком
        data = []

    # Поиск и обновление данных, если user_id найден
    user_found = False
    for i, record in enumerate(data):
        if record.get('user_id') == user_id:
            # Обновляем данные для существующего user_id только если значение не None
            for key, value in data_to_add.items():
                if value is not None:
                    record[key] = value
            data[i] = record
            user_found = True
            break

    if not user_found:
        # Добавляем новый словарь, если user_id не найден
        data.append(data_to_add)

    # Сохраняем обновленные данные обратно в файл
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
