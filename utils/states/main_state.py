from aiogram.fsm.state import StatesGroup, State


# Stage для создания сделки в Bitrix
class MainState(StatesGroup):
    field_activity = State()
    which_help = State()
    info = State()  # переменная, чтобы хранить экземпляр класса информации о клиенте для последующего его перенаса в кэш
    info_phone = State() # переменная, чтобы хранить экземпляр класса информации о клиенте когда он решил отправить номер телефона
    field_activity_question = State()
    which_help_question = State()
    send_request = State()
