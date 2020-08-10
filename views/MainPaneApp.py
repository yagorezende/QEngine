from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from views.navigator.OptionsMenu import OptionsMenu
from kivy.core.window import Window

Window.fullscreen = 'auto'

class MainPaneWidget(Widget):
    pass

class QEngineApp(App):

    def build(self):
        root = MainPaneWidget()
        return root