from pymongo import MongoClient
from datetime import datetime, timedelta
from pyrogram import Client, filters

# Connect to MongoDB (Replace with your MongoDB URI)
MONGO_URI = "mongodb+srv://your_mongo_uri"
client = MongoClient(MONGO_URI)
db = client["bot_database"]
premium_users = db["premium_users"]

# Add premium user
@Client.on_message(filters.command("addpremium") & filters.user("YOUR_ADMIN_ID"))
def add_premium(bot, message):
    args = message.text.split()
    if len(args) < 3:
        return message.reply("Usage: /addpremium @username days")
    
    username = args[1]
    days = int(args[2])
    expiry_date = datetime.utcnow() + timedelta(days=days)

    premium_users.update_one(
        {"username": username}, 
        {"$set": {"expiry": expiry_date}}, 
        upsert=True
    )
    message.reply(f"✅ {username} added to premium for {days} days!")

# Remove premium user
@Client.on_message(filters.command("removepremium") & filters.user("YOUR_ADMIN_ID"))
def remove_premium(bot, message):
    args = message.text.split()
    if len(args) < 2:
        return message.reply("Usage: /removepremium @username")
    
    username = args[1]
    premium_users.delete_one({"username": username})
    message.reply(f"❌ {username} removed from premium.")

# Check premium status
@Client.on_message(filters.command("checkpremium"))
def check_premium(bot, message):
    args = message.text.split()
    if len(args) < 2:
        return message.reply("Usage: /checkpremium @username")

    username = args[1]
    user = premium_users.find_one({"username": username})

    if user:
        expiry = user["expiry"].strftime("%Y-%m-%d %H:%M:%S")
        message.reply(f"🔹 {username} is a premium user until {expiry}.")
    else:
        message.reply(f"⚠ {username} is not a premium user.")

# Premium Button in Start Command
@Client.on_message(filters.command("start"))
def start(bot, message):
    from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("💎 Buy Premium", url="https://t.me/AdminUsername")],
        [InlineKeyboardButton("Help", callback_data="help")]
    ])

    message.reply("Welcome! Get premium benefits:", reply_markup=keyboard)
