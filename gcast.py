from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors import FloodWaitError
from time import sleep, time
from colorama import Fore,Style, init as color_ama
color_ama(autoreset=True)
import json, re, sys, os, random

banner = Style.BRIGHT+Fore.YELLOW +  """

   ____               _   
  / ___| ___ __ _ ___| |_ 
 | |  _ / __/ _` / __| __|
 | |_| | (_| (_| \__ \ |_ 
  \____|\___\__,_|___/\__|
                          """

putih = Style.BRIGHT+Fore.WHITE
hijau = Style.BRIGHT+Fore.GREEN
merah = Style.BRIGHT+Fore.RED
kuning = Style.BRIGHT+Fore.YELLOW
reset = Fore.RESET
biru = Style.BRIGHT+Fore.BLUE


os.system('clear') 
print(banner)
print("\n")
print(f'{hijau}[+] Indonesia/English')
import random
import sys
import time
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.2)
#ubah angka 0.1 sesuai keinginan kamu
#angka terkecil adalah yang paling cepat
#angka terbesar adalah yang paling lambat
mengetik("[+] Ini Ada\n[+] Semua Res!\n[+] Th\n[+] All \n")
if not os.path.exists('session'):
    os.makedirs('session')
if len(sys.argv) < 2:
    print( Fore.RED + '\n\nUsage : python main.py +62' + Fore.RESET)
    sys.exit(1)
api_id = 29826983
api_hash = '8de0ed7bbdc2d04c1938226d6bb9af38'
phone_number = sys.argv[1]
client = TelegramClient('session/' + phone_number, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    try:
        client.send_code_request(phone_number)
        me = client.sign_in(phone_number, input(Fore.WHITE + 'Enter Yout Code Code : '))
    except SessionPasswordNeededError:
        passw = input(Fore.RESET + 'Your 2fa Password : ')
        me = client.start(phone_number, passw)
saia = client.get_me()
print('[*]Account:',saia.first_name)
print('[*]Phone:',saia.phone,'\n')
channel_username = '@gcstbosss'
channel_entity = client.get_entity('@gcstbosss')
print('Memulai Bot Gcast..!')


while True:
  try:
    client.send_message(entity=channel_entity, message='.gikes group halo semuaa ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(250)
    client.send_message(entity=channel_entity, message='.limit')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(8)
    client.send_message(entity=channel_entity, message='.gikes group LIIVE OMEEK TALEENT CEK DI BIIIO 😍😍😍

LIIVE OMEEK TALEENT CEK DI BIIIO 😍😍😍

LIIVE OMEEK TALEENT CEK DI BIIIO 😍😍😍')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(250)
    client.send_message(entity=channel_entity, message='.gikes group cape bgt main tele dri 2023 ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(250)
    client.send_message(entity=channel_entity, message='.gikes group detol ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(250)
    client.send_message(entity=channel_entity, message='.gikes group ngeri banget liat nya deck ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(250)
    client.send_message(entity=channel_entity, message='.limit')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(8)
    client.send_message(entity=channel_entity, message='.gikes group ydh si ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(250)
    client.send_message(entity=channel_entity, message='.gikes group ell opn bgt ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(250)
    client.send_message(entity=channel_entity, message='.gikes group apalah😭😭 ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(250)
    client.send_message(entity=channel_entity, message='.gikes group jgn lupa nyolong kotak amal biar amalnya banyak ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(250)
    client.send_message(entity=channel_entity, message='.limit')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(8)
    client.send_message(entity=channel_entity, message='.gikes group duh kedeak ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(250)
    client.send_message(entity=channel_entity, message='.gikes group ka sini ke b1y0 temani aku ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(250)
    client.send_message(entity=channel_entity, message='.gikes group vc,s yuk ')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(250)
    
  except:
    print(f'{hijau} Gcast gagal.! {putih} gcast by : ruz')
    sleep(120)

sys.exit()
client.disconnect()
