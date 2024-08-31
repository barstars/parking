from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

from kivmob import KivMob, TestIds, RewardedListenerInterface

from datetime import datetime
import requests

class Datas(BoxLayout):
    def __init__(self, **kwargs):
        super(Datas, self).__init__(orientation="vertical", size_hint_y=None, spacing=5, **kwargs)
        self.bind(minimum_height=self.setter('height'))
        self.response_data()

    def create_widgets(self, datas):
        self.clear_widgets()

        index_data = 0
        for data in datas:
            index_data += 1
            box_data = GridLayout(cols=4, height=90, size_hint_y=None)

            car_number = Label(text=data[0])
            box_data.add_widget(car_number)

            times = Label(text=data[1])
            box_data.add_widget(times)

            delate_button = Button(text=str(index_data))
            delate_button.bind(on_release=self.data_delate)
            box_data.add_widget(delate_button)

            self.add_widget(box_data)

        creat_data = GridLayout(cols=2, height=90, size_hint_y=None)

        self.input_text = TextInput(hint_text='123abc13', multiline=False)
        creat_data.add_widget(self.input_text)

        creat_but = Button(text="Добавить")
        creat_but.bind(on_release=self.data_create)
        creat_data.add_widget(creat_but)

        self.add_widget(creat_data)

        upload = Button(text="Обновить", height=90, size_hint_y=None)
        upload.bind(on_release=self.update_data_btn)
        self.add_widget(upload)

    def update_data_btn(self, instance):
        self.response_data()

    def update_data(self, response):
        dic = response.json()
        data_keys = list(dic.keys())
        if data_keys[0] == 'null':
            res = [['Нет','Данные']]
        else:
            res = []
            for el_key in data_keys:
                a = dic[el_key]
                dic_key = list(a.keys())[0]
                time = (dic[el_key][dic_key])
                string = time[:time.find(".")]
                res.append([dic_key,string])

        self.data = res
        self.create_widgets(res)
        

    def response_data(self):
        url = 'https://muhammedeveloper1.pythonanywhere.com/parking/view_data'
        # url = 'http://192.168.1.7:5000/parking/view_data'

        # Данные запроса
        data = {'1':'1'}

        # Отправка POST-запроса с данными
        response = requests.post(url, json=data)
        self.update_data(response)

    def data_create(self, instance):
        text = self.input_text.text
        if text != "":
            url = 'https://muhammedeveloper1.pythonanywhere.com/parking/create_data'
            # url = 'http://192.168.1.7:5000/parking/create_data'

            # Данные запроса
            data = {"data":text}

            # Отправка POST-запроса с данными
            response = requests.post(url, json=data)
            self.update_data(response)

    def data_delate(self, data):
        ind = int(data.text)
        if self.data[ind-1][1] != "Данные":
            data = {"del":self.data[ind-1][0]}
            print(data)
            url = 'https://muhammedeveloper1.pythonanywhere.com/parking/delete_data'
            # url = 'http://192.168.1.7:5000/parking/delete_data'
            response = requests.post(url, json=data)
            self.update_data(response)

class Parking(App):
    def build(self):
        self.ads = KivMob(TestIds.APP)
        self.ads.new_banner(TestIds.BANNER,False)
        self.ads.request_banner()
        self.ads.show_banner()
        screen = ScrollView()
        self.widgets = Datas()
        screen.add_widget(self.widgets)

        return screen



if __name__ == '__main__':
    Parking().run()
