import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import requests

vk_session = vk_api.VkApi(token='vk1.a.lEKeoY0XU50m2UXlZ-COJ7z0YB0U-oPnHP1a6cjlh7CSavPSiJHQr9nN-1Zmti-jPVKMac0uSB_Y8VjfEUiQhO-NewpADX42HHxApAxjw9RR1hsk7FLfLq10JuK9ym2xMDiGjRTLGxbiCFz6eJn5LZ3vE0yAFfxVS7u7Ial_epSzRgLGMOyqwACDahSkDsDQlkXSDPy6U9nykM2qhjPs4Q')
session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)
proverka_chisel = False
proverka_photo = False


def vstavkaphoto(id, photo):
    a = vk_session.method("photos.getMessagesUploadServer")
    b = requests.post(a['upload_url'], files={'photo': open(photo, 'rb')}).json()
    c = \
        vk_session.method('photos.saveMessagesPhoto',
                          {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[
            0]
    d = "photo{}_{}".format(c["owner_id"], c["id"])
    vk_session.method("messages.send", {"peer_id": id, "attachment": d, "random_id": 0})


spisok = ['прив', 'здрав', 'добрый вечер', 'добрый день', 'доброе утр', 'ало', 'але', 'доброй ноч', 'хай', 'ку', 'йо', 'здаров']
spisok_func = ['контактные данные', 'список направлений', 'информация организации', 'расписание', 'информацию о преподавателях']

def send_some_msg(id, some_text):
    vk_session.method("messages.send", {"user_id": id, "message":some_text, "random_id":0})

for event in longpool.listen():

    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower()
            id_p = event.user_id
            for i in spisok:
                if i in msg:
                    send_some_msg(id_p, 'Здравствуйте, я бот It-куб.Вурнары. Чтобы ознакомиться с моими возможностями, введите "Помощь"')
                    break


            else:

                if msg == spisok_func[2]:
                    send_some_msg(id_p,
                                  'ЦЦОД "IT-Куб" Вурнарского сельскохозяйственного техникума Минобразования Чувашии.\n'
                                  '«IT-куб»— федеральная сеть центров цифрового образования.\n'
                                  '«IT-куб»— новая современная площадка дополнительного образования и интеллектуального развития детей и подростков в сфере современных информационных и телекоммуникационных технологий.\n'
                                  '«IT-куб» — это уникальная атмосфера для технического творчества, где дети и подростки не просто изучают информационные технологии, а создают программные проекты.')

                elif msg == spisok_func[1]:
                    send_some_msg(id_p, '-Программирование на Python\n'
                                      '-Разработка VR/AR -приложений\n'
                                      '-Системное администрирование\n'
                                      '-Основы программирования на Java\n'
                                      '-Лаборатория программирования роботов\n'
                                      '-Цифровая гигиена и работа с большими данными\n'
                                      '-Основы алгоритмики. Пиктомир.\n'
                                      '-Шахматы\n'
                                      '-Мобильная разработка\n'
                                      '-Программирование на Scratch')

                elif msg == spisok_func[0]:
                    send_some_msg(id_p, 'Вот наш номер телефона, по которому вы можете нам звонить: +7 (991) 465-11-55')



                elif msg == 'помощь':
                    proverka_chisel = True
                    proverka_photo = False
                    send_some_msg(id_p, '1. ""Контактные данные""\n'
                                      '2. ""Список направлений""\n'
                                      '3. ""Информация организации""\n'
                                      '4. ""Расписание""\n'
                                      '5. ""Информацию о преподавателях""\n')


                elif msg == spisok_func[3]:
                    proverka_chisel = False
                    proverka_photo = True
                    send_some_msg(id_p, 'Выберите необходимые пункты:\n'
                                      '1.Основы программирования java, шахматы, программирование на Scrathc, мобильная разработка.\n'
                                      '2.Лаборатория программирования роботов\n'
                                        '3.Цифровая гигиена и работа с большими данными, Основы алгоритмики. Пиктомир.\n'
                                        '4.Разработка VR/AR -приложений.\n'
                                        '5.Программирование на Python')
                # 1 фото
                elif proverka_photo and msg == '1':
                    vstavkaphoto(id_p, 'img_5.png')
                # 2 фото
                elif proverka_photo and msg == '2':
                    vstavkaphoto(id_p, 'img_6.png')
                # 3 фото
                elif proverka_photo and msg == '3':
                    vstavkaphoto(id_p, 'img_7.png')
                # 4 фото
                elif proverka_photo and msg == '4':
                    vstavkaphoto(id_p, 'img_8.png')
                # 5 фото
                elif proverka_photo and msg == '5':
                    vstavkaphoto(id_p, 'img_9.png')

                    # 4 фото

                elif msg == spisok_func[4]:
                    send_some_msg(id_p,
                                  'Заместитель руководителя по работе с федеральной сетью и внешними партнерами - Петриченко Петр Александрович\n'
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
                elif 'пок' in msg or 'до свидания' in msg:
                    send_some_msg(id_p, 'Пока')

                elif proverka_chisel and msg == '1':

                    send_some_msg(id_p, 'Вот наш номер телефона, по которому вы можете нам звонить: +7 (991) 465-11-55')

                elif proverka_chisel and msg == '2':

                    send_some_msg(id_p, '-Программирование на Python\n'
                                        '-Разработка VR/AR -приложений\n'
                                        '-Системное администрирование\n'
                                        '-Основы программирования на Java\n'
                                        '-Лаборатория программирования роботов\n'
                                        '-Цифровая гигиена и работа с большими данными\n'
                                        '-Основы алгоритмики. Пиктомир.\n'
                                        '-Шахматы\n'
                                        '-Мобильная разработка\n'
                                        '-Программирование на Scratch')
                elif proverka_chisel and msg == '3':

                    send_some_msg(id_p,
                                  'ЦЦОД "IT-Куб" Вурнарского сельскохозяйственного техникума Минобразования Чувашии.\n'
                                  '«IT-куб»— федеральная сеть центров цифрового образования.\n'
                                  '«IT-куб»— новая современная площадка дополнительного образования и интеллектуального развития детей и подростков в сфере современных информационных и телекоммуникационных технологий.\n'
                                  '«IT-куб» — это уникальная атмосфера для технического творчества, где дети и подростки не просто изучают информационные технологии, а создают программные проекты.')

                elif proverka_chisel and msg == '4':
                    proverka_chisel = False
                    proverka_photo = True
                    send_some_msg(id_p, 'Выберите необходимые пункты:\n'
                                        '1.Основы программирования java, шахматы, программирование на Scrathc, мобильная разработка.\n'
                                        '2.Лаборатория программирования роботов\n'
                                        '3.Цифровая гигиена и работа с большими данными, Основы алгоритмики. Пиктомир.\n'
                                        '4.Разработка VR/AR -приложений.\n'
                                        '5.Программирование на Python')

                elif proverka_photo and msg == '1':
                    vstavkaphoto(id_p, 'img_5.png')

                elif proverka_photo and msg == '2':
                    vstavkaphoto(id_p, 'img_6.png')

                elif proverka_photo and msg == '3':
                    vstavkaphoto(id_p, 'img_7.png')

                elif proverka_photo and msg == '4':
                    vstavkaphoto(id_p, 'img_8.png')

                elif proverka_photo and msg == '5':
                    vstavkaphoto(id_p, 'img_9.png')

                elif proverka_chisel and msg == '5':
                    send_some_msg(id_p,
                                  'Заместитель руководителя по работе с федеральной сетью и внешними партнерами - Петриченко Петр Александрович\n'
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
                    send_some_msg(id_p,
                                  'Извините, я вас не понимаю. Чтобы узнать мои возможности напишите команду "Помощь"')



