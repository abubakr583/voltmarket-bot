import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import (
    InlineKeyboardButton, 
    InlineKeyboardMarkup, 
    WebAppInfo, 
    KeyboardButton, 
    ReplyKeyboardMarkup
)
from aiohttp import web

# @BotFather bergan tokenni bu yerga qo'ying
BOT_TOKEN = "8875271497:AAHkIQSkSAg-X_e57nBnR7ry-agTT9geGyk"

# Sizning Telegram ID raqamingiz (@userinfobot yoki skrindan ko'ringan @GetmyIDBot orqali bilib olasiz)
ADMIN_ID = 8185164117

# Saytingizning Vercel manzili
WEBAPP_URL = "https://market-dusky-two.vercel.app"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# --- 1. Asosiy Menyu Klaviaturasi ---
def get_main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🛍 Do'konga kirish (Web App)", web_app=WebAppInfo(url=WEBAPP_URL))
            ],
            [
                KeyboardButton(text="💻 B/U Noutbuklar"),
                KeyboardButton(text="🔄 Trade-In Kalkulyator")
            ],
            [
                KeyboardButton(text="🌡️ Termopasta & Servis"),
                KeyboardButton(text="📍 Manzil va Aloqa")
            ]
        ],
        resize_keyboard=True
    )

# --- 2. /start buyrug'i ---
@dp.message(CommandStart())
async def start_command(message: types.Message):
    welcome_text = (
        f"⚡ **Assalomu alaykum, {message.from_user.first_name}!**\n\n"
        "🎮 **VOLTMARKET** — Gaming noutbuklar, B/U texnika, ehtiyot qismlar va servis markaziga xush kelibsiz!\n\n"
        "Quyidagi menyu orqali do'konimizga kirishingiz, noutbukingizni Trade-In orqali baholashingiz "
        "yoki ustalarimiz xizmatiga yozilishingiz mumkin 👇"
    )
    
    inline_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🚀 Do'konni to'liq ekranda ochish", 
                    web_app=WebAppInfo(url=WEBAPP_URL)
                )
            ]
        ]
    )
    await message.answer(welcome_text, reply_markup=get_main_menu(), parse_mode="Markdown")
    await message.answer("Tezkor xarid uchun to'g'ridan-to'g'ri marketni oching:", reply_markup=inline_kb)

# --- 3. B/U Noutbuklar tezkor ro'yxati ---
@dp.message(F.text == "💻 B/U Noutbuklar")
async def show_laptops(message: types.Message):
    text = (
        "🔥 **Do'konda mavjud bo'lgan eng ommabop B/U o'yin noutbuklari:**\n\n"
        "1. **Acer Nitro 5** — Core i5 / 16GB / GTX 1650 4GB\n"
        "   💰 Narxi: ~3 400 000 so'm (PUBG: 90+ FPS)\n\n"
        "2. **ASUS TUF Gaming F15** — Core i5 / 16GB / RTX 3050 4GB\n"
        "   💰 Narxi: ~4 400 000 so'm (CS2: 240+ FPS)\n\n"
        "3. **Lenovo Legion 5** — Ryzen 7 / 16GB / RTX 3060 6GB\n"
        "   💰 Narxi: ~5 800 000 so'm (Top sovutish)\n\n"
        "4. **Apple MacBook Air M1** — 8GB / 256GB SSD\n"
        "   💰 Narxi: ~5 200 000 so'm (Ideal akkumulyator)\n\n"
        "Barcha 100+ modellarni rasmlari bilan ko'rish uchun saytga kiring:"
    )
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔎 Barcha noutbuklarni ko'rish", web_app=WebAppInfo(url=WEBAPP_URL))]
        ]
    )
    await message.answer(text, reply_markup=kb, parse_mode="Markdown")

# --- 4. Trade-In Tezkor kalkulyator ---
@dp.message(F.text == "🔄 Trade-In Kalkulyator")
async def show_tradein(message: types.Message):
    text = (
        "🔄 **Trade-In Xizmati: Eskisini bering — Yangisini oling!**\n\n"
        "Qanday ishlaydi?\n"
        "1. Eski noutbukingiz holati tekshiriladi.\n"
        "2. Narxi baholanib, yangi noutbuk narxidan chegirib beriladi.\n\n"
        "💵 **Taxminiy baholash:**\n"
        "• Core i3 / Ofis modellari: 1.5 - 2.5 mln so'm\n"
        "• Core i5 / Gaming modellari: 3.0 - 4.5 mln so'm\n"
        "• Core i7 / RTX modellari: 5.0 - 7.5 mln so'm\n\n"
        "Noutbukingizni aniq hisoblash uchun tugmani bosing:"
    )
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🧮 Onlayn hisoblash", web_app=WebAppInfo(url=WEBAPP_URL))]
        ]
    )
    await message.answer(text, reply_markup=kb, parse_mode="Markdown")

