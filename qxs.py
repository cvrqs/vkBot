import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


def main():
    vk_session = vk_api.VkApi(
        token='vk1.a.SIagh1n0Ts9oFMBe1NmvUJQphTSs92Cg2YSedBUgaNr8FjcV-cXISV1b5gmYBZpd36C2-X5_WlSAzMEHgT0WbfvplXkS6B2niUcn1JEVn4ttgt9d9gr_8dr8axsxo0q1XWv0BDQk0fRexdOOy1daefOk4ynl5UJPX7xckwgJKMMFQGBNhpZKxC2VoD_xtiYGgm2oJiO8M6jv5Bh5xg2NMA')

    longpoll = VkBotLongPoll(vk_session, 'https://vk.com/public219645497')

    for event in longpoll.listen():
        class VkBot:

            def __init__(self, user_id):
                print("Создан объект бота!")
                self._USER_ID = user_id
                self._USERNAME = self._get_user_name_from_vk_id(user_id)

                self._COMMANDS = ["HELP",
                                  "РАССКАЖИ ОБ ОРГАНИЗАЦИИ",
                                  "ПРЕДОСТАВЬ РАСПИСАНИЕ",
                                  "ПРЕДОСТАВЬ ИНФОРМАЦИЮ О ПРЕПОДОВАТЕЛЯХ",
                                  "ПРЕДОСТАВЬ СПИСОК НАПРАВЛЕНИЙ",
                                  "ПРЕДОСТАВЬ КОНТАКТНЫЕ ДАННЫЕ"]

            def new_message(self, message):

                # 0
                if message.upper() == self._COMMANDS[0]:
                    return self._COMMANDS

                # 1
                elif message.upper() == self._COMMANDS[1]:
                    return 'ЦЦОД "IT-Куб" Вурнарского сельскохозяйственного техникума Минобразования Чувашии\n' \
                           '«IT-куб»— федеральная сеть центров цифрового образования.\n' \
                           '«IT-куб»— новая современная площадка дополнительного образования и интеллектуального развития детей и подростков в сфере современных информационных и телекоммуникационных технологий.\n' \
                           'Обучение в центре цифрового образования "IT-куб" БЕСПЛАТНО.\n' \
                           '«IT-куб» — это уникальная атмосфера для технического творчества, где дети и подростки не просто изучают информационные технологии, а создают программные проекты.'

                # 2
                elif message.upper() == self._COMMANDS[2]:
                    return []

                # 3
                elif message.upper() == self._COMMANDS[3]:
                    return []

                elif message.upper() == self._COMMANDS[4]:
                    return 'Программирование на Python, Разработка VR/AR -приложений, Системное администрирование,' \
                           ' Основы программирования на Java, Лаборатория программирования роботов,' \
                           ' Цифровая гигиена и работа с большими данными, Основы алгоритмики. Пиктомир.,' \
                           'Шахматы, Мобильная разработка, Программирование на Scratch.'

                elif message.upper() == self._COMMANDS[5]:
                    return '+7 (991) 465-11-55'

                else:
                    return "Не понимаю о чем вы..."



if __name__ == '__main__':
    main()
