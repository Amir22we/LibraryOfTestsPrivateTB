from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

confidence_questions = [
    {
        "text": "Чувствуете ли вы себя уверенно, когда принимаете важные решения?",
        "answers": [
            {"text": "Нет, боюсь ошибиться.", "score": 1},
            {"text": "Иногда сомневаюсь.", "score": 2},
            {"text": "Да, всегда уверен.", "score": 3},
        ],
    },
    {
        "text": "Легко ли вам выражать своё мнение в компании людей?",
        "answers": [
            {"text": "Нет, мне трудно.", "score": 1},
            {"text": "Иногда получается.", "score": 2},
            {"text": "Да, я свободно высказываюсь.", "score": 3},
        ],
    },
    {
        "text": "Чувствуете ли вы себя спокойно, сталкиваясь с трудностями?",
        "answers": [
            {"text": "Нет, я нервничаю.", "score": 1},
            {"text": "Иногда сохраняю спокойствие.", "score": 2},
            {"text": "Да, остаюсь спокойным.", "score": 3},
        ],
    },
    {
        "text": "Можете ли вы вдохновить других своим примером?",
        "answers": [
            {"text": "Нет, редко.", "score": 1},
            {"text": "Иногда.", "score": 2},
            {"text": "Да, часто вдохновляю.", "score": 3},
        ],
    },
    {
        "text": "Чувствуете ли вы себя комфортно в новых ситуациях?",
        "answers": [
            {"text": "Нет, избегаю их.", "score": 1},
            {"text": "Иногда могу адаптироваться.", "score": 2},
            {"text": "Да, легко адаптируюсь.", "score": 3},
        ],
    },
]

async def create_confidence_keyboard(question_index: int) -> InlineKeyboardMarkup:
    if question_index < 0 or question_index >= len(confidence_questions):
        raise ValueError(f"Некорректный индекс вопроса: {question_index}")

    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    for idx, answer in enumerate(confidence_questions[question_index]["answers"]):
        keyboard.inline_keyboard.append([
            InlineKeyboardButton(
                text=answer["text"],
                callback_data=f"confidence_answer_{question_index}_{idx}"
            )
        ])
    return keyboard
