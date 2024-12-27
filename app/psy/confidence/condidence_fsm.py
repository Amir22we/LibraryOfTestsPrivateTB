from aiogram.fsm.state import StatesGroup, State

class ConfidenceState(StatesGroup):
    QUESTION = State()
    RESULT = State()
