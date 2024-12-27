from aiogram.fsm.state import StatesGroup, State

class AmirTestState(StatesGroup):
    QUESTION = State()
    RESULT = State()
