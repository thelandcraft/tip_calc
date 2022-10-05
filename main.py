from kivy.lang import Builder

from kivymd.app import MDApp


class Test(MDApp):

    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(
            '''
MDScreen:

    MDBottomNavigation:
        #panel_color: "#eeeaea"
        selected_color_background: "green"
        text_color_active: "lightgrey"

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Калькулятор'
            icon: 'calculator'
            

            MDLabel:
                text: 'About me'
                halign: 'center'


        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'About Me'
            icon: 'pencil'

            MDLabel:
                text: 'Связь со мной : +7(999)999-99-99'
                halign: 'center'
'''
        )


Test().run()