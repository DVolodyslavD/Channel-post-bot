from config import dp
from aiogram.utils import executor
import bot


if __name__ == '__main__':
    executor.start_polling(dp)