from telethon.sync import TelegramClient
import datetime
import time
import sys
import re
import os
import platform
from dataconfig import api_id, api_hash, chats


canal = "GM6mdAQjjZuAiwA1zjza"
client =  TelegramClient('aquilesfromtroy', api_id, api_hash)
card_file = 'TC-Recopiladas-{}.txt'.format(datetime.date.today())


year = int(sys.argv[1])
mes = int(sys.argv[2])
dia = int(sys.argv[3])

sistema = platform.system()

if sistema == 'Linux':
    os.system('clear')
else:
    os.system("cls")

print("\n[*] Ejecutando barrido... vaya por un café...\n")

j = open("ccards.txt", "w", encoding="utf-8")

date_of_post = datetime.datetime(year, mes, dia)

for chat in chats:
    with TelegramClient('test', api_id, api_hash) as client:
        print("[-] Extrayendo info desde: %s" % chat)
        try:
            for message in client.iter_messages(chat, offset_date=date_of_post , reverse=True):
                data = message.text
                #tcs = re.findall(r'([456][0-9]{14}[0-9][^a-zA-Z\']\d+.\d+.\d+)',str(data))
                #tcs = re.findall(r'([456][0-9]{15}[^a-zA-Z\']\d+.\d+.\d+)',str(data))
                tcs = re.findall(r'([456][0-9]{15})',str(data))
                j.write(str(tcs))
        except Exception as e:
            print(e,":", chat)
            continue

j.close()

with open("ccards.txt", "r") as card:
    cards = card.read()
    limpiar_lineas = re.sub(r'(\[)|(\')',"",cards)
    limpiar = re.sub(r'(\])|(\,)',"\n",limpiar_lineas)
    limpiar_card = re.sub(r'( )',"",limpiar)
    print('[*] Creando archivo de tarjetas...\n')
    with open("base_limpia.txt", "w", encoding="utf-8") as cleandata:
        cleandata.write(limpiar_card.strip())
        cleandata.close()

tarjetas = []

base = open("base_limpia.txt")
base_limpia = base.read()
tc_negocio = re.findall(r'(^(404028).+|^(409152).+|^(409767).+|^(421413).+|^(445596).+|^(447409).+|^(447410).+|^(447411).+|^(460072).+|^(465375).+|^(499847).+|^(512795).+|^(513689).+|^(514332).+|^(522375).+|^(522468).+|^(528209).+|^(530756).+|^(533187).+|^(548740).+|^(548742).+|^(558984).+|^(603142).+|^(627180).+|^(627180).+|^(627180).+|^(854881).+|^(854899).+|^(881006).+|^(881052).+|^(407876).+|^(512269).+)', base_limpia, re.MULTILINE)
base.close()

buscar = tarjetas.append(tc_negocio)
#nuevas = re.findall(r'([456][0-9]{15}.[0-9].{10})', str(tarjetas))
nuevas = re.findall(r'([456][0-9]{15})', str(tarjetas))
eliminar_espacios = '|\n'.join(nuevas)+'|'
#limpiar_lineas = re.sub(r'(\[)|(\])|(\")|(\')',"", str(nuevas))
#eliminar_coma = re.sub(r'(\,)',"\n", limpiar_lineas)
#eliminar_espacios = re.sub(r'( )',"", eliminar_coma)

tc_nuevas = open(card_file, "w", encoding="utf-8")
tc_nuevas.write(str(eliminar_espacios))

print("[*] Datos recopilados y enviados con éxito!\n")


if sistema == 'Linux':
    os.system('rm ccards.txt')
    os.system('rm base_limpia.txt')
else:
    os.system('del ccards.txt')
    os.system('del base_limpia.txt')

###Script version 5 scrapeergram.py