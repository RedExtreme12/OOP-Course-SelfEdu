class Message:

    def __init__(self, text):
        self.text = text
        self.fl_like = False


class Viber:

    messages = []

    @classmethod
    def add_message(cls, msg: Message):
        cls.messages.append(msg)

    @classmethod
    def remove_message(cls, msg: Message):
        cls.messages.remove(msg)

    @classmethod
    def set_like(cls, msg: Message):
        # for msg_obj in cls.messages:
        #     if msg is msg_obj:
        #         desired_msg_obj = msg_obj
        #         break
        # else:
        #     return None

        # if desired_msg_obj.fl_like:
        #     desired_msg_obj.fl_like = False
        # else:
        #     desired_msg_obj.fl_like = True

        if msg.fl_like:
            msg.fl_like = False
        else:
            msg.fl_like = True

    @classmethod
    def show_last_message(cls, count: int):
        return cls.messages[:-count]

    @classmethod
    def total_messages(cls):
        return len(cls.messages)


# msg = Message("Всем привет!")
# msg1 = Message('Hi!!!!')
# Viber.add_message(msg)
# Viber.add_message(Message("Это курс по Python ООП."))
# Viber.add_message(Message("Что вы о нем думаете?"))
# Viber.set_like(msg)
# Viber.set_like(msg1)
# print(msg1.fl_like)
# Viber.remove_message(msg)
