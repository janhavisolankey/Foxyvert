# (©)CodeFlix_Bots
# rohit_1888 on Tg #Dont remove this line

import base64
import re
import asyncio
import time
from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from config import *
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.errors import FloodWait
from shortzy import Shortzy
from database.database import *


async def check_subscription(client, user_id, channel_id):
    """Check if a user is subscribed to a specific channel."""
    if not channel_id:
        return True
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(chat_id=channel_id, user_id=user_id)
        return member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.MEMBER]
    except UserNotParticipant:
        return False
    except Exception:
        return False


async def encode(string):
    """Encode a string to a Base64 URL-safe format."""
    string_bytes = string.encode("ascii")
    base64_bytes = base64.urlsafe_b64encode(string_bytes)
    return base64_bytes.decode("ascii").strip("=")


async def decode(base64_string):
    """Decode a Base64 URL-safe formatted string."""
    base64_string = base64_string.strip("=")
    base64_bytes = (base64_string + "=" * (-len(base64_string) % 4)).encode("ascii")
    return base64.urlsafe_b64decode(base64_bytes).decode("ascii")


async def get_messages(client, message_ids):
    """Retrieve messages from the database channel."""
    messages = []
    total_messages = 0
    while total_messages != len(message_ids):
        temp_ids = message_ids[total_messages:total_messages+200]
        try:
            msgs = await client.get_messages(chat_id=client.db_channel.id, message_ids=temp_ids)
        except FloodWait as e:
            await asyncio.sleep(e.value)
            msgs = await client.get_messages(chat_id=client.db_channel.id, message_ids=temp_ids)
        except Exception:
            msgs = []
        total_messages += len(temp_ids)
        messages.extend(msgs)
    return messages


async def get_message_id(client, message):
    """Extract message ID from forwarded message or text link."""
    if message.forward_from_chat and message.forward_from_chat.id == client.db_channel.id:
        return message.forward_from_message_id
    elif message.forward_sender_name:
        return 0
    elif message.text:
        pattern = r"https://t.me/(?:c/)?(.*)/(\d+)"
        matches = re.match(pattern, message.text)
        if matches:
            channel_id, msg_id = matches.groups()
            msg_id = int(msg_id)
            if channel_id.isdigit() and f"-100{channel_id}" == str(client.db_channel.id):
                return msg_id
            elif channel_id == client.db_channel.username:
                return msg_id
    return 0


def get_readable_time(seconds: int) -> str:
    """Convert seconds into a human-readable time format."""
    periods = [("days", 86400), ("h", 3600), ("m", 60), ("s", 1)]
    time_list = []
    for name, sec in periods:
        if seconds >= sec:
            value, seconds = divmod(seconds, sec)
            time_list.append(f"{int(value)}{name}")
    return ":".join(time_list) if time_list else "0s"


async def get_verify_status(user_id):
    """Retrieve user verification status."""
    return await db_verify_status(user_id)


async def update_verify_status(user_id, verify_token="", is_verified=False, verified_time=0, link=""):
    """Update user verification status in the database."""
    current = await db_verify_status(user_id)
    current.update({
        "verify_token": verify_token,
        "is_verified": is_verified,
        "verified_time": verified_time,
        "link": link
    })
    await db_update_verify_status(user_id, current)


async def get_shortlink(url, api, link):
    """Generate a short link using Shortzy API."""
    shortzy = Shortzy(api_key=api, base_site=url)
    return await shortzy.convert(link)


def get_exp_time(seconds):
    """Convert expiration time from seconds to readable format."""
    periods = [("days", 86400), ("hours", 3600), ("mins", 60), ("secs", 1)]
    result = []
    for name, sec in periods:
        if seconds >= sec:
            value, seconds = divmod(seconds, sec)
            result.append(f"{int(value)} {name}")
    return " ".join(result)


# Subscription Filters
subscribed1 = filters.create(lambda _, client, update: asyncio.run(check_subscription(client, update.from_user.id, FORCE_SUB_CHANNEL1)))
subscribed2 = filters.create(lambda _, client, update: asyncio.run(check_subscription(client, update.from_user.id, FORCE_SUB_CHANNEL2)))
subscribed3 = filters.create(lambda _, client, update: asyncio.run(check_subscription(client, update.from_user.id, FORCE_SUB_CHANNEL3)))
subscribed4 = filters.create(lambda _, client, update: asyncio.run(check_subscription(client, update.from_user.id, FORCE_SUB_CHANNEL4)))

# rohit_1888 on Tg
