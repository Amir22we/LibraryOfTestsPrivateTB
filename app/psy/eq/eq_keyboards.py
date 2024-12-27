from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ei_questions = [
    {
        "text": "Вы замечаете, когда окружающие чувствуют себя неудобно?",
        "answers": [
            {"text": "Редко.", "score": 1},
            {"text": "Иногда.", "score": 2},
            {"text": "Часто замечаю.", "score": 3},
        ],
    },
    {
        "text": "Легко ли вы распознаёте свои эмоции?",
        "answers": [
            {"text": "Нет, мне это трудно.", "score": 1},
            {"text": "Иногда могу.", "score": 2},
            {"text": "Да, всегда.", "score": 3},
        ],
    },
    {
        "text": "Можете ли вы поддержать друга в трудной ситуации?",
        "answers": [
            {"text": "Не всегда.", "score": 1},
            {"text": "Иногда.", "score": 2},
            {"text": "Да, всегда готов поддержать.", "score": 3},
        ],
    },
    {
        "text": "Способны ли вы контролировать свои эмоции в стрессовых ситуациях?",
        "answers": [
            {"text": "Редко удаётся.", "score": 1},
            {"text": "Иногда получается.", "score": 2},
            {"text": "Да, я контролирую себя.", "score": 3},
        ],
    },
    {
        "text": "Вы стараетесь понять, почему другие люди поступают определённым образом?",
        "answers": [
            {"text": "Нет, редко об этом думаю.", "score": 1},
            {"text": "Иногда задумываюсь.", "score": 2},
            {"text": "Да, мне это интересно.", "score": 3},
        ],
    },
]

async def create_ei_keyboard(question_index: int) -> InlineKeyboardMarkup:
    if question_index < 0 or question_index >= len(ei_questions):
        raise ValueError(f"Некорректный индекс вопроса: {question_index}")

    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    for idx, answer in enumerate(ei_questions[question_index]["answers"]):
        keyboard.inline_keyboard.append([
            InlineKeyboardButton(
                text=answer["text"],
                callback_data=f"ei_answer_{question_index}_{idx}"
            )
        ])
    return keyboard