# --- 5. Termopasta & Servis ---
@dp.message(F.text == "🌡️ Termopasta & Servis")
async def show_service(message: types.Message):
    text = (
        "🛠 **VOLTMARKET Rasmiy Servis Profilaktikasi:**\n\n"
        "Noutbukingiz qizib, shovqin qilyaptimi yoki o'yinlarda qotyaptimi?\n\n"
        "❄️ **Bizning xizmatlar:**\n"
        "• Kulerlar va radiatorlarni to'liq changdan tozalash\n"
        "• **Honeywell PTM7950** fazoviy o'tuvchi termopasta surtish (-12°C ga tushadi)\n"
        "• **Arctic MX-4** yoki Suyuq metall surtish\n"
        "• Windows 11 o'rnatish va o'yinlar uchun optimizatsiya\n\n"
        "⏱ Vaqti: ~30-40 daqiqa."
    )
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📅 Servisga yozilish", web_app=WebAppInfo(url=WEBAPP_URL))]
        ]
    )
    await message.answer(text, reply_markup=kb, parse_mode="Markdown")

# --- 6. Manzil va Kontaktlar ---
@dp.message(F.text == "📍 Manzil va Aloqa")
async def show_location(message: types.Message):
    text = (
        "📍 **Do'konimiz manzillari:**\n"
        "1. Toshkent shahri, Malika savdo markazi, A-15 do'kon.\n"
        "2. Namangan shahri, Bobur shoh ko'chasi.\n\n"
        "⏰ **Ish vaqti:** Har kuni 09:00 dan 20:00 gacha (Dam olish kunlarisiz).\n"
        "📞 **Telefon / Telegram:** +998 (90) 123-45-67\n"
        "🚚 **Yetkazib berish:** Toshkentda 2 soatda, viloyatlarga BTS pochta orqali 24 soatda!\n"
        "🛡 **Kafolat:** Har bir B/U tovar uchun 14 kunlik to'liq tekshirish kafolati."
    )
    await message.answer(text, parse_mode="Markdown")

# --- 7. Saytdan tushadigan buyurtmalar API serveri ---
async def receive_order_api(request):
    try:
        data = await request.json()
        name = data.get("name", "Mijoz")
        phone = data.get("phone", "Ko'rsatilmadi")
        address = data.get("address", "Do'kondan olib ketish")
        items = data.get("items", "Ko'rsatilmadi")
        total = data.get("total", "0 so'm")
        order_type = data.get("order_type", "To'liq to'lov")

        admin_msg = (
            "🔔 **YANGI BUYURTMA KELIB TUSHDI!**\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            f"👤 **Xaridor:** {name}\n"
            f"📞 **Telefon:** `{phone}`\n"
            f"📍 **Manzil:** {address}\n"
            f"💳 **To'lov usuli:** {order_type}\n\n"
            f"📦 **Tovarlar ro'yxati:**\n{items}\n\n"
            f"💰 **Umumiy summa:** `{total}`\n"
            "━━━━━━━━━━━━━━━━━━━━"
        )

        # Admin uchun boshqaruv tugmalari
        admin_kb = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="✅ Buyurtmani qabul qilish", callback_data="order_accept"),
                    InlineKeyboardButton(text="❌ Bekor qilish", callback_data="order_cancel")
                ],
                [
                    InlineKeyboardButton(text="📞 Mijoz bilan bog'lanish", url=f"tel:{phone}")
                ]
            ]
        )

        await bot.send_message(chat_id=ADMIN_ID, text=admin_msg, reply_markup=admin_kb, parse_mode="Markdown")
        return web.json_response({"status": "ok"})
    except Exception as e:
        return web.json_response({"status": "error", "message": str(e)}, status=500)

@dp.callback_query(F.data == "order_accept")
async def accept_order_btn(call: types.CallbackQuery):
    await call.message.edit_text(call.message.text + "\n\n🟢 **STATUS: Qabul qilindi, mijozga chiqildi.**")
    await call.answer("Buyurtma qabul qilindi!")

@dp.callback_query(F.data == "order_cancel")
async def cancel_order_btn(call: types.CallbackQuery):
    await call.message.edit_text(call.message.text + "\n\n🔴 **STATUS: Buyurtma bekor qilindi.**")
    await call.answer("Buyurtma bekor qilindi.")

# --- 8. Web server va Botni birgalikda ishga tushirish ---
async def start_server():
    app = web.Application()
    app.router.add_post("/api/order", receive_order_api)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8080)
    await site.start()

async def main():
    await start_server()
    print(">>> VOLTMARKET Boti va Buyurtma Serveri muvaffaqiyatli ishga tushdi! <<<")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())