import asyncio
from depspy import DepsClient
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

client = DepsClient(api_key="your_api_key_here")

async def get_server_stats(server_id: int):
    try:
        online = await client.get_online_players(server_id)
        fractions = await client.get_fractions(server_id)
        admins = await client.get_admins(server_id)
        return {
            "server_id": server_id,
            "online_count": len(online.data) if online and online.data else 0,
            "fractions_count": len(fractions.data) if fractions and fractions.data else 0,
            "admins_count": len(admins.admins) if admins and admins.admins else 0
        }
    except Exception as e:
        return {
            "server_id": server_id,
            "error": str(e)
        }

async def cmd_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        server_id = int(context.args[0])
        stats = await get_server_stats(server_id)
        if "error" in stats:
            await update.message.reply_text(f"Ошибка сервера {stats['server_id']}: {stats['error']}")
        else:
            response = f"📊 Статистика сервера {stats['server_id']}:\n"
            response += f"👥 Онлайн: {stats['online_count']}\n"
            response += f"🏢 Фракции: {stats['fractions_count']}\n"
            response += f"👮 Админы: {stats['admins_count']}"
            await update.message.reply_text(response)
    except (IndexError, ValueError):
        await update.message.reply_text("Используйте команду в формате: /info номер_сервера")

def main():
    app = Application.builder().token("your_api_key_here_from_bot_father").build()
    app.add_handler(CommandHandler("info", cmd_info))
    app.run_polling()

if __name__ == "__main__":
    main()