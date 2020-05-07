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
#edit how many times in 'police' 
EDIT_TIMES = 10

love_siren = [
            "❤️❤️❤️🧡🧡🧡💚💚💚\n💙💙💙💜💜💜🖤🖤🖤",
            "🖤🖤🖤💜💜💜💙💙💙\n❤️❤️❤️🧡🧡🧡💚💚💚",
            "💛💛💛💙💙💙❤️❤️❤️\n💜💜💜❤️❤️❤️🧡🧡🧡",
            "❤️❤️❤️🧡🧡🧡💚💚💚\n💙💙💙💜💜💜🖤🖤🖤",
            "🖤🖤🖤💜💜💜💙💙💙\n❤️❤️❤️🧡🧡🧡💚💚💚",
            "💛💛💛💙💙💙❤️❤️❤️\n💜💜💜❤️❤️❤️🧡🧡🧡",
            "❤️❤️❤️🧡🧡🧡💚💚💚\n💙💙💙💜💜💜🖤🖤🖤",
            "🖤🖤🖤💜💜💜💙💙💙\n❤️❤️❤️🧡🧡🧡💚💚💚",
            "💛💛💛💙💙💙❤️❤️❤️\n💜💜💜❤️❤️❤️🧡🧡🧡"
]


hack_you = [
            "Looking for WhatsApp databases in targeted person...",
            " User online: True\nTelegram access: True\nRead Storage: True ",
            "Hacking... 20.63%\n[███░░░░░░░░░░░░░░░░░]",    
            "Hacking... 86.21%\n[███████████████░░░░░]",
            "Hacking... 93.50%\n[█████████████████░░░]",
            "hacking....  100%\n[████████████████████]",
]



small_text = [
               "────▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀█─█\n▀▀▀▀▄─█─█─█─█─█─█──█▀█\n─────▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀─▀",            
               "───║─▄──▄──▄──▄──║────\n───║─▓──▓──▓──▓──║────\n───░░░░░░░░░░░░░─║────\n▀███████████████████──\n░██████████████████▀░░",               
               "───▄▄─▄████▄▐▄▄▄▌\n──▐──████▀███▄█▄▌\n▐─▌──█▀▌──▐▀▌▀█▀\n─▀───▌─▌──▐─▌\n─────█─█──▐▌█",
]




@user_admin
@run_async
def smalltext(bot: Bot, update: Update):
    msg = update.effective_message.reply_text('🔥') 
    for x in range(EDIT_TIMES):
        msg.edit_text(small_text[x%5])
        time.sleep(EDIT_SLEEP)
    msg.edit_text('😅')








@user_admin
@run_async
def hack(bot: Bot, update: Update):
    msg = update.effective_message.reply_text('Target selected') 
    for x in range(EDIT_TIMES):
        msg.edit_text(hack_you[x%5])
        time.sleep(EDIT_SLEEP)
    msg.edit_text('successful hacked')








@user_admin
@run_async
def love(bot: Bot, update: Update):
    msg = update.effective_message.reply_text('❣️') 
    for x in range(EDIT_TIMES):
        msg.edit_text(love_siren[x%5])
        time.sleep(EDIT_SLEEP)
    msg.edit_text('പ്രണയം  😂 ')



__help__ = """

- /love
- /hack
- /smalltext
"""



LOVE_HANDLER = DisableAbleCommandHandler("love", love)
HACK_HANDLER = DisableAbleCommandHandler("hack", hack)
SMALLTEXT_HANDLER = DiasableAbleCommandHandler("smalltext",smalltext)
dispatcher.add_handler(LOVE_HANDLER)
dispatcher.add_handler(HACK_HANDLER)
dispatcher.add_handler(SMALLTEXT_HANDLER)
__mod_name__ = "EMOJIS"
__command_list__ = ["love", "hack", "smalltext"]
__handlers__ = [LOVE_HANDLER, HACK_HANDLER, SMALLTEXT_HANDLER]
