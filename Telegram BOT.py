import random
import telebot
TOKEN = '5197416979:AAG7_JDuiN65jF8-Xr_ryEzOgcLf4apyxrE'

DICES = {
    1: 'CAACAgEAAxkBAAEDu1xh7BdtelPGqeZ9wDaxXwcAAdk7kl0AAn8OAAKCNHoBjFGPRkJXQwEjBA',
    2: 'CAACAgEAAxkBAAEDu15h7BdzAAH0E2bz51XSSiCED1TlicEAAoAOAAKCNHoBDJb6LTO722gjBA',
    3: 'CAACAgEAAxkBAAEDu2Bh7Bd3ibHpSiTgQhM-AQ4O6G9ZCgACgQ4AAoI0egHmMZTw4jEsUiME',
    4: 'CAACAgEAAxkBAAEDu2Jh7Bd9MUSD2gABM3q7_iVldN88oK0AAoIOAAKCNHoBcXoP6t45cr0jBA',
    5: 'CAACAgEAAxkBAAEDu2Rh7Bd_vAx4mkMqQvDkbJYl60IFFgACgw4AAoI0egHMmDGMXUyPXyME',
    6: 'CAACAgEAAxkBAAEDu2Zh7BeCd1XOe3AbmUClUBuhhP_8wQAChA4AAoI0egEyx_5CLNK94CME',
}

def roll_dice():
    dice_index = random.randint(1, 6)
    return DICES[dice_index]
roll_dice()

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands = ['start', 'help'])
def on_roll_dice(message):
    bot.reply_to(message, 'Hi👋, I am DiceBot. I can roll 🎲 for you. I was created by @dandzher. If you wont play, write /roll_dice')

@bot.message_handler(commands = ['roll_dice'])
def on_roll_dice(message):
    dice = roll_dice()
    dice2 = roll_dice()
    bot.send_sticker(message.chat.id, str(dice))
    bot.send_sticker(message.chat.id, str(dice2))



bot.infinity_polling()







