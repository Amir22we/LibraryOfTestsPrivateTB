from aiogram.fsm.state import StatesGroup, State

class CatState(StatesGroup):
    QUESTION = State()
    RESULT = State()
