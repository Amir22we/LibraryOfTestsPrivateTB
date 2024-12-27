from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, )

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Выбрать тесты')],
    [KeyboardButton(text='Информация')],
    [KeyboardButton(text='Предложить тесты')]
],
    resize_keyboard=True,
    input_field_placeholder="Выберай Выберай Выберай :P"
)

choose_test = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Тесты по психологии', callback_data='psy_test')],
    [InlineKeyboardButton(text='Мемные тесты', callback_data='meme_test')],
    [InlineKeyboardButton(text='Рандомное', callback_data='random_test')]
])

psy_test_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Тест на уверенность в себе', callback_data='self_confidience')],
    [InlineKeyboardButton(text='Тест на эмоциональный интеллект (EQ)', callback_data='emotional_intelligence')],
    [InlineKeyboardButton(text='Тест на зависимость', callback_data='addiction')],
    [InlineKeyboardButton(text='Назад', callback_data='back_to_main')]
])

meme_test_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Тест на уровень кринжа', callback_data='cringe_level')],
    [InlineKeyboardButton(text='Тест на вид кабачка', callback_data='type_of_zucchini')],
    [InlineKeyboardButton(text='Тест на тип котика', callback_data='type_of_cat')],
    [InlineKeyboardButton(text='Назад', callback_data='back_to_main')]
])

random_test_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Тест на общие знания', callback_data='general_knowledge')],
    [InlineKeyboardButton(text='Тест на Амира', callback_data='amir_test')],
    [InlineKeyboardButton(text='Назад', callback_data='back_to_main')]
])

contacts = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Предложить тесты', url='https://t.me/new24qwerty')],
    [InlineKeyboardButton(text='Личный канал', url='https://t.me/bunkeramira')]
])