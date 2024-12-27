from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

gk_questions = [
    {
        "text": "Как называется самая большая планета в Солнечной системе?",
        "answers": [
            {"text": "Земля", "score": 1},
            {"text": "Юпитер", "score": 3},
            {"text": "Сатурн", "score": 2},
        ],
    },
    {
        "text": "Какое животное является символом Австралии?",
        "answers": [
            {"text": "Коала", "score": 2},
            {"text": "Кенгуру", "score": 3},
            {"text": "Эму", "score": 1},
        ],
    },
    {
        "text": "Сколько океанов на Земле?",
        "answers": [
            {"text": "Пять", "score": 3},
            {"text": "Четыре", "score": 2},
            {"text": "Три", "score": 1},
        ],
    },
    {
        "text": "Кто написал роман 'Война и мир'?",
        "answers": [
            {"text": "Фёдор Достоевский", "score": 1},
            {"text": "Лев Толстой", "score": 3},
            {"text": "Антон Чехов", "score": 2},
        ],
    },
    {
        "text": "Какой элемент обозначается символом 'O'?",
        "answers": [
            {"text": "Кислород", "score": 3},
            {"text": "Водород", "score": 2},
            {"text": "Азот", "score": 1},
        ],
    },
]

async def create_gk_keyboard(question_index: int) -> InlineKeyboardMarkup:
    if question_index < 0 or question_index >= len(gk_questions):
        raise ValueError(f"Некорректный индекс вопроса: {question_index}")

    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    for idx, answer in enumerate(gk_questions[question_index]["answers"]):
        keyboard.inline_keyboard.append([
            InlineKeyboardButton(
                text=answer["text"],
                callback_data=f"gk_answer_{question_index}_{idx}"
            )
        ])
    return keyboard
