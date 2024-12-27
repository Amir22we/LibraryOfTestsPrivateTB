from aiogram.fsm.state import StatesGroup, State

class CringeState(StatesGroup):
    QUESTION = State()
    RESULT = State()
