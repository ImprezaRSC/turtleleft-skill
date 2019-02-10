from mycroft import MycroftSkill, intent_file_handler
import subprocess

class Turtleleft(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('turtleleft.intent')
    def handle_turtleleft(self, message):
        self.speak_dialog('turtleleft')
        s = "rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, 1.8]'"
        subprocess.call([s],shell=True)

def create_skill():
    return Turtleleft()

