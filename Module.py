from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import types
import KB

storage= MemoryStorage()
bot = Bot(token= "6106250764:AAHV-jZy1rkHGDK2OCfCHxQ9Sq42i7wSIDU", parse_mode= types.ParseMode.HTML)
dp = Dispatcher(bot, storage= storage)
