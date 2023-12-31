import logging
from aiogram.dispatcher import FSMContext
from buttons import timeform_kb, continuation_kb, choose_help_kb
from messages import structure_dict, examples_dict
from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text


logging.basicConfig(level=logging.INFO)

# Создание словаря для сопоставления идентификаторов пользователей с объектами User
user_mapping = dict()

# Создание экземпляра Bot и Dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


# Обработчик для команды /start
@dp.message_handler(commands=['start'], state='*')
async def start_message(message: types.Message, state: FSMContext):
    await message.answer("Добро пожаловать в бота-помощника по временам Английского языка!")
    await message.answer("Выберите время, которое вас интересует:", reply_markup=timeform_kb)
    await state.set_state("choose_timeform")


# Обработчик для команды "restart"
@dp.message_handler(Text("restart"), state='*')
async def start_message(message: types.Message, state: FSMContext):
    await message.answer("Добро пожаловать в бота-помощника по временам Английского языка!")
    await message.answer("Выберите время, которое вас интересует:", reply_markup=timeform_kb)
    await state.set_state("choose_timeform")


# Обработчик для выбора времени "Present"
@dp.message_handler(Text(equals="Present", ignore_case=True), state="choose_timeform")
async def start_message(message: types.Message, state: FSMContext):
    await state.update_data(timeform="present")
    await message.answer("Выберите форму времени:", reply_markup=continuation_kb)
    await state.set_state("choose_continuation")


# Обработчик для выбора времени "Past"
@dp.message_handler(Text(equals="Past", ignore_case=True), state="choose_timeform")
async def start_message(message: types.Message, state: FSMContext):
    await state.update_data(timeform="past")
    await message.answer("Выберите форму времени:", reply_markup=continuation_kb)
    await state.set_state("choose_continuation")


# Обработчик для выбора времени "Future"
@dp.message_handler(Text(equals="Future", ignore_case=True), state="choose_timeform")
async def start_message(message: types.Message, state: FSMContext):
    await state.update_data(timeform="future")
    await message.answer("Выберите форму времени:", reply_markup=continuation_kb)
    await state.set_state("choose_continuation")


# Обработчик для выбора продолжения "Simple"
@dp.message_handler(Text(equals="Simple"), state="choose_continuation")
async def simple(message: types.Message, state: FSMContext):
    await state.update_data(continuation="simple")
    await message.answer("Выберите то, что вас интересует:", reply_markup=choose_help_kb)
    await state.set_state("choose_help")


# Обработчик для выбора продолжения "Continuous"
@dp.message_handler(Text(equals="Continuous"), state="choose_continuation")
async def continuous(message: types.Message, state: FSMContext):
    await state.update_data(continuation="continuous")
    await message.answer("Выберите то, что вас интересует:", reply_markup=choose_help_kb)
    await state.set_state("choose_help")


# Обработчик для выбора продолжения "Perfect"
@dp.message_handler(Text(equals="Perfect"), state="choose_continuation")
async def continuous(message: types.Message, state: FSMContext):
    await state.update_data(continuation="perfect")
    await message.answer("Выберите то, что вас интересует:", reply_markup=choose_help_kb)
    await state.set_state("choose_help")


# Обработчик для выбора продолжения "Perfect Continuous"
@dp.message_handler(Text(equals="Perfect Continuous"), state="choose_continuation")
async def continuous(message: types.Message, state: FSMContext):
    await state.update_data(continuation="perfect_continuous")
    await message.answer("Выберите то, что вас интересует:", reply_markup=choose_help_kb)
    await state.set_state("choose_help")


# Обработчик для выбора варианта "Структура"
@dp.message_handler(Text(equals="Структура"), state="choose_help")
async def structure(message: types.Message, state: FSMContext):
    data = await state.get_data()
    timeform = data["timeform"]
    continuation = data["continuation"]

    message_to_user = structure_dict[timeform][continuation]

    await message.answer(message_to_user, parse_mode="HTML")


# Обработчик для выбора варианта "Примеры"
@dp.message_handler(Text(equals="Примеры"), state="choose_help")
async def examples(message: types.Message, state: FSMContext):
    data = await state.get_data()
    timeform = data["timeform"]
    continuation = data["continuation"]
    message_to_user = examples_dict[timeform][continuation]

    await message.answer(message_to_user, parse_mode="HTML")

# Запуск опроса
if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)
