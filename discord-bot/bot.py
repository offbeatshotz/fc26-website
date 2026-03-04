import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from models import init_db, Script

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///discord_bot.db')

# Initialize database session
session: Session = init_db(DATABASE_URL)

intents = discord.Intents.default()
intents.message_content = True  # Required for accessing message content

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print('Database tables created/checked.')

@bot.command(name='uploadscript')
async def uploadscript(ctx, name, platform, description, *, script_content):
    """Upload a new script to the database."""
    try:
        new_script = Script(
            name=name,
            description=description,
            platform=platform,
            script_content=script_content,
            uploaded_by=str(ctx.author)
        )
        session.add(new_script)
        session.commit()
        await ctx.send(f'Script \'{name}\' for {platform} uploaded successfully by {ctx.author.mention}!')
    except Exception as e:
        session.rollback()
        await ctx.send(f'Error uploading script: {e}')

@bot.command(name='downloadscript')
async def downloadscript(ctx, name: str):
    """Download a script by its name."""
    script = session.query(Script).filter_by(name=name).first()
    if script:
        await ctx.author.send(f'Script Name: {script.name}\nPlatform: {script.platform}\nDescription: {script.description}\n\n```\n{script.script_content}\n```')
        await ctx.send(f'Script \'{name}\' sent to your DMs, {ctx.author.mention}.')
    else:
        await ctx.send(f'Script \'{name}\' not found.')

@bot.command(name='listscripts')
async def listscripts(ctx):
    """List all available scripts."""
    scripts = session.query(Script).all()
    if scripts:
        response = "**Available Scripts:**\n"
        for script in scripts:
            response += f"- {script.name} ({script.platform}) - Uploaded by {script.uploaded_by}\n"
        await ctx.send(response)
    else:
        await ctx.send("No scripts available yet.")

bot.run(TOKEN)
