from kivy.app import App
from kivy.uix.progressbar import ProgressBar
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)


class BasicProgressBar(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        cx = Window.width / 2
        # ProgressBar(max=100, value=50): sets the maximum and current progress.
        # size_hint=(None, None) and pos=(...): manually place the progress bar in the window.
        self.pb = ProgressBar(max=100, value=50, size_hint=(None, None), width=300, height=30,pos=(cx - 150, Window.height - 100))
            #   max: Maximum allowed value (default 100).
            #   value: Current value of the progress bar.
            #   size_hint, width, height: manual sizing.
        # add_widget(pb): adds the progress bar to the Kivy window.
        self.add_widget(self.pb)


class ProgressBarApp(App):
    def build(self):
        return BasicProgressBar()


if __name__ == '__main__':
    ProgressBarApp().run()