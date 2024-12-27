from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from app.memes.cat.cat_fsm import CatState
from app.memes.cat.cat_keyboards import create_cat_keyboard, cat_questions
from aiogram.types import FSInputFile
import asyncio
router = Router()

@router.callback_query(lambda c: c.data == "type_of_cat")
async def start_cat_test(callback: types.CallbackQuery, state: FSMContext):

    await state.set_state(CatState.QUESTION)
    await state.update_data(score=0, question_index=0)

    question_index = 0
    question_text = cat_questions[question_index]["text"]
    keyboard = await create_cat_keyboard(question_index)

    await callback.message.edit_text(
        text=question_text,
        reply_markup=keyboard
    )
    await callback.answer("Начнём тест на котика!")

@router.callback_query(lambda c: c.data.startswith("cat_answer_"))
async def handle_cat_answer(callback: types.CallbackQuery, state: FSMContext):
    user_data = await state.get_data()

    data = callback.data.split("_")
    question_index = int(data[2])
    answer_index = int(data[3])

    if question_index < 0 or question_index >= len(cat_questions):
        await callback.answer("Произошла ошибка: вопрос не найден.")
        return

    if answer_index < 0 or answer_index >= len(cat_questions[question_index]["answers"]):
        await callback.answer("Произошла ошибка: выбранный ответ не найден.")
        return

    score = cat_questions[question_index]["answers"][answer_index]["score"]
    total_score = user_data.get("score", 0) + score
    await state.update_data(score=total_score)

    question_index += 1
    if question_index < len(cat_questions):
        await state.update_data(question_index=question_index)
        question_text = cat_questions[question_index]["text"]
        keyboard = await create_cat_keyboard(question_index)

        await callback.message.edit_text(
            text=question_text,
            reply_markup=keyboard
        )
    else:
        await show_cat_results(callback, state)

    await callback.answer()


async def show_cat_results(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    user_data = await state.get_data()
    total_score = user_data.get("score", 0)
    await callback.message.edit_text("Подождите... Взламываем пентагон чтобы узнать результат")
    await asyncio.sleep(2)
    await callback.message.edit_text("Обработка: [▓▓▓░░░░░░░░░░░░░░░░░░░░░░] 10%")
    await asyncio.sleep(2)
    await callback.message.edit_text("Обработка: [▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░] 50%")
    await asyncio.sleep(2)
    await callback.message.edit_text("Обработка: [▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░] 75%")
    await asyncio.sleep(2)
    await callback.message.edit_text("Обработка: [▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░] 95%")
    if total_score <= 8:
        result = (
            "<b>Ленивый котик</b>\n\n"
            "Ты - мастер отдыха и уюта. Лежишь, мурчишь, наслаждаешься жизнью."
        )
        photo_path = "app/memes/cat/photo/image.png"
    elif total_score <= 12:
        result = (
            "<b>Игривый котик</b>\n\n"
            "Ты обожаешь шалости и мячики. Все думают, что ты супер позитивный!"
        )
        photo_path = "app/memes/cat/photo/image copy.png"
    elif total_score <= 16:
        result = (
            "<b>Котик-мем</b>\n\n"
            "Твои поступки - сплошные мемы. Ты звезда соцсетей!"
        )
        photo_path = "app/memes/cat/photo/image copy 2.png"
    else:
        result = (
            "<b>Король котиков</b>\n\n"
            "Ты самый величественный кот, который правит миром!"
        )
        photo_path = "app/memes/cat/photo/image copy 3.png"

    photo = FSInputFile(photo_path)

    await callback.message.answer_photo(
        photo=photo,
        caption=f"Ты - {result}",
        parse_mode="HTML"
    )
    await callback.message.edit_text("Обработка: [▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓] 100%")
    await asyncio.sleep(2)
    await callback.message.edit_text("Пентагон взломан!")
    await state.clear()
