# import datetime
# import time
# import os
#
# CLEAR = "\033[2J"
# CLEAR_AND_RETURN = "\033[H"
#
#
# while True:
#     os.system('clear')
#     time.sleep(1)
#     hour_now = datetime.datetime.now().hour
#     min_now = datetime.datetime.now().minute
#     sec_now = datetime.datetime.now().second
#     print(f"{CLEAR_AND_RETURN}Este ora {hour_now:02d} : {min_now:02d} minute si {sec_now:02d} secunde")
# import datetime
# import logging
#
# logging.basicConfig(filename='loger_sda.log', format = '%(asctime)s %(message)s', filemode='w')
#
# obj_log = logging.getLogger()
#
# """
# Niveluri de logging:
# debug: cel mai jos nivel de alerta
# info: info
# warning: atrage atentia
# error
# critical
# """
#
# obj_log.setLevel(logging.DEBUG)
# obj_log.debug("Just an info")
#
#
# def division_stuff(x, y):
#     return x/y
#
# a = 8
# b= 0
#
# try:
#     print(division_stuff(a,b))
#     obj_log.info("Done division")
# except ZeroDivisionError:
#     obj_log.critical(f"Zero division of function division_stuff with arguments {a,b}")

# import json
# import logging
# import asyncio
# import telegram
# import os
#
# data = {'cursanti':
#             [{'nume': 'Ionescu',
#               'prenume': 'Anton',
#               'varsta': 22,
#               'hobby': ['snowboard', 'matematica'],
#               'numar_tel': {'cod_tara': '+40', 'nr': '756235896'}
#               },
#
#              {'nume': 'Mazare',
#               'prenume': 'Anastasia',
#               'varsta': 19,
#               'hobby': ['Hardware', 'fizica'],
#               'numar_tel': {'cod_tara': '+33', 'nr': '5689633356'}
#               },
#              {
#                  'nume': 'Vasilescu',
#                  'prenume': 'Andrei',
#                  'varsta': 21,
#                  'hobby': ['snowboard', 'matematica'],
#                  'numar_tel': [{'cod_tara': '+40', 'nr': '756235896'}, {'cod_tara': '+33', 'nr': '5689633357'}]
#              }]
#         }
#
#
#
# #
# # nrx = data['cursanti'][-1]['numar_tel'][0]['nr']
# # print(nrx)
#
# # print(data['cursanti'])
# #
# # nume_1 = data['cursanti'][0]['nume']
# # print(nume_1)
# #
# # for el in data['cursanti']:
# #     print(el['nume'])
#
# data1 ={'nume': 'Titulescu',
#                'prenume': 'Bogdan',
#                'varsta': 25,
#                'hobby': ['snowboard', 'matematica'],
#                'numar_tel': [{'cod_tara': '+40', 'nr': '756235896'}]
#                }
#
#
# tg_api = '6227517925:AAEG62y40j_iGJqvXdTSceUlejR1OdRagTQ'
# id_Constantin = 1307289323
# text_to_send = []
#
#
# async def send_mes(id, text):
#     bot = telegram.Bot(tg_api)
#     async with bot:
#         await bot.sendMessage(id, text)
#
#
# file_path = 'C:/Users/Andrei/PycharmProjects/pythonProject1'
#
# logging.basicConfig(filename='loger_sda.log', format='%(asctime)s %(message)s', filemode='w')
# obj_log = logging.getLogger()
# obj_log.setLevel(logging.INFO)
#
# obj_log.info('Inceput de program')
#
#
# def in_afara_orelor_de_curs(func):
#     def wrapper(*args):
#         ora_curenta = 12
#         if 8 < ora_curenta < 16:
#             return func(*args)
#         else:
#             text3 = 'Am iesit din afara orelor de program. Nu se poate scrie studentul suplimentar'
#             asyncio.run(send_mes(id_Constantin, text3))
#             quit()
#     return wrapper
#
#
# @in_afara_orelor_de_curs
# def student_adauga():
#     with open(f'{file_path}/student.json', 'w') as f:
#         f.write(json.dumps(data, indent=2))
#         obj_log.info('Adaugam prima lista de studenti')
#
#
# data['cursanti'].append(data1)
#
#
# @in_afara_orelor_de_curs
# def adauga_student_suplimentar():
#     with open(f'{file_path}/student.json', 'r') as f_read:
#         data = json.load(f_read)
#     try:
#         data.update(data1)
#         json.dump(data, f_read)
#         obj_log.info('Adaugam si studentul suplimentar')
#     except Exception as e:
#         print(f'Error adding student: {str(e)}')
#
#
# student_adauga()
# adauga_student_suplimentar()
#
# text1 = f"Cei {len(data['cursanti']) + len(data1)} studenti sunt: "
# print(text1)
# text2 = ''
# for el in data['cursanti']:
#     for key, value in el.items():
#         text2 += f"{key} {value}\n"
#         print(text2)
# # asyncio.run(send_mes(id_Constantin, text1 + text2))
# obj_log.info(f'Trimitem mesaj pe telegram ')
