from kivy.app import App
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.progressbar import ProgressBar
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.clearcolor = (0.98, 0.98, 1, 1)


class ProgressButton(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pb = ProgressBar(max=100, value=0, size_hint=(1, None), height=30)
        # Popup(...): displays the progress bar in a separate window.
        self.popup = Popup(title='Download', content=self.pb, size_hint=(0.5, 0.2))
        self.popup.bind(on_open=self.start_progress)
        # Button(...): triggers the popup containing the progress bar.
        btn = Button(text='Start Download', size_hint=(None,None), width=150, height=40,pos=(Window.width/2 - 75, Window.height - 100), on_release=self.show_popup)
        self.add_widget(btn)

    def show_popup(self, instance):
        self.pb.value = 0
        self.popup.open()

    def start_progress(self, instance):
        # Clock.schedule_interval(...): repeatedly calls update_progress to increment the bar.
        Clock.schedule_interval(self.update_progress, 1/25)

    # update_progress(...): stops updating when value reaches 100.
    def update_progress(self, dt):
        if self.pb.value >= 100:
            return False
        self.pb.value += 1


class ProgressBarApp(App):
    def build(self):
        return ProgressButton()


if __name__ == '__main__':
    ProgressBarApp().run()