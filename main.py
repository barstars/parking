from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

from datetime import datetime
import requests

class Datas(BoxLayout):
    def __init__(self, datas, **kwargs):
        super(Datas, self).__init__(orientation="vertical", size_hint_y=None, spacing=5, **kwargs)
        self.bind(minimum_height=self.setter('height'))
        self.data = datas
        self.create_widgets()

    def create_widgets(self):
        self.clear_widgets()

        for data in self.data:
            box_data = GridLayout(cols=4, height=40, size_hint_y=None)

            car_number = Label(text=data[0])
            box_data.add_widget(car_number)

            times = Label(text=data[1])
            box_data.add_widget(times)

            client_no_client = Label(text=data[2])
            box_data.add_widget(client_no_client)

            delate_button = Button(text="del")
            box_data.add_widget(delate_button)

            self.add_widget(box_data)

        creat_data = GridLayout(cols=2, height=40, size_hint_y=None)

        input_text = TextInput(multiline=False)
        creat_data.add_widget(input_text)

        creat_but = Button(text="Добавить")
        creat_data.add_widget(creat_but)

        self.add_widget(creat_data)

        upload = Button(text="Обновить", height=40, size_hint_y=None)
        upload.bind(on_release=self.update_data)
        self.add_widget(upload)

    def update_data(self, instance):
        self.data = response_data()
        self.create_widgets()

class Parking(App):
    def build(self):
        screen = ScrollView()
        data = response_data()

        self.widgets = Datas(data)
        screen.add_widget(self.widgets)

        return screen

def response_data():
    do = datetime(2024, 6, 7, 19, 0, 24, 78915)
    after = datetime.now()
    time_diff = after - do
    return [["204aes13", str(time_diff), "Клиент"] for _ in range(12)]

if __name__ == '__main__':
    Parking().run()
