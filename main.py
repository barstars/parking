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
    def __init__(self, **kwargs):
        super(Datas, self).__init__(orientation="vertical", size_hint_y=None, spacing=5, **kwargs)
        self.bind(minimum_height=self.setter('height'))
        self.data = self.response_data()
        self.create_widgets()

    def create_widgets(self):
        self.clear_widgets()

        index_data = 0
        for data in self.data:
            index_data += 1
            box_data = GridLayout(cols=4, height=40, size_hint_y=None)

            car_number = Label(text=data[0])
            box_data.add_widget(car_number)

            times = Label(text=data[1])
            box_data.add_widget(times)

            client_no_client = Label(text=data[2])
            box_data.add_widget(client_no_client)

            delate_button = Button(text=str(index_data))
            delate_button.bind(on_release=self.data_delate)
            box_data.add_widget(delate_button)

            self.add_widget(box_data)

        creat_data = GridLayout(cols=2, height=40, size_hint_y=None)

        self.input_text = TextInput(hint_text='123abc13', multiline=False)
        creat_data.add_widget(self.input_text)

        creat_but = Button(text="Добавить")
        creat_but.bind(on_release=self.data_create)
        creat_data.add_widget(creat_but)

        self.add_widget(creat_data)

        upload = Button(text="Обновить", height=40, size_hint_y=None)
        upload.bind(on_release=self.update_data)
        self.add_widget(upload)

    def update_data(self, instance):
        self.data = self.response_data()
        self.create_widgets()

    def response_data(self):
        url = 'https://muhammedeveloper1.pythonanywhere.com/parking/view_data'

        # Данные запроса
        data = {'1':'1'}

        # Отправка POST-запроса с данными
        response = requests.post(url, json=data)
        dic = response.json()
        data_keys = list(dic.keys())
        if data_keys[0] == 'null':
            return [['Нет','Данные','0']]
        res = []
        for el_key in data_keys:
            res.append([el_key, dic[el_key], str(datetime.now()-datetime.fromisoformat(dic[el_key]))])
        return res

    def data_create(self, instance):
        data = self.input_text.text
        if data != "":
            url = 'https://muhammedeveloper1.pythonanywhere.com/parking/create_data'

            # Данные запроса
            time = datetime.now().isoformat()
            data = {data:time}

            # Отправка POST-запроса с данными
            response = requests.post(url, json=data)
            if response.text == "Success":
                self.update_data("")
            else:
                self.input_text.text = ''
                self.input_text.hint_text = response.text

    def data_delate(self, data):
        ind = int(data.text)
        data = self.data[ind-1][0]
        url = 'https://muhammedeveloper1.pythonanywhere.com/parking/delate_data'
        response = requests.post(url, data=data)
        self.update_data("")

class Parking(App):
    def build(self):
        screen = ScrollView()
        self.widgets = Datas()
        screen.add_widget(self.widgets)

        return screen



if __name__ == '__main__':
    Parking().run()
