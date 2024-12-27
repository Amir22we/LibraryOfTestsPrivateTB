from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from app.random.gk.gk_fsm import GeneralKnowledgeState
from app.random.gk.gk_keyboards import create_gk_keyboard, gk_questions

router = Router()

@router.callback_query(lambda c: c.data == "general_knowledge")
async def start_gk_test(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(GeneralKnowledgeState.QUESTION)
    await state.update_data(score=0, question_index=0)

    question_index = 0
    question_text = gk_questions[question_index]["text"]
    keyboard = await create_gk_keyboard(question_index)

    await callback.message.edit_text(
        text=question_text,
        reply_markup=keyboard
    )
    await callback.answer("Начнём тест на общие знания!")

@router.callback_query(lambda c: c.data.startswith("gk_answer_"))
async def handle_gk_answer(callback: types.CallbackQuery, state: FSMContext):
    user_data = await state.get_data()

    data = callback.data.split("_")
    question_index = int(data[2])
    answer_index = int(data[3])

    if question_index < 0 or question_index >= len(gk_questions):
        await callback.answer("Произошла ошибка: вопрос не найден.")
        return

    if answer_index < 0 or answer_index >= len(gk_questions[question_index]["answers"]):
        await callback.answer("Произошла ошибка: выбранный ответ не найден.")
        return

    score = gk_questions[question_index]["answers"][answer_index]["score"]
    total_score = user_data.get("score", 0) + score
    await state.update_data(score=total_score)

    question_index += 1
    if question_index < len(gk_questions):
        await state.update_data(question_index=question_index)
        question_text = gk_questions[question_index]["text"]
        keyboard = await create_gk_keyboard(question_index)

        await callback.message.edit_text(
            text=question_text,
            reply_markup=keyboard
        )
    else:
        await show_gk_results(callback, state)

    await callback.answer()

async def show_gk_results(callback: types.CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    total_score = user_data.get("score", 0)

    if total_score <= 5:
        result = (
            "<b>Низкий уровень знаний</b>\n\n"
            "Ваши общие знания пока на низком уровне. Попробуйте узнать больше о мире, читая книги и изучая интересные факты."
        )
    elif total_score <= 10:
        result = (
            "<b>Средний уровень знаний</b>\n\n"
            "Ваши знания на среднем уровне. Продолжайте узнавать новое, чтобы стать ещё лучше."
        )
    else:
        result = (
            "<b>Высокий уровень знаний</b>\n\n"
            "Ваши знания о мире впечатляют! Продолжайте развиваться и изучать новые темы."
        )

    await callback.message.answer(
        text=f"У вас - {result}",
        parse_mode="HTML"
    )
    await state.clear()
