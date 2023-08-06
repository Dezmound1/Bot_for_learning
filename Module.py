from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import types
import KB

storage= MemoryStorage()
bot = Bot(token= "6544689005:AAE4moL83cHveFgI-DVZfll-_thcXMOmaRs", parse_mode= types.ParseMode.HTML)
dp = Dispatcher(bot, storage= storage)
