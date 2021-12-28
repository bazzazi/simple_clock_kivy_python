from kivy.config import Config
Config.set("graphics", "resizable", 0)
from kivy.app import App
from kivy.core.window import Window
from kivy.lang.builder import Builder
from time import strftime
from kivy.clock import Clock

Window.size=(400,400)

class SimpleClock(App):
    def build(self):
        return Builder.load_file("design.kv")

    def update_time(self, *args):
        date = strftime("[font=ITCKRIST][size=50]%H:%M[/size]:%S\n %a, %B %d[/font]")
        self.root.ids.timer.text = date

    def on_start(self):
        Clock.schedule_interval(self.update_time, 0)

SimpleClock().run()