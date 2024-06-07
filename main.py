from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from datetime import datetime

class Datas(BoxLayout):
    def __init__(self, datas, **kwargs):
        super(Datas, self).__init__(orientation="vertical", size_hint_y=None, **kwargs)
        self.bind(minimum_height=self.setter('height'))
        
        for data in datas:
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

class Parking(App):
    def build(self):
        screen = ScrollView()
        data = response_data()

        widgets = Datas(data)
        screen.add_widget(widgets)

        return screen

def response_data():
    do = datetime(2024, 6, 7, 19, 0, 24, 78915)
    after = datetime.now()
    time_diff = after - do
    return [["204aes13", str(time_diff), "Клиент"] for _ in range(100)]

if __name__ == '__main__':
    Parking().run()
