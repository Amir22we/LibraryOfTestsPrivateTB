from aiogram.fsm.state import StatesGroup, State

class EmotionalIntelligenceState(StatesGroup):
    QUESTION = State()
    RESULT = State()
