import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import requests

vk_session = vk_api.VkApi(token='vk1.a.lEKeoY0XU50m2UXlZ-COJ7z0YB0U-oPnHP1a6cjlh7CSavPSiJHQr9nN-1Zmti-jPVKMac0uSB_Y8VjfEUiQhO-NewpADX42HHxApAxjw9RR1hsk7FLfLq10JuK9ym2xMDiGjRTLGxbiCFz6eJn5LZ3vE0yAFfxVS7u7Ial_epSzRgLGMOyqwACDahSkDsDQlkXSDPy6U9nykM2qhjPs4Q')
session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)

spisok = ['прив', 'здрав', 'добрый вечер', 'добрый день', 'доброе утр', 'ало', 'але', 'доброй ноч', 'хай', 'ку']
def send_some_msg(id, some_text):
    vk_session.method("messages.send", {"user_id": id, "message":some_text, "random_id":0})

for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower()
            id = event.user_id
            if msg == 'расскажи об организации':
                send_some_msg(id, 'ЦЦОД "IT-Куб" Вурнарского сельскохозяйственного техникума Минобразования Чувашии.\n'
                                  '«IT-куб»— федеральная сеть центров цифрового образования.\n'
                                  '«IT-куб»— новая современная площадка дополнительного образования и интеллектуального развития детей и подростков в сфере современных информационных и телекоммуникационных технологий.\n'
                                  '«IT-куб» — это уникальная атмосфера для технического творчества, где дети и подростки не просто изучают информационные технологии, а создают программные проекты.')

            elif msg == 'предоставь список направлений':
                send_some_msg(id, '1.Программирование на Python\n'
                                  '2.Разработка VR/AR -приложений\n'
                                  '3.Системное администрирование\n'
                                  '4.Основы программирования на Java\n'
                                  '5.Лаборатория программирования роботов\n'
                                  '6.Цифровая гигиена и работа с большими данными\n'
                                  '7.Основы алгоритмики. Пиктомир.\n'
                                  '8.Шахматы\n'
                                  '9.Мобильная разработка\n'
                                  '10.Программирование на Scratch')

            elif msg == 'предоставь контактные данные':
                send_some_msg(id, '+7 (991) 465-11-55')


            elif msg in spisok:
                send_some_msg(id, 'Здравствуйте, чтобы узнать мои возможности напишите команду "help".')

            elif msg == 'help':
                send_some_msg(id, '1.Предоставь контактные данные\n'
                                  '2.Предоставь список направлений\n'
                                  '3.Расскажи об организации\n'
                                  '4.Предоставь расписание\n'
                                  '5.Предоставь информацию о преподавателях\n')
            elif msg == 'предоставь расписание':
                a = vk_session.method("photos.getMessagesUploadServer")
                b = requests.post(a['upload_url'], files={'photo': open('img_5.png', 'rb')}).json()
                c = \
                vk_session.method('photos.saveMessagesPhoto', {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[
                    0]
                d = "photo{}_{}".format(c["owner_id"], c["id"])
                vk_session.method("messages.send", {"peer_id": id, "attachment": d, "random_id": 0})
                # safdsafasf




                a = vk_session.method("photos.getMessagesUploadServer")
                b = requests.post(a['upload_url'], files={'photo': open('img_6.png', 'rb')}).json()
                c = \
                    vk_session.method('photos.saveMessagesPhoto',
                                      {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[
                        0]
                d = "photo{}_{}".format(c["owner_id"], c["id"])
                vk_session.method("messages.send",
                                  {"peer_id": id, "attachment": d, "random_id": 0})
                # safdsafasf



                a = vk_session.method("photos.getMessagesUploadServer")
                b = requests.post(a['upload_url'], files={'photo': open('img_7.png', 'rb')}).json()
                c = \
                    vk_session.method('photos.saveMessagesPhoto',
                                      {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[
                        0]
                d = "photo{}_{}".format(c["owner_id"], c["id"])
                vk_session.method("messages.send",
                                  {"peer_id": id, "attachment": d, "random_id": 0})

                # safdsafasf

                a = vk_session.method("photos.getMessagesUploadServer")
                b = requests.post(a['upload_url'], files={'photo': open('img_8.png', 'rb')}).json()
                c = \
                    vk_session.method('photos.saveMessagesPhoto',
                                      {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[
                        0]
                d = "photo{}_{}".format(c["owner_id"], c["id"])
                vk_session.method("messages.send",
                                  {"peer_id": id, "attachment": d, "random_id": 0})
                # sadsafsa
                a = vk_session.method("photos.getMessagesUploadServer")
                b = requests.post(a['upload_url'], files={'photo': open('img_9.png', 'rb')}).json()
                c = \
                    vk_session.method('photos.saveMessagesPhoto',
                                      {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[
                        0]
                d = "photo{}_{}".format(c["owner_id"], c["id"])
                vk_session.method("messages.send",
                                  {"peer_id": id, "attachment": d, "random_id": 0})


            elif msg == 'предоставь информацию о преподавателях':
                send_some_msg(id,'Заместитель руководителя по работе с федеральной сетью и внешними партнерами - Петриченко Петр Александрович\n'
                                 '\n'
                                 'Заместитель руководителя, заведующая учебной частью -  Казенова Ирина Петровна\n'
                                 '\n'
                                 'Методист - Мнейкина Анастасия Александровна\n'
                                 '\n'
                                 'Педагог дополнительного образования - Павлова Екатерина Сергеевна\n'
                                 '\n'
                                 'Педагог дополнительного образования - Репин Анатолий Владимирович\n'
                                 '\n'
                                 'Педагог дополнительного образования - Нарышкин Владимир Александрович\n'
                                 '\n'
                                 'Педагог дополнительного образования - Васильева Юлия Александровна\n'
                                 '\n'
                                 'Педагог дополнительного образования - Трофимова Кристина Сергеевна\n'
                                 '\n'
                                 'Педагог дополнительного образования - Никитин Александр Николаевич\n'
                                 '\n'
                                 'Педагог дополнительного образования - Иванов Руслан Олегович\n'
                                 '\n'
                                 'Педагог дополнительного образования - Глухов Владимир Анатольевич\n'
                                 '\n'
                                 'Педагог дополнительного образования - Чермаков Владимир Сергеевич\n'
                                 '\n'
                                 'Педагог дополнительного образования - Иванова Любовь Анатольевна')

            else:
                for i in spisok:
                    if i in msg:
                        send_some_msg(id, 'Здравствуйте, чтобы узнать мои возможности напишите команду "help".')


                send_some_msg(id,'Извините, я вас не понимаю. Чтобы узнать мои возможности напишите команду "help"')







