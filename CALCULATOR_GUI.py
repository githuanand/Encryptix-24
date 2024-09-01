from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.operators = ['+', '-', '*', '/']
        self.last_was_operator = False
        self.last_was_equal = False
        
        layout = BoxLayout(orientation='vertical')
        self.result = TextInput(font_size=32, readonly=True, halign='right', multiline=False)
        layout.add_widget(self.result)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for button_text in row:
                button = Button(text=button_text, pos_hint={'center_x': 0.5, 'center_y': 0.5})
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)

        return layout

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        if button_text == 'C':
            self.result.text = ''
            self.last_was_operator = False
            self.last_was_equal = False
        elif button_text == '=':
            if self.last_was_operator:
                return
            try:
                self.result.text = str(eval(self.result.text))
                self.last_was_equal = True
            except Exception as e:
                self.result.text = 'Error'
        else:
            if self.last_was_equal and button_text in self.operators:
                self.last_was_equal = False
                self.result.text = current + button_text
            elif button_text in self.operators:
                if self.last_was_operator:
                    return
                self.result.text += button_text
                self.last_was_operator = True
            else:
                self.result.text += button_text
                self.last_was_operator = False

if __name__ == '__main__':
    CalculatorApp().run()

