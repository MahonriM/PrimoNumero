import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid,self).__init__(**kwargs)
        self.cols=1
        self.inside=GridLayout()
        self.inside.cols=2
        self.inside.add_widget(Label(text="Ingresa un numero"))
        self.num=TextInput(multiline=False)
        self.inside.add_widget(self.num)
        self.prim=(Label(text=""))
        self.inside.add_widget(self.prim)
        self.add_widget(self.inside)

        self.submit=Button(text="Calcular",font_size=20)
        self.submit.bind(on_press=self.primo)
        self.add_widget(self.submit)
    def primo(self,instance):
        contador=0
        num1=int(self.num.text)
        for i in range(1, num1+1):
            if num1 % i == 0:
                contador+=1
        if contador==2:
            print("Es Primo")
            self.prim.text=("El numero es primo")
        else:
            print("No es primo")
            self.prim.text=("No es primo")
class MyApp(App):
    def build(self):
        return MyGrid()
if __name__=="__main__":
    MyApp().run()