import asyncio

from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from tugmalar import menyu, inline_katalog, orqaga

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

# 1-Handler
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Assalomu alaykum hurmatli foydalanuvchi Test Botimizga xush kelibsiz!",
    reply_markup=menyu
)


# Callback uchun Handler
@dp.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
    await callback.answer("Siz Katalog tugmasini bosdingiz!")
    await callback.message.edit_text('Bitta meva tanlang: ', reply_markup=inline_katalog)

@dp.callback_query(F.data == 'anor')
async def anor(callback: CallbackQuery):
    await callback.message.edit_text("""Oddiy anor ( lotincha: Púnica granátum) — derbenlar oilasiga  (Lythraceae) turkumiga mansub o‘simlik turi, mevasi iste’molga yaroqli. 
Anor mevalarini ozuqa mevasi sifatida xom holda, tayyor ovqatga solishda, shuningdek, sharbatini olib, ichimlik sifatida foydalanish mumkin. 
Shimoliy yarimsharda anor mavsumi odatda sentabrdan fevralgacha, janubiy yarimsharda — martdan maygacha davom etadi. Anor Gʻarbiy Osiyo aholisi tomonidan qadim zamonlardan buyon qo‘llanib kelinadi. 
Hozirgi vaqtda u Yaqin Sharq va Kavkazda, Shimoliy va tropik Afrikada, Osiyo va O‘rtayer dengizining bir qator mintaqalarida keng yetishtiriladi.""", reply_markup=orqaga)

@dp.callback_query(F.data == 'orqaga') # This handler is now correctly triggered by both "back" buttons
async def back_to_catalog(callback: CallbackQuery):
    await callback.answer("Katalogga qaytish")
    await callback.message.edit_text('Bitta meva tanlang: ', reply_markup=inline_katalog)

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Dastur to'xtadi!")