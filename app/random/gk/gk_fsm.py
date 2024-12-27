from aiogram.fsm.state import StatesGroup, State

class GeneralKnowledgeState(StatesGroup):
    QUESTION = State()
    RESULT = State()