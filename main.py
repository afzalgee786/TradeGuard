from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class TradeGuardApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        title = Label(text='TradeGuard', font_size='40sp', bold=True)
        sub = Label(text='Trading Safety App\nAPK Ready', font_size='20sp')
        btn = Button(text='START TRADING SAFE', size_hint=(1, 0.25))
        layout.add_widget(title)
        layout.add_widget(sub)
        layout.add_widget(btn)
        return layout

TradeGuardApp().run()
