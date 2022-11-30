#pip install kivy
#pip install kivymd
#pip install https://github.com/kivymd/KivyMD/archive/3274d62.zip

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.uix.button import MDRoundFlatIconButton

from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout

from kivymd.icon_definitions import md_icons
from kivymd.font_definitions import fonts

from kivymd.uix.menu import MDDropdownMenu
from kivy.clock import Clock
import webbrowser


KV = '''
#https://stackoverflow.com/questions/65698145/kivymd-tab-name-containing-icons-and-text
# this import will prevent disappear tabs through some clicks on them)))
#:import md_icons kivymd.icon_definitions.md_icons
#:import fonts kivymd.font_definitions.fonts


# Menu item in the DrawerList list.
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color


<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "data/logo/kivy-icon-256.png"

    MDLabel:
        text: "Калькулятор чаевых"
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    MDLabel:
        text: "Автор Бурьяк Данил"
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]

 


    ScrollView:

        DrawerList:
            id: md_list



Screen:

    MDNavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Калькулятор чаевых"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                        md_bg_color: 0, 0, 0, 1
                        right_action_items: [["language-python",lambda x: nav_drawer.set_state("shutdown")]]
                    MDTabs:
                        id: tabs
                        on_tab_switch: app.on_tab_switch(*args)
                        height:"48dp"
                        tab_indicator_anim: False
                        background_color: 0.1, 0.1, 0.1, 1

                        Tab:
                            id: tab1
                            name: 'tab1'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['calculator']}[/size][/font] Калькулятор"
                        
                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"   
                                
                                BoxLayout:
                                    orientation: 'horizontal'                               
                                    
                                    MDIconButton:
                                        icon: "account-cash"
                                        
                                    MDTextField:
                                        hint_text: "Счет чека"
                                        id:loan
                                        color_mode:'custom'
                                        line_color_focus: 0,0,0,1
                                        text_color: 0,0,0,1
                                        current_hint_text_color: 0,0,0,1
                                
                                BoxLayout:
                                    orientation: 'horizontal'                         
                                    
                                    MDIconButton:                      
                                        icon: "percent"
                                        
                                    MDTextField:
                                        hint_text: "Процент чаевых,%"
                                        id: months
                                        color_mode:'custom'
                                        line_color_focus: 0,0,0,1
                                        text_color: 0,0,0,1
                                        current_hint_text_color: 0,0,0,1

                                BoxLayout:
                                    orientation: 'horizontal'                                
                                    
                                    MDIconButton:
                                        icon: "account-group"
        
                                    MDTextField:
                                        hint_text: "Разделить счёт"
                                        id: interest
                                        color_mode:'custom'
                                        line_color_focus: 0,0,0,1
                                        text_color: 0,0,0,1
                                        current_hint_text_color: 0,0,0,1

                                                               
                                

                                MDSeparator:
                                    height: "1dp"



                                BoxLayout:
                                    orientation: 'horizontal'
                                    
                                    AnchorLayout:
                                        anchor_x: 'center'

                                        MDIconButton:
                                            icon: "cash"
                                            text: "vi4islenie"
                                            theme_text_color: "Custom"
                                            text_color: 1, 1, 1, 1
                                            line_color: 0, 0, 0, 1
                                            icon_color: 1, 0, 0, 1
                                            md_bg_color: 0.1, 0.1, 0.1, 1
                                            adaptive_width: True
                                            on_release: app.calc_table(*args)

                        Tab:
                            id: tab2
                            name: 'tab2'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['table-large']}[/size][/font] Список"

                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp" 
                                
                                ScrollView:
                                
                                    MDList:
                                        id: table_list              

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer

<ItemTable>:
    size_hint_y: None
    height: "42dp"

    canvas:
        Color:
            rgba: root.color
        Rectangle:
            size: self.size
            pos: self.pos

    
    MDLabel:
        text: root.payment
        halign: "center"
    MDLabel:
        text: root.interest
        halign: "center"
    MDLabel:
        text: root.principal
        halign: "center"
    MDLabel:
        text: root.rubles
        halign: "center"
    MDLabel:
        text: root.debt
        halign: "center"
        
'''


class ContentNavigationDrawer(BoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))

    def open(self,*args):
        webbrowser.open_new_tab("https://telegra.ph/Esli-nashli-oshibku-11-30")


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Вызывается при нажатии на пункт меню."""

        # Установка цвета значка и текста для пункта меню.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class Tab(MDFloatLayout, MDTabsBase):
    pass

class ItemTable(BoxLayout):
    num = StringProperty()
    date = StringProperty()
    payment = StringProperty()
    interest = StringProperty()
    principal = StringProperty()
    debt = StringProperty()
    color = ListProperty()
    rubles = StringProperty()

class CalculateTip(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        # https://kivymd.readthedocs.io/en/latest/components/menu/?highlight=MDDropDownItem#center-position
        #menu_items = [{"icon": "git", "text": f"Item {i}"} for i in range(5)]
        

   

    def build(self):
        self.theme_cls.theme_style = "Light"  # "Dark"  # "Light"
        #return Builder.load_string(KV)
        return self.screen

    


    def on_start(self):
        
        self.screen.ids.loan.text = "5000"
        self.screen.ids.months.text = "12"
        self.screen.ids.interest.text = "2"
        


        icons_item = {
            "book":"О приложении",
            "github":"Код на GitHub",
            "alert":"Нашли ошибку"   
        }
        
        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )

        
        # for name_tab in list(md_icons.keys())[15:30]:
        #     self.root.ids.tabs.add_widget(Tab(icon=name_tab, title=name_tab)
        #     )


        # for icon_name, name_tab in icons_item_tab.items():
        #     self.root.ids.tabs.add_widget(
        #          Tab(
        #              text=f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons[icon_name]}[/size][/font] {name_tab}"
        #             )
        #         )


        #отвечает за перелистывание tab
    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
        ): 
        print("click" + tab_text)
      
    def calc_table(self, *args):
        print("button1 pressed")
        
        loan = self.screen.ids.loan.text
        months = self.screen.ids.months.text
        interest = self.screen.ids.interest.text
        
        print(loan+" "+months+" "+interest+" ")
        # преобразовать в объект date, float и так далее
        
        loan = float(loan)
        months = int(months)
        interest = float(interest)

       
        percent = months/100
        full_loan = (loan+(loan*percent))/interest
        rublesl = loan*percent
        
        print(full_loan)

        

        
        self.screen.ids.table_list.add_widget(
            ItemTable(
                color=(0.2, 0.2, 0.2, 0.5),
                               
                payment="Чек",
                interest="Люди",
                principal="Чаевые,%",
                rubles ="Чаевые,руб." ,
                debt="Итог",
            )
        )

        
        for i in range(0, 1):
            row_color = (1, 1, 1, 1)
            if (i % 2 != 0):
                row_color = (0.2, 0.2, 0.2, 0.1)
        

            self.screen.ids.table_list.add_widget(
                ItemTable(
                    color=row_color,  # (0, 0, 0, 1),
                              
                    payment=str(round(loan, 2)),
                    interest=str(round(interest, 2)),
                    principal=str(round(months , 2 ))+"%",
                    rubles=str(round(rublesl,2)),
                    debt=str(round(full_loan, 2)),
                )
            )

            # d = datetime.datetime.today()
            # print(next_month_date(d))
            # start_date = start_date + datetime.timedelta(days=30)

        

        pass
        
CalculateTip().run()