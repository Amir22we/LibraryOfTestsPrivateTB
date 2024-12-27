from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

cringe_questions = [
    {
        "text": "Как ведёшь себя при кринже?",
        "answers": [
            {"text": "Перематываю, делаю вид 'ничего'.", "score": 2},
            {"text": "Смеюсь, но в душе боль.", "score": 3},
            {"text": "Ставлю на паузу и думаю.", "score": 4},
            {"text": "Что такое кринж?", "score": 1},
        ],
    },
    {
        "text": "Что делаешь в соцсетях?",
        "answers": [
            {"text": "Пишу '😂😂🔥🔥' везде.", "score": 3},
            {"text": "Лайкаю свои старые посты.", "score": 4},
            {"text": "Только мемы и всё.", "score": 2},
            {"text": "Ничего, я загадка.", "score": 1},
        ],
    },
    {
        "text": "Как ведёшь себя в компании?",
        "answers": [
            {"text": "Молчу, пока не спросят.", "score": 1},
            {"text": "Перебиваю всех своими шутками.", "score": 3},
            {"text": "Смеюсь, даже если кринж.", "score": 2},
            {"text": "Танцую, потом сам кринжую.", "score": 4},
        ],
    },
    {
        "text": "Реакция на старые фотки?",
        "answers": [
            {"text": "О, боже, это я?", "score": 4},
            {"text": "Это было модно, кек.", "score": 2},
            {"text": "Выгляжу нормально.", "score": 1},
            {"text": "Публикую в сторис сразу.", "score": 3},
        ],
    },
    {
        "text": "Как ты поёшь в караоке?",
        "answers": [
            {"text": "Не буду, голос плохой.", "score": 1},
            {"text": "Кто слушает? Я пою.", "score": 2},
            {"text": "Я Леди Гага сейчас!.", "score": 3},
            {"text": "Пою так, что стены стонут.", "score": 4},
        ],
    },
]

async def create_cringe_keyboard(question_index: int) -> InlineKeyboardMarkup:

    if question_index < 0 or question_index >= len(cringe_questions):
        raise ValueError(f"Некорректный индекс вопроса: {question_index}")
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    for idx, answer in enumerate(cringe_questions[question_index]["answers"]):
        keyboard.inline_keyboard.append([
            InlineKeyboardButton(
                text=answer["text"],
                callback_data=f"cringe_answer_{question_index}_{idx}"
            )
        ])
    return keyboard
