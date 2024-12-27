from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from app.psy.addiction.addiction_fsm import AddictionState
from app.psy.addiction.addiction_keyboards import create_addiction_keyboard, addiction_questions

router = Router()

@router.callback_query(lambda c: c.data == "addiction")
async def start_addiction_test(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(AddictionState.QUESTION)
    await state.update_data(score=0, question_index=0)

    question_index = 0
    question_text = addiction_questions[question_index]["text"]
    keyboard = await create_addiction_keyboard(question_index)

    await callback.message.edit_text(
        text=question_text,
        reply_markup=keyboard
    )
    await callback.answer("Начнём тест на зависимость!")

@router.callback_query(lambda c: c.data.startswith("addiction_answer_"))
async def handle_addiction_answer(callback: types.CallbackQuery, state: FSMContext):
    user_data = await state.get_data()

    data = callback.data.split("_")
    question_index = int(data[2])
    answer_index = int(data[3])

    if question_index < 0 or question_index >= len(addiction_questions):
        await callback.answer("Произошла ошибка: вопрос не найден.")
        return

    if answer_index < 0 or answer_index >= len(addiction_questions[question_index]["answers"]):
        await callback.answer("Произошла ошибка: выбранный ответ не найден.")
        return

    score = addiction_questions[question_index]["answers"][answer_index]["score"]
    total_score = user_data.get("score", 0) + score
    await state.update_data(score=total_score)

    question_index += 1
    if question_index < len(addiction_questions):
        await state.update_data(question_index=question_index)
        question_text = addiction_questions[question_index]["text"]
        keyboard = await create_addiction_keyboard(question_index)

        await callback.message.edit_text(
            text=question_text,
            reply_markup=keyboard
        )
    else:
        await show_addiction_results(callback, state)

    await callback.answer()

async def show_addiction_results(callback: types.CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    total_score = user_data.get("score", 0)

    if total_score <= 5:
        result = (
            "<b>Низкий риск зависимости</b>\n\n"
            "Вы не проявляете признаков серьёзной зависимости. Продолжайте поддерживать баланс в жизни!"
        )
    elif total_score <= 10:
        result = (
            "<b>Умеренный риск зависимости</b>\n\n"
            "Вы проявляете некоторые признаки зависимости. Подумайте о снижении влияния этого на вашу жизнь."
        )
    else:
        result = (
            "<b>Высокий риск зависимости</b>\n\n"
            "Вы демонстрируете явные признаки зависимости. Рекомендуем обратиться за поддержкой!"
        )

    await callback.message.answer(
        text=f"У вас - {result}",
        parse_mode="HTML"
    )
    await state.clear()
