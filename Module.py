from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import types
import cfg
import KB
import list_of_colums
storage= MemoryStorage()
bot = Bot(token= cfg.TOKEN_API, parse_mode= types.ParseMode.HTML)
dp = Dispatcher(bot, storage= storage)
