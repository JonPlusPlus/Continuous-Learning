from kivy.app import App
from kivy.clock import Clock
from kivy.uix.progressbar import ProgressBar
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.clearcolor = (1, 1, 0.95, 1)


class AutoProgress(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        cx = Window.width / 2
        # No popup needed; the progress bar is displayed directly in the main window.
        self.pb = ProgressBar(max=100, value=0, size_hint=(None,None), width=300, height=30,pos=(cx - 150, Window.height - 120))
        self.add_widget(self.pb)
        # Clock.schedule_interval(...): updates the progress bar at regular intervals.
        Clock.schedule_interval(self.update_progress, 1/20)

    # update_progress(...): increments value until it reaches the maximum.
    def update_progress(self, dt):
        if self.pb.value < 100:
            self.pb.value += 1


class ProgressBarApp(App):
    def build(self):
        return AutoProgress()


if __name__ == '__main__':
    ProgressBarApp().run()