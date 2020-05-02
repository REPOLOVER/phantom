import html
import random
import time
from typing import List

from telegram import Bot, Update, ParseMode
from telegram.ext import run_async

from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler
from tg_bot.modules.helper_funcs.chat_status import is_user_admin, user_admin
from tg_bot.modules.helper_funcs.extraction import extract_user

#sleep how many times after each edit in 'police' 
EDIT_SLEEP = 1
#edit how many times in 'fire' 
EDIT_TIMES = 3

fire = [
            "🏃‍♂️🏃‍♀️\n🏃‍♂️🏃‍♀️\n🏃‍♂️🏃‍♀️",
            "🏃‍♀️🏃‍♂️\n🏃‍♀️🏃‍♂️\n🏃‍♀️🏃‍♂️"
]



@user_admin
@run_async
def police(bot: Bot, update: Update):
    msg = update.effective_message.reply_text('🔥 is comming') 
    for x in range(EDIT_TIMES):
        msg.edit_text(fire[x%2])
        time.sleep(EDIT_SLEEP)
    msg.edit_text('help help 😭')


__help__ = """
- /fire : 🔥
"""

FIRE_HANDLER = DisableAbleCommandHandler("fire", fire)


dispatcher.add_handler(FIRE_HANDLER)

__mod_name__ = "FIRE"
__command_list__ = ["fire"]
__handlers__ = [FIRE_HANDLER]
