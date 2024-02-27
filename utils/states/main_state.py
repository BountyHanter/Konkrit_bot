from aiogram.fsm.state import StatesGroup, State


# Stage для создания сделки в Bitrix
class MainState(StatesGroup):
    field_activity = State()
    which_help = State()
    info = State()  # переменная, чтобы хранить экземпляр класса информации о сделке для последующего его перенаса в кэш
