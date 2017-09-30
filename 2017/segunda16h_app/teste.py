from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.camera import Camera

tela_avatar = Screen()
tela_avatar.add_widget(Label(text='Olá mundo'))
cam = Camera()
#cam.resolution = (320, 240)

#tela_avatar.add_widget(cam)

telas = ScreenManager()
telas.add_widget( tela_avatar )

class VDapp(App):

    def build(self):
        return telas


if __name__ == '__main__':
    VDapp().run()