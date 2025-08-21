from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

menyu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Katalog', callback_data='catalog')
    ],

    [
        InlineKeyboardButton(text='Yordam', callback_data='help')
    ]
]
)

# Inline Keyboard
inline_katalog = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Anor", callback_data='anor'),
            InlineKeyboardButton(text="Olma", callback_data='olma')
        ],
        [
            InlineKeyboardButton(text="Anjir", callback_data='anjir'),
            InlineKeyboardButton(text="Banan", callback_data='banan'),
            InlineKeyboardButton(text="Uzum", callback_data='uzum')
        ],
        [
            InlineKeyboardButton(text='Orqaga', callback_data='orqaga')
        ]

])

orqaga = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Orqaga', callback_data='orqaga')
    ]
])