from telethon import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from config import api_hash, api_id, session_name, images_path, sessions_path, images_name_template, time_zone, time_delta_hours, system_version
from datetime import datetime, timedelta
from argparse import ArgumentParser, ArgumentTypeError
from pytz import timezone
from pathlib import Path


def valid_tz(s):
  try:
    return timezone(s)
  except:
    msg = "Not a valid tz: '{0}'.".format(s)
    raise ArgumentTypeError(msg)


parser = ArgumentParser()
parser.add_argument("--api_id", required=False, help="user api ID", type=str, default=api_id)
parser.add_argument("--api_hash", required=False, help="user api Hash", type=str, default=api_hash)
parser.add_argument("--tz", required=False, help="time zone", type=valid_tz, default=valid_tz(time_zone))
parser.add_argument("--session_name", required=False, help="session name", type=str, default=session_name)
parser.add_argument("--time_delta_hours", required=False, help="time delta hours", type=int, default=time_delta_hours)

parser.add_argument("--system_version", required=False, help="system_version", type=str, default=system_version)

args = parser.parse_args()
session_path = sessions_path + args.session_name

if not Path(sessions_path).exists():
  from os import makedirs
  makedirs(sessions_path)

client = TelegramClient(session_path, args.api_id, args.api_hash, system_version = system_version)
client.start()


async def main():
  now = datetime.now(args.tz)
  filename = (now + timedelta(hours=args.time_delta_hours)).strftime(images_name_template)
  filepath = Path(images_path + filename)
  if filepath.is_file():
    await client(DeletePhotosRequest(await client.get_profile_photos("me")))
    file = await client.upload_file(filepath)
    await client(UploadProfilePhotoRequest(file = file))
  else:
    print(f'File "{filepath}" not found')


if __name__ == '__main__':
  from asyncio import get_event_loop
  get_event_loop().run_until_complete(main())