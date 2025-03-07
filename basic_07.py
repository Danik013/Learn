import ptbot
import os
from dotenv import load_dotenv
import random
import pytimeparse


load_dotenv()
TG_TOKEN = os.getenv("TOKEN")
TG_CHAT_ID = os.getenv("CHAT_ID")


def wait(chat_id, question, bot):
    message_id = bot.send_message(chat_id, "Запускаю таймер...")    
    bot.create_countdown(pytimeparse.parse(question), notify_progress, chat_id=chat_id, message_id=message_id, question=question, bot=bot)
    bot.create_timer(pytimeparse.parse(question), choose, chat_id=chat_id, message_id=message_id, bot=bot)


def choose(chat_id, message_id, bot):
    message = "Время вышло!"
    bot.send_message(chat_id, message,)


def notify_progress(secs_left, question, chat_id, message_id, bot):
    time = pytimeparse.parse(question)
    bot.update_message(chat_id, message_id, "Осталось {} секунд\n{} ".format(secs_left, render_progressbar(time, secs_left)))
    

def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def main():
    bot = ptbot.Bot(TG_TOKEN)
    bot.reply_on_message(wait, bot=bot)
    bot.run_bot()


if __name__ == "__main__":
    main()
