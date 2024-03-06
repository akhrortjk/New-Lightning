import os
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram import executor
from groq import Groq

# Initialize the Groq client
api_key = "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"
client = Groq(api_key=api_key)

# Initialize the Telegram bot
API_TOKEN = "6685386108:AAF0MIYvthrnfMWnspuNqOqRKAyMBroyH8k"
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Define a function to handle incoming messages
async def handle_message(message: types.Message):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message.text,
            }
        ],
        model="mixtral-8x7b-32768",
    )
    response = chat_completion.choices[0].message.content
    await message.reply(response)
    
# Start the bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
