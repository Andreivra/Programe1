import json
import logging
import asyncio
import telegram


data = {'cursanti':
        [{'nume': 'Ionescu',
          'prenume': 'Anton',
          'varsta': 22,
          'hobby': ['snowboard', 'matematica'],
          'numar_tel': {'cod_tara': '+40', 'nr': '756235896'}
          },

         {'nume': 'Mazare',
          'prenume': 'Anastasia',
          'varsta': 19,
          'hobby': ['Hardware', 'fizica'],
          'numar_tel': {'cod_tara': '+33', 'nr': '5689633356'}
          },
         {
             'nume': 'Vasilescu',
             'prenume': 'Andrei',
             'varsta': 21,
             'hobby': ['snowboard', 'matematica'],
             'numar_tel': [{'cod_tara': '+40', 'nr': '756235896'}, {'cod_tara': '+33', 'nr': '5689633357'}]
         }]
        }

data1 = {'nume': 'Titulescu',
         'prenume': 'Bogdan',
         'varsta': 25,
         'hobby': ['snowboard', 'matematica'],
         'numar_tel': [{'cod_tara': '+40', 'nr': '756235896'}]
         }

file_path = 'C:/Users/Andrei/PycharmProjects/pythonProject1'

logging.basicConfig(filename='loger_sda.log', format='- %(asctime)s - %(name)s - %(message)s', filemode='a')
obj_log = logging.getLogger('Program json')
obj_log.setLevel(logging.INFO)

obj_log.info('Inceput de program')

tg_api = '6227517925:AAEG62y40j_iGJqvXdTSceUlejR1OdRagTQ'
id_Constantin = 1307289323
text_to_send = []


async def send_mes(id1, text):
    bot = telegram.Bot(tg_api)
    async with bot:
        await bot.sendMessage(id1, text)


def in_afara_orelor_de_curs(func):
    def wrapper(*args):
        ora_curenta = 12
        if 8 < ora_curenta < 16:
            obj_log.info('S-a verificat functia wrapper')
            return func(*args)
        else:
            text3 = 'Am iesit din afara orelor de program. Nu se poate scrie studentul suplimentar'
            obj_log.info(text3)
            quit()
    return wrapper


@in_afara_orelor_de_curs
def creere_fisier_json(filename='studenti.json'):
    with open(f'{file_path}/{filename}', 'w') as f:
        f.write(json.dumps(data, indent=4))
        obj_log.info('In functia creere fisier json am creat fisierul')


@in_afara_orelor_de_curs
def citire_fisier(filename='studenti.json'):
    creere_fisier_json()
    try:
        with open(f'{file_path}/{filename}', 'r') as f:
            data = json.loads(f.read())
            return data
    except FileNotFoundError:
        obj_log.error("Fisierul nu a fost gasit.")
    obj_log.info('Citim fisierul creat si verificam daca exista(daca a fost creat')


@in_afara_orelor_de_curs
def adaugare_student_la_json(data1, filename='studenti.json'):
    global data
    obj_log.info('Am apelat functia de adaugare')
    citire_fisier()
    with open(filename, 'r+') as f:
        data = json.loads(f.read())
        data["cursanti"].append(data1)
        f.seek(0)
        json.dump(data, f, indent=4)


try:
    adaugare_student_la_json(data1)
    obj_log.info('Am adaugat o intrare suplimentara in fisierul json')
except Exception:
    obj_log.critical('Eroare adaugare intrare suplimentara in fisierul json')
    quit()

text1 = f"Cei {len(data['cursanti'])} studenti sunt: "

text2 = ''
for el in data['cursanti']:
    for key, value in el.items():
        text2 += f"{key} {value}\n"
# asyncio.run(send_mes(id_Constantin, text1 + text2))
obj_log.info(f'Trimitem mesaj pe telegram ')
