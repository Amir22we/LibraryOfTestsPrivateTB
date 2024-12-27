from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

amir_questions = [
    {
        "text": "Кто такой Амир?",
        "answers": [
            {"text": "Человек", "score": 3},
            {"text": "Супер человек", "score": 1},
            {"text": "Чиловый человек", "score": 2},
        ],
    },
    {
        "text": "Зачем вообще зашли сюда?",
        "answers": [
            {"text": "Ты заставил._.", "score": 1},
            {"text": "Я чиловый парень", "score": 3},
            {"text": "...", "score": 2},
        ],
    },
    {
        "text": "Что я люблю?",
        "answers": [
            {"text": "Шоколад", "score": 2},
            {"text": "Соль", "score": 3},
            {"text": "Банан", "score": 1},
        ],
    },
    {
        "text": "Да",
        "answers": [
            {"text": "Да", "score": 1},
            {"text": "Да", "score": 3},
            {"text": "Да", "score": 2},
        ],
    },
    {
        "text": "Как думаешь... Я тебя люблю или нет?(если даже ты мужик)",
        "answers": [
            {"text": "Да", "score": 2},
            {"text": "Не знаю...(ДА!)", "score": 3},
            {"text": "Нет!(ДАААА!)", "score": 1},
        ],
    },
]

async def create_amir_keyboard(question_index: int) -> InlineKeyboardMarkup:
    if question_index < 0 or question_index >= len(amir_questions):
        raise ValueError(f"Некорректный индекс вопроса: {question_index}")

    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    for idx, answer in enumerate(amir_questions[question_index]["answers"]):
        keyboard.inline_keyboard.append([
            InlineKeyboardButton(
                text=answer["text"],
                callback_data=f"amir_answer_{question_index}_{idx}"
            )
        ])
    return keyboard
