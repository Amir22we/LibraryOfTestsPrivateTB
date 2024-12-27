from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from app.memes.zucchini.fsm import ZucchiniState
from app.memes.zucchini.zucchini_keyboards import create_zucchini_keyboard, zucchini_questions
from aiogram.types import FSInputFile
import asyncio
router = Router()

@router.callback_query(lambda c: c.data == "type_of_zucchini")
async def start_zucchini_test(callback: types.CallbackQuery, state: FSMContext):

    await state.set_state(ZucchiniState.QUESTION)
    await state.update_data(score=0, question_index=0)

    question_index = 0
    question_text = zucchini_questions[question_index]["text"]
    keyboard = await create_zucchini_keyboard(question_index)

    await callback.message.edit_text(
        text=question_text,
        reply_markup=keyboard
    )
    await callback.answer("Начнём тест на какой ты кабачок!")


@router.callback_query(lambda c: c.data.startswith("zucchini_answer_"))
async def handle_zucchini_answer(callback: types.CallbackQuery, state: FSMContext):

    user_data = await state.get_data()

    data = callback.data.split("_")
    question_index = int(data[2])
    answer_index = int(data[3])

    if question_index < 0 or question_index >= len(zucchini_questions):
        await callback.answer("Произошла ошибка: вопрос не найден.")
        return

    if answer_index < 0 or answer_index >= len(zucchini_questions[question_index]["answers"]):
        await callback.answer("Произошла ошибка: выбранный ответ не найден.")
        return

    score = zucchini_questions[question_index]["answers"][answer_index]["score"]
    total_score = user_data.get("score", 0) + score
    await state.update_data(score=total_score)

    question_index += 1
    if question_index < len(zucchini_questions):
        await state.update_data(question_index=question_index)
        question_text = zucchini_questions[question_index]["text"]
        keyboard = await create_zucchini_keyboard(question_index)

        await callback.message.edit_text(
            text=question_text,
            reply_markup=keyboard
        )
    else:
        await show_zucchini_results(callback, state)

    await callback.answer()


async def show_zucchini_results(callback: types.CallbackQuery, state: FSMContext):

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
            "<b>Запечённый кабачок</b>\n\n"
            "Ты — истинный кабачок-страдалец. Твои эмоции на сковородке, но ты стойко держишься! Мемы — твой единственный свет в этом мире."
        )
        photo_path = "app/memes/zucchini/photo/image.png"
    elif total_score <= 12:
        result = (
            "<b>Скромный кабачок с грядки</b>\n\n"
            "Ты прост, как кабачок, но твоя душа чиста. У тебя есть немного стресса, но ты держишь равновесие."
        )
        photo_path = "app/memes/zucchini/photo/image copy 2.png"
    elif total_score <= 16:
        result = (
            "<b>Кабачок для всех сезонов</b>\n\n"
            "Ты универсальный овощ, который умеет всё: и на гриле, и в духовке, и в икре. В жизни ты мемный мастер и душа компании."
        )
        photo_path = "app/memes/zucchini/photo/image copy.png"
    else:
        result = (
            "<b>Король кабачков</b>\n\n"
            "Ты самый мемный, самый крутой кабачок! Жизнь на твоей грядке — вечный праздник. Бабульки на рынке готовы драться за тебя!"
        )
        photo_path = "app/memes/zucchini/photo/image copy 3.png"
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
