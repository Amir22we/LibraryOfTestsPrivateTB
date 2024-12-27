from aiogram.fsm.state import StatesGroup, State

class AddictionState(StatesGroup):
    QUESTION = State()
    RESULT = State()
