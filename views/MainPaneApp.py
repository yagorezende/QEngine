from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from views.navigator.OptionsMenu import OptionsMenu
import kivy
kivy.require('1.0.7')

class MainPaneWidget(Widget):
    # TODO: Organize the grid with the CanvasPane on center

    def on_touch_down(self, touch):

        print(touch)

class MainPaneApp(App):

    def build(self):
        root = MainPaneWidget()
        # root.add_widget(box)

        return root