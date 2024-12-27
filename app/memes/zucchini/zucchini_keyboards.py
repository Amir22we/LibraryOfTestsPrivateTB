from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

zucchini_questions = [
    {
        "text": "Как проводишь выходные?",
        "answers": [
            {"text": "Лежу на диване.", "score": 1},
            {"text": "Иду на тусу.", "score": 2},
            {"text": "Много работаю, думаю о жизни.", "score": 3},
            {"text": "Смотрю мемы, смеюсь.", "score": 4}
        ]
    },
    {
        "text": "Что выберешь на завтрак?",
        "answers": [
            {"text": "Кабачковую икру.", "score": 2},
            {"text": "Пиццу с кабачком.", "score": 4},
            {"text": "Ничего, страдаю от голода.", "score": 1},
            {"text": "Омлет, я ЗОЖ-кабачок.", "score": 3}
        ]
    },
    {
        "text": "Куда отправили бы тебя?",
        "answers": [
            {"text": "В супермаркет блестеть.", "score": 3},
            {"text": "На рынок к бабулькам.", "score": 4},
            {"text": "Прямо в духовку.", "score": 1},
            {"text": "Оставили бы на грядке.", "score": 2}
        ]
    },
    {
        "text": "Кто твой лучший друг?",
        "answers": [
            {"text": "Баклажан, брат мемов.", "score": 1},
            {"text": "Морковь, яркая и крутая.", "score": 2},
            {"text": "Картошка, угнетённый овощ.", "score": 3},
            {"text": "Огурец, иногда я как он.", "score": 4}
        ]
    },
    {
        "text": "Как относишься к лету?",
        "answers": [
            {"text": "Люблю, время кабачков.", "score": 1},
            {"text": "Лето как жизнь на сковородке.", "score": 2},
            {"text": "Норм, главное — мемы.", "score": 3},
            {"text": "Я кабачок для всех сезонов.", "score": 4}
        ]
    }
]

async def create_zucchini_keyboard(question_index: int) -> InlineKeyboardMarkup:
    """
    Создаёт инлайн-клавиатуру для вопроса теста "Кринж".
    """
    if question_index < 0 or question_index >= len(zucchini_questions):
        raise ValueError(f"Некорректный индекс вопроса: {question_index}")
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    for idx, answer in enumerate(zucchini_questions[question_index]["answers"]):
        keyboard.inline_keyboard.append([
            InlineKeyboardButton(
                text=answer["text"],
                callback_data=f"zucchini_answer_{question_index}_{idx}"
            )
        ])
    return keyboard
