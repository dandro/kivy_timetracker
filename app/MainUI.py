from kivy.uix.widget import Widget
from kivy.uix.image import Image
from app.MainController import MainController

WINDOW_SIZE = 400, 768
BUTTON_SPACING = 16


class MainUI(Widget):
    def __init__(self, **kwargs):
        super(MainUI, self).__init__(**kwargs)
        self.controller = MainController(window_size=WINDOW_SIZE)
        self.build_ui()

    @staticmethod
    def relative_top(relative_object):
        return relative_object.top - relative_object.height - BUTTON_SPACING

    def build_ui(self):
        # Set MainUI Attributes
        self.size = WINDOW_SIZE

        # UI Background
        self.add_widget(Image(source='./assets/PyStalkerBackground_v2.gif', size=WINDOW_SIZE))

        # Add Timer Label
        self.add_widget(self.controller.timer_label)

        # Add load day before button
        self.controller.submit_button.size = 39, 39
        self.controller.submit_button.background_normal = './assets/button_add_row.png'
        self.controller.submit_button.top = WINDOW_SIZE[1] - 96
        self.controller.submit_button.right = 383
        self.add_widget(self.controller.submit_button)

        # Add load day before button
        self.controller.button_previous_day.size = 40, 42
        self.controller.button_previous_day.background_normal = './assets/button_prev_day.png'
        self.controller.button_previous_day.top = self.relative_top(self.controller.submit_button)
        self.controller.button_previous_day.right = 383
        self.add_widget(self.controller.button_previous_day)

        # Add load day before button
        self.controller.button_next_day.size = 39, 42
        self.controller.button_next_day.background_normal = './assets/button_next_day.png'
        self.controller.button_next_day.top = self.relative_top(self.controller.button_previous_day)
        self.controller.button_next_day.right = 383
        self.add_widget(self.controller.button_next_day)

        # Add Button down
        self.controller.button_report.size = 39, 39
        self.controller.button_report.background_normal = './assets/button_record.png'
        self.controller.button_report.top = self.relative_top(self.controller.button_next_day)
        self.controller.button_report.right = 383
        self.add_widget(self.controller.button_report)

        # Add Time Row Date label
        self.controller.current_day_display.font_size = 16
        self.controller.current_day_display.size = 295, 38
        self.controller.current_day_display.top = WINDOW_SIZE[1] - 80
        self.controller.current_day_display.right = 222
        self.add_widget(self.controller.current_day_display)

        # Add Time Row Form Project Text
        self.controller.row_form.text_project.size = 295, 38
        self.controller.row_form.text_project.top = WINDOW_SIZE[1] - 120
        self.controller.row_form.text_project.right = 310
        self.controller.row_form.text_project.background_color = MainController.rgba2float(58, 58, 58)
        self.controller.row_form.text_project.font_size = 17
        self.controller.row_form.text_project.foreground_color = MainController.rgba2float(163, 152, 51)

        # Add Time Row Form Project Description
        self.controller.row_form.text_description.size = 295, 110
        self.controller.row_form.text_description.top = self.relative_top(self.controller.row_form.text_project)
        self.controller.row_form.text_description.right = 310
        self.controller.row_form.text_description.background_color = MainController.rgba2float(58, 58, 58)
        self.controller.row_form.text_description.font_size = 17
        self.controller.row_form.text_description.foreground_color = MainController.rgba2float(163, 152, 51)

        # Add Form widget
        self.add_widget(self.controller.row_form)

        # Add button up
        self.controller.button_up.size = 27, 16
        self.controller.button_up.background_normal = './assets/button_go_up.png'
        self.controller.button_up.top = self.relative_top(self.controller.row_form.text_description)
        self.controller.button_up.right = 267
        self.add_widget(self.controller.button_up)

        # Add Button down
        self.controller.button_down.size = 28, 16
        self.controller.button_down.background_normal = './assets/button_go_down.png'
        self.controller.button_down.top = self.controller.button_up.top
        self.controller.button_down.right = self.controller.button_up.right + self.controller.button_up.width + BUTTON_SPACING
        self.add_widget(self.controller.button_down)

        # Set UI Stack Layout
        self.controller.stack_layout.orientation = 'tb-lr'
        self.controller.stack_layout.size = (WINDOW_SIZE[0], 430)
        self.controller.stack_layout.padding = 10
        self.controller.stack_layout.spacing = 5
        self.add_widget(self.controller.stack_layout)
