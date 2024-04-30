from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.color_definitions import colors
from kivymd.uix.screen import Screen
import openai

openai.api_key = 'sk-proj-rely1kMPjD244fHCFCuvT3BlbkFJd9LlI7tOXQxauvGsFx4o'  # Replace 'your-api-key' with your actual OpenAI API key

search_helper = """
MDTextField:
    hint_text: "Enter the Book Name"
    helper_text: "Or Search Through Camera"
    helper_text_mode: "on_focus"
    pos_hint: {'center_x': 0.42, 'center_y': 0.81}
    size_hint_x: 0.52
    size_hint_y: None
    height: "30dp"
"""

class Books(MDApp):

    def build(self):
        screen = Screen()

        label = MDLabel(text='Everything Books', pos_hint={'x': 0.35, 'y': 0.47}, theme_text_color='Custom',
                        text_color='#a4c639', font_style='H4')

        self.search = Builder.load_string(search_helper)
        btn_flat = MDRectangleFlatButton(text='DISCOVER', pos_hint={'x':0.7, 'y':0.79}, on_release=self.show_data)
        self.response_box = MDBoxLayout(orientation='vertical', pos_hint={'center_x': 0.5, 'center_y': 0.4})


        screen.add_widget(label)
        screen.add_widget(self.search)
        screen.add_widget(btn_flat)
        


        return screen
    def show_data(self, obj):
        user_input = self.search.text
        try:
            # Send the input to ChatGPT and get the response
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": user_input}
                ]
            )
            # Display the response in the response box
            response_text = response['choices'][0]['message']['content']
            self.response_box.add_widget(MDLabel(text=response_text))
        except Exception as e:
            self.response_box.add_widget(MDLabel(text=f"Error: {str(e)}"))

if __name__ == '__main__':
    Books().run()
