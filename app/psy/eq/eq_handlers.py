from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from app.psy.eq.eq_fsm import EmotionalIntelligenceState
from app.psy.eq.eq_keyboards import create_ei_keyboard, ei_questions

router = Router()

@router.callback_query(lambda c: c.data == "emotional_intelligence")
async def start_ei_test(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(EmotionalIntelligenceState.QUESTION)
    await state.update_data(score=0, question_index=0)

    question_index = 0
    question_text = ei_questions[question_index]["text"]
    keyboard = await create_ei_keyboard(question_index)

    await callback.message.edit_text(
        text=question_text,
        reply_markup=keyboard
    )
    await callback.answer("Начнём тест на эмоциональный интеллект!")

@router.callback_query(lambda c: c.data.startswith("ei_answer_"))
async def handle_ei_answer(callback: types.CallbackQuery, state: FSMContext):
    user_data = await state.get_data()

    data = callback.data.split("_")
    question_index = int(data[2])
    answer_index = int(data[3])

    if question_index < 0 or question_index >= len(ei_questions):
        await callback.answer("Произошла ошибка: вопрос не найден.")
        return

    if answer_index < 0 or answer_index >= len(ei_questions[question_index]["answers"]):
        await callback.answer("Произошла ошибка: выбранный ответ не найден.")
        return

    score = ei_questions[question_index]["answers"][answer_index]["score"]
    total_score = user_data.get("score", 0) + score
    await state.update_data(score=total_score)

    question_index += 1
    if question_index < len(ei_questions):
        await state.update_data(question_index=question_index)
        question_text = ei_questions[question_index]["text"]
        keyboard = await create_ei_keyboard(question_index)

        await callback.message.edit_text(
            text=question_text,
            reply_markup=keyboard
        )
    else:
        await show_ei_results(callback, state)

    await callback.answer()

async def show_ei_results(callback: types.CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    total_score = user_data.get("score", 0)

    if total_score <= 5:
        result = (
            "<b>Низкий эмоциональный интеллект</b>\n\n"
            "Вы можете испытывать трудности в понимании эмоций — своих и чужих. Попробуйте больше уделять внимания эмоциональной сфере."
        )
    elif total_score <= 10:
        result = (
            "<b>Средний эмоциональный интеллект</b>\n\n"
            "Ваш эмоциональный интеллект находится на среднем уровне. Развитие эмпатии и эмоционального контроля поможет вам."
        )
    else:
        result = (
            "<b>Высокий эмоциональный интеллект</b>\n\n"
            "У вас высокий эмоциональный интеллект! Вы хорошо понимаете свои и чужие эмоции. Продолжайте развивать этот навык."
        )

    await callback.message.answer(
        text=f"У вас - {result}",
        parse_mode="HTML"
    )
    await state.clear()