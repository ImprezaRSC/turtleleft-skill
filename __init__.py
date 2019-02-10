from mycroft import MycroftSkill, intent_file_handler


class Turtleleft(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('turtleleft.intent')
    def handle_turtleleft(self, message):
        self.speak_dialog('turtleleft')


def create_skill():
    return Turtleleft()

