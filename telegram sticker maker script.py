from telegram import Bot, InputStickerSetItem, Update
from telegram.error import TelegramError
from telegram.ext import Updater, CommandHandler, ContextTypes
from PIL import Image
import os

# Telegram Bot Token
TOKEN = '7338128711:AAHvHGZ2d4-4dn815qP5cYg7Jqb1g4NkVYA'

# Create a Telegram Bot instance
bot = Bot(token=TOKEN)

# Specify the input and output folders
input_folder = 'output_images'
sticker_pack_name = 'My Sticker Pack'

# Create a list to store the sticker set
sticker_set = []

# Iterate over all files in the input folder
for filename in os.listdir(input_folder):
    # Check if the file is an image
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
        # Open the image
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # Check if the image is 512x512 pixels
        if img.size != (512, 512):
            print(f"Skipping {filename} (not 512x512 pixels)")
            continue

        # Convert GIF images to PNG
        if filename.lower().endswith('.gif'):
            png_filename = filename.replace('.gif', '.png')
            png_path = os.path.join(input_folder, png_filename)
            img.save(png_path)
            img_path = png_path

        # Add the sticker to the sticker set
        sticker_set.append(InputStickerSetItem(png_sticker=open(img_path, 'rb'), emojis=''))

# Create the sticker set
try:
    set_name = f"{sticker_pack_name}_by_{bot.username}"
    png_sticker_path = os.path.join(input_folder, next((f for f in os.listdir(input_folder) if f.endswith('.png')), None))
    if png_sticker_path:
        bot.create_new_sticker_set(
            user_id=1173941658,  
            name=set_name,
            title=sticker_pack_name,
            stickers=sticker_set,
            png_sticker=open(png_sticker_path, 'rb')
        )
        print(f"Sticker pack '{sticker_pack_name}' created successfully!")
        print(f"Telegram Bot Link: https://t.me/{bot.username}")
except TelegramError as e:
    print(f"Error creating sticker pack: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Define a command handler for the /get command
def get_sticker_pack(update: Update, context: ContextTypes) -> None:
    set_name = f"{sticker_pack_name}_by_{bot.username}"
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Get the sticker pack here: t.me/addstickers/{set_name}")

# Create an Updater and pass it the bot's token
updater = Updater(TOKEN)

# Get the dispatcher to register handlers
dp = updater.dispatcher

# Register the /get command handler
dp.add_handler(CommandHandler("get", get_sticker_pack))

# Start the bot
updater.start_polling()
updater.idle()