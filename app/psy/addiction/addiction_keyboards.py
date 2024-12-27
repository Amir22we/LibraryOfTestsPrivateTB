from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

addiction_questions = [
    {
        "text": "Часто ли вы испытываете потребность в играх, алкоголе или другом, чтобы расслабиться?",
        "answers": [
            {"text": "Нет, почти никогда.", "score": 1},
            {"text": "Иногда.", "score": 2},
            {"text": "Часто.", "score": 3},
        ],
    },
    {
        "text": "Считаете ли вы, что зависимость влияет на вашу продуктивность?",
        "answers": [
            {"text": "Нет.", "score": 1},
            {"text": "В некоторых случаях.", "score": 2},
            {"text": "Да, постоянно.", "score": 3},
        ],
    },
    {
        "text": "Вы чувствуете раздражение, если не можете удовлетворить свою зависимость?",
        "answers": [
            {"text": "Нет, мне всё равно.", "score": 1},
            {"text": "Немного.", "score": 2},
            {"text": "Да, сильно раздражаюсь.", "score": 3},
        ],
    },
    {
        "text": "Ваши близкие замечали, что у вас может быть зависимость?",
        "answers": [
            {"text": "Нет, никогда.", "score": 1},
            {"text": "Иногда упоминали.", "score": 2},
            {"text": "Да, говорят об этом часто.", "score": 3},
        ],
    },
    {
        "text": "Вы пытаетесь скрывать свою зависимость от других?",
        "answers": [
            {"text": "Нет, не скрываю.", "score": 1},
            {"text": "Иногда.", "score": 2},
            {"text": "Да, скрываю часто.", "score": 3},
        ],
    },
]

async def create_addiction_keyboard(question_index: int) -> InlineKeyboardMarkup:
    if question_index < 0 or question_index >= len(addiction_questions):
        raise ValueError(f"Некорректный индекс вопроса: {question_index}")

    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    for idx, answer in enumerate(addiction_questions[question_index]["answers"]):
        keyboard.inline_keyboard.append([
            InlineKeyboardButton(
                text=answer["text"],
                callback_data=f"addiction_answer_{question_index}_{idx}"
            )
        ])
    return keyboard
