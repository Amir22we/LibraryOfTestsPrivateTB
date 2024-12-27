from aiogram.fsm.state import StatesGroup, State

class ZucchiniState(StatesGroup):
    QUESTION = State()
    RESULT = State()    