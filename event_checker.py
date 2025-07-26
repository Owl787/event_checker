import discord
from discord.ext import commands
import sys

print("✅ Python Version:", sys.version)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", self_bot=True, intents=intents)

allowed_users = [
    123456789012345678,  # Replace with real allowed user IDs
    987654321098765432
]

correct_emoji = "✅"
wrong_emoji = "❌"
event_channel_id = 112233445566778899  # Replace with your actual event channel ID

@bot.event
async def on_ready():
    print(f"🚀 Bot started as {bot.user} | تم تشغيل البوت بنجاح")

@bot.event
async def on_reaction_add(reaction, user):
    if reaction.message.channel.id != event_channel_id:
        return
    if user.id == bot.user.id:
        return
    if user.id in allowed_users:
        print(f"✅ Allowed reaction by {user} ({user.id}) | تم التفاعل الصحيح من {user}")
    else:
        try:
            await reaction.remove(user)
            print(f"❌ Removed invalid reaction from {user} ({user.id}) | تم حذف تفاعل غير مسموح")
        except Exception as e:
            print(f"⚠️ Error removing reaction: {e}")

bot.run("YOUR_DISCORD_ACCOUNT_TOKEN", bot=False)
