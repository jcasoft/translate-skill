from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler


class Translate(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('translate.intent')
    def handle_translate(self, message):
        self.speak_dialog('translate')


def create_skill():
    return Translate()

