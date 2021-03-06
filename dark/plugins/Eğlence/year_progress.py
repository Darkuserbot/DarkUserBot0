#by @deleteduser420
import datetime
from userge import userge
import math

@userge.on_cmd("yp$", about={'header': "Yıl durum Çubuğu"})
async def progresss(message):
    x = datetime.datetime.now()
    day = int(x.strftime("%j"))
    
    percent = math.trunc( day / 366 * 100 )
    #366 days cuz leap year xD
    num = round(percent/5)
    
    progress = [
    "░░░░░░░░░░░░░░░░░░░░",
    "▓░░░░░░░░░░░░░░░░░░░",
    "▓▓░░░░░░░░░░░░░░░░░░",
    "▓▓▓░░░░░░░░░░░░░░░░░",
    "▓▓▓▓░░░░░░░░░░░░░░░░",
    "▓▓▓▓▓░░░░░░░░░░░░░░░",
    "▓▓▓▓▓▓░░░░░░░░░░░░░░",
    "▓▓▓▓▓▓▓░░░░░░░░░░░░░",
    "▓▓▓▓▓▓▓▓░░░░░░░░░░░░",
    "▓▓▓▓▓▓▓▓▓░░░░░░░░░░░",
    "▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░",
    "▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░",
    "▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░",
    "▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░",
    "▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░",
    "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░",
    "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░",
    "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░",
    "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░",
    "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░",
    "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓",
    ]

    message_out  =   "<b>Yılın durumu</b>\n"
    message_out  += f"<code>{progress[num]} {percent}</code>"
    message_out  +=  "`%`"
    await message.edit(message_out)
