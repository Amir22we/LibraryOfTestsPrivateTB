from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
import app.keyboards as kb
import asyncio

from app.memes.zucchini.zucchini_handlers import router as zucchini_router
from app.memes.cringe.cringe_handlers import router as cringe_router
from app.memes.cat.cat_handlers import router as cat_router
from app.psy.addiction.addiction_handlers import router as addiction_router
from app.psy.confidence.confidence_handlers import router as confidence_router
from app.psy.eq.eq_handlers import router as eq_router
from app.random.gk.gk_handlers import router as gk_router
from app.random.amir.amir_handlers import router as amir_router
router = Router()
router.include_router(amir_router)
router.include_router(gk_router)
router.include_router(eq_router)
router.include_router(confidence_router)
router.include_router(addiction_router)
router.include_router(zucchini_router)
router.include_router(cringe_router)
router.include_router(cat_router)
@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer(
        f'Привет {message.from_user.full_name} !\n\n'
        'Здесь вы можете пройти различные тесты и узнать, кто вы!',
        reply_markup=kb.main
    )

@router.message(F.text == 'Выбрать тесты')
async def test_select(message: Message):
    await message.answer("Выберите категорию тестов:", reply_markup=kb.choose_test)

@router.callback_query(lambda c: c.data in ['psy_test', 'meme_test', 'random_test'])
async def show_test_category(callback: types.CallbackQuery):
    if callback.data == 'psy_test':
        await callback.message.edit_text("Выберите тест по психологии:", reply_markup=kb.psy_test_keyboard)
    elif callback.data == 'meme_test':
        await callback.message.edit_text("Выберите мемный тест:", reply_markup=kb.meme_test_keyboard)
    elif callback.data == 'random_test':
        await callback.message.edit_text("Выберите рандомный тест:", reply_markup=kb.random_test_keyboard)
    await callback.answer("Переходим...")

@router.callback_query(lambda c: c.data == 'back_to_main')
async def back_to_main_hadler(callback: types.CallbackQuery):
    await callback.message.edit_text("Выберите категорию тестов:", reply_markup=kb.choose_test)
    await callback.answer("Переходим...")

@router.message(F.text == 'Информация')
async def info_handler(message: Message):
    await message.answer("Привет! 👋 Здесь ты можешь найти разные тесты: от «Какой ты кабачок?» до проверки твоего эмоционального интеллекта. Выбирай, проходи и узнавай о себе что-то новое!Кстати, подпишись на мой канал — там тоже куча интересного.", reply_markup=kb.contacts)

@router.message(F.text == 'Предложить тесты')
async def offer_test(message: Message):
    await message.answer("Прежде чем предложить тесты, учтите два важных правила: \n\nНикакого нелегального контента. Это значит, что мы не принимаем тесты, связанные с порнографией, наркотиками, убийствами и прочим запрещённым содержимым.\n\nПолная информация. Если вы хотите добавить тест, обязательно предоставьте всю информацию:\nВопросы и варианты ответов.\nРезультаты и описание.\nИсточник (откуда вы взяли информацию).\n\nСпасибо за понимание! 😊", reply_markup=kb.contacts)