from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

cat_questions = [
    {
        "text": "Как ты проводишь время?",
        "answers": [
            {"text": "Сплю весь день.", "score": 1},
            {"text": "Играю с друзьями.", "score": 2},
            {"text": "Делюсь мемами о котах.", "score": 3},
            {"text": "Лежу, как король.", "score": 4},
        ],
    },
    {
        "text": "Какой твой любимый звук?",
        "answers": [
            {"text": "Мурчание.", "score": 1},
            {"text": "Шуршание пакета.", "score": 2},
            {"text": "Звук открывающейся еды.", "score": 3},
            {"text": "Тишина.", "score": 4},
        ],
    },
    {
        "text": "Где бы ты жил?",
        "answers": [
            {"text": "На мягком диване.", "score": 1},
            {"text": "В коробке.", "score": 2},
            {"text": "В интернет-мемах.", "score": 3},
            {"text": "В дворце.", "score": 4},
        ],
    },
    {
        "text": "Что ты делаешь в свободное время?",
        "answers": [
            {"text": "Мурлычу.", "score": 1},
            {"text": "Играю.", "score": 2},
            {"text": "Лазаю по мемам.", "score": 3},
            {"text": "Принимаю поклонения.", "score": 4},
        ],
    },
    {
        "text": "Что ты любишь есть?",
        "answers": [
            {"text": "Кошачий корм.", "score": 1},
            {"text": "Что-нибудь вкусное.", "score": 2},
            {"text": "Людскую еду.", "score": 3},
            {"text": "Что захочу!", "score": 4},
        ],
    },
]

async def create_cat_keyboard(question_index: int) -> InlineKeyboardMarkup:
    if question_index < 0 or question_index >= len(cat_questions):
        raise ValueError(f"Некорректный индекс вопроса: {question_index}")

    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    for idx, answer in enumerate(cat_questions[question_index]["answers"]):
        keyboard.inline_keyboard.append([
            InlineKeyboardButton(
                text=answer["text"],
                callback_data=f"cat_answer_{question_index}_{idx}"
            )
        ])
    return keyboard
