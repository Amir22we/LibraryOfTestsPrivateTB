from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from app.random.amir.amir_fsm import AmirTestState
from app.random.amir.amir_keyboards import create_amir_keyboard, amir_questions

router = Router()

@router.callback_query(lambda c: c.data == "amir_test")
async def start_amir_test(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(AmirTestState.QUESTION)
    await state.update_data(score=0, question_index=0)

    question_index = 0
    question_text = amir_questions[question_index]["text"]
    keyboard = await create_amir_keyboard(question_index)

    await callback.message.edit_text(
        text=question_text,
        reply_markup=keyboard
    )
    await callback.answer("Начнём тест на знание Амира!")

@router.callback_query(lambda c: c.data.startswith("amir_answer_"))
async def handle_amir_answer(callback: types.CallbackQuery, state: FSMContext):
    user_data = await state.get_data()

    data = callback.data.split("_")
    question_index = int(data[2])
    answer_index = int(data[3])

    if question_index < 0 or question_index >= len(amir_questions):
        await callback.answer("Произошла ошибка: вопрос не найден.")
        return

    if answer_index < 0 or answer_index >= len(amir_questions[question_index]["answers"]):
        await callback.answer("Произошла ошибка: выбранный ответ не найден.")
        return

    score = amir_questions[question_index]["answers"][answer_index]["score"]
    total_score = user_data.get("score", 0) + score
    await state.update_data(score=total_score)

    question_index += 1
    if question_index < len(amir_questions):
        await state.update_data(question_index=question_index)
        question_text = amir_questions[question_index]["text"]
        keyboard = await create_amir_keyboard(question_index)

        await callback.message.edit_text(
            text=question_text,
            reply_markup=keyboard
        )
    else:
        await show_amir_results(callback, state)

    await callback.answer()

async def show_amir_results(callback: types.CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    total_score = user_data.get("score", 0)

    if total_score <= 5:
        result = (
            "<b>Привет, Я Амир и я создал эти тесты!</b>\n\n"
            "Ты лучший!"
        )
    elif total_score <= 10:
        result = (
            "<b>Привет, Я Амир и я создал эти тесты!</b>\n\n"
            "Ты лучший!."
        )
    else:
        result = (
            "<b>Ты лучший!</b>\n\n"
            "Привет, Я Амир и я создал эти тесты!"
        )

    await callback.message.answer(
        text=result,
        parse_mode="HTML"
    )
    await state.clear()