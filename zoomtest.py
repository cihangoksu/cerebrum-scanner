#####
# check this web page : https://groups.google.com/g/kivy-users/c/gD9_2E8hebI
from kivy.app import App
from kivy.lang import Builder

kv = """
BoxLayout:
    ScrollView:
        bar_width: 40
        scroll_type:['bars']
        BoxLayout:
            size_hint: None, None
            size: 1000, 1000
            Scatter:
                pos_hint: {'center_x': 1, 'center_y': 1}
                do_rotation: False
                Image:
                    source: 'TimerBackground.png'  # Select your own image... 
                    size: 500, 500
"""

class ImageViewerApp(App):
    def build(self):
        return Builder.load_string(kv)

ImageViewerApp().run()