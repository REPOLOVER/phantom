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
#edit how many times in 'hack' 
EDIT_TIMES = 3

hack = [
            "■■■■□□□□□\n■■■■□□□□□\n■■■■□□□□□",
            "□□□□■■■■■\n□□□□■■■■■\n□□□□■■■■■"
]



@user_admin
@run_async
def hack(bot: Bot, update: Update):
    msg = update.effective_message.reply_text('Target account selected!') 
    for x in range(EDIT_TIMES):
        msg.edit_text(hack[x%2])
        time.sleep(EDIT_SLEEP)
    msg.edit_text('Police is here!')


__help__ = """
- /hack : 😆
"""

POLICE_HANDLER = DisableAbleCommandHandler("police", police)


dispatcher.add_handler(POLICE_HANDLER)

__mod_name__ = "HACK"
__command_list__ = ["hack"]
__handlers__ = [HACK_HANDLER]
