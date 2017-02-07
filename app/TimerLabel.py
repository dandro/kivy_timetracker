from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.clock import Clock
import time

TIME_FORMAT = '%Y-%m-%d %H:%M:%S'


class TimerLabel(Widget):
    def __init__(self, parent_size, **kwargs):
        super(TimerLabel, self).__init__(**kwargs)

        # schedule clock
        Clock.schedule_interval(self.update_time, 1)

        # init attributes
        self.parent_size = parent_size
        self.size = (300, 50)
        self.relative_top = self.parent_size[1] - self.height - 35
        self.pos = (32, self.relative_top)

        # Create and Add time_label
        self.time_label = Label(text=self.display_time(), pos=self.pos, size=self.size, font_size=20, markup=True)
        self.add_widget(self.time_label)

    @staticmethod
    def display_time():
        # return "[color=dfe9a2]" + str(datetime.today()) + "[/color]"
        return "[color=b2b2b2]" + time.strftime(TIME_FORMAT) + "[/color]"

    def update_time(self, dt):
        self.time_label.text = self.display_time()
        self.time_label.time = time.strftime(TIME_FORMAT)
