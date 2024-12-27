from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from app.memes.cringe.cringe_fsm import CringeState
from app.memes.cringe.cringe_keyboards import create_cringe_keyboard, cringe_questions
from aiogram.types import FSInputFile
import asyncio
router = Router()

@router.callback_query(lambda c: c.data == "cringe_level")
async def start_cringe_test(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(CringeState.QUESTION)
    await state.update_data(score=0, question_index=0)

    question_index = 0
    question_text = cringe_questions[question_index]["text"]
    keyboard = await create_cringe_keyboard(question_index)

    await callback.message.edit_text(
        text=question_text,
        reply_markup=keyboard
    )
    await callback.answer("Начнём тест на кринж!")


@router.callback_query(lambda c: c.data.startswith("cringe_answer_"))
async def handle_cringe_answer(callback: types.CallbackQuery, state: FSMContext):

    user_data = await state.get_data()

    data = callback.data.split("_")
    question_index = int(data[2])
    answer_index = int(data[3])

    if question_index < 0 or question_index >= len(cringe_questions):
        await callback.answer("Произошла ошибка: вопрос не найден.")
        return

    if answer_index < 0 or answer_index >= len(cringe_questions[question_index]["answers"]):
        await callback.answer("Произошла ошибка: выбранный ответ не найден.")
        return

    score = cringe_questions[question_index]["answers"][answer_index]["score"]
    total_score = user_data.get("score", 0) + score
    await state.update_data(score=total_score)

    question_index += 1
    if question_index < len(cringe_questions):
        await state.update_data(question_index=question_index)
        question_text = cringe_questions[question_index]["text"]
        keyboard = await create_cringe_keyboard(question_index)

        await callback.message.edit_text(
            text=question_text,
            reply_markup=keyboard
        )
    else:
        await show_cringe_results(callback, state)

    await callback.answer()


async def show_cringe_results(callback: types.CallbackQuery, state: FSMContext):
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
            "<b>Кринж отшельник</b>\n\n"
            "Ты редко ощущаешь кринж, но если что-то кринжанёт, то надолго. Твои друзья считают тебя нормальным, но ты понимаешь: главное — это внутренняя гармония."
        )
        photo_path = "app/memes/cringe/photo/image_alone.png"
    elif total_score <= 12:
        result = (
            "<b>Лёгкий кринжанский</b>\n\n"
            "Ты иногда ловишь кринжовые ситуации, но стараешься быстро перевести всё в шутку. В компании ты мемный, но без лишнего перегиба."
        )
        photo_path = "app/memes/cringe/photo/image_heavy.png"
    elif total_score <= 16:
        result = (
            "<b>Кринж мастер</b>\n\n"
            "Ты не только видишь кринж, но и создаёшь его. Тебе не стыдно за свои шутки и действия, потому что ты знаешь: жизнь слишком коротка, чтобы не мемить."
        )
        photo_path = "app/memes/cringe/photo/image_master.png"
    else:
        result = (
            "<b>Король кринжа</b>\n\n"
            "Ты просто король кринжа, не важно, что подумают другие!"
        )
        photo_path = "app/memes/cringe/photo/image_ling.png"

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
