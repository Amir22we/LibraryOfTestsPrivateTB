from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from app.psy.confidence.condidence_fsm import ConfidenceState
from app.psy.confidence.confidence_keyboards import create_confidence_keyboard, confidence_questions

router = Router()

@router.callback_query(lambda c: c.data == "self_confidience")
async def start_confidence_test(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(ConfidenceState.QUESTION)
    await state.update_data(score=0, question_index=0)

    question_index = 0
    question_text = confidence_questions[question_index]["text"]
    keyboard = await create_confidence_keyboard(question_index)

    await callback.message.edit_text(
        text=question_text,
        reply_markup=keyboard
    )
    await callback.answer("Начнём тест на уверенность в себе!")

@router.callback_query(lambda c: c.data.startswith("confidence_answer_"))
async def handle_confidence_answer(callback: types.CallbackQuery, state: FSMContext):
    user_data = await state.get_data()

    data = callback.data.split("_")
    question_index = int(data[2])
    answer_index = int(data[3])

    if question_index < 0 or question_index >= len(confidence_questions):
        await callback.answer("Произошла ошибка: вопрос не найден.")
        return

    if answer_index < 0 or answer_index >= len(confidence_questions[question_index]["answers"]):
        await callback.answer("Произошла ошибка: выбранный ответ не найден.")
        return

    score = confidence_questions[question_index]["answers"][answer_index]["score"]
    total_score = user_data.get("score", 0) + score
    await state.update_data(score=total_score)

    question_index += 1
    if question_index < len(confidence_questions):
        await state.update_data(question_index=question_index)
        question_text = confidence_questions[question_index]["text"]
        keyboard = await create_confidence_keyboard(question_index)

        await callback.message.edit_text(
            text=question_text,
            reply_markup=keyboard
        )
    else:
        await show_confidence_results(callback, state)

    await callback.answer()

async def show_confidence_results(callback: types.CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    total_score = user_data.get("score", 0)

    if total_score <= 5:
        result = (
            "<b>Низкая уверенность</b>\n\n"
            "Вы проявляете низкий уровень уверенности. Работайте над уверенностью в своих силах!"
        )
    elif total_score <= 10:
        result = (
            "<b>Средняя уверенность</b>\n\n"
            "У вас есть уверенность, но её стоит развивать, чтобы добиться больших успехов."
        )
    else:
        result = (
            "<b>Высокая уверенность</b>\n\n"
            "Вы уверены в себе! Это отличный результат, продолжайте в том же духе."
        )

    await callback.message.answer(
        text=f"У вас - {result}",
        parse_mode="HTML"
    )
    await state.clear()
