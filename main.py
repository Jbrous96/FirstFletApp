import flet as ft
from flet import View, Page, AppBar, ElevatedButton, Text, Icon, FilledTonalButton
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment

def main(page: Page):
    page.title = "Flet Demo"
    # Routes sidebar #
    def change_Content(e):
        nav_dest= e.control.selected_index
        page.controls.clear()
# Routes for sidebar          |
    # Routes for sidebar      |
        # Routes for sidebar  V
        if nav_dest == 0:
            app_bar = ft.AppBar(
                leading=ft.Icon(ft.icons.PALETTE),
                leading_width=40,
                title=ft.Text("AppBar Example"),
                center_title=False,
                bgcolor=ft.colors.SURFACE_VARIANT,
                actions=[
                    ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
                    ft.IconButton(ft.icons.FILTER_3),
                    ft.PopupMenuButton(
                        items=[
                            ft.PopupMenuItem(text="Item 1"),
                            ft.PopupMenuItem(),  # divider
                            ft.PopupMenuItem(text="Checked item"),
                        ]
                    ),
                ]
            )
            page.add(app_bar)
            page.add(ft.Text(value="Home", size=30))
            page.add(ft.ElevatedButton(text='Home', on_click=lambda _: page.go('/Search')))
# Set alignment           |
    # Set alignment       |
        # Set alignment   v            
            page.vertical_alignment = MainAxisAlignment.START
            page.horizontal_alignment = CrossAxisAlignment.CENTER
            page.spacing = 26
# More Routes                |
    # More Routes            |
        # Routes for sidebar V               
        if nav_dest == 1:
            page.add(ft.AppBar(title=Text('Recent'), bgcolor='red'))
            page.add(ft.Text(value="Recent", size=30))
            page.add(ft.ElevatedButton(text='Home', on_click=lambda _: page.go('/Recent')))
# More Routes                |
    # More Routes            |
        # Routes for sidebar V   
        if nav_dest == 2:
            page.add(ft.AppBar(title=Text('Recent'), bgcolor='white'))
            page.add(ft.Text(value="Hom", size=30))
            page.add(ft.ElevatedButton(text='Home', on_click=lambda _: page.go('/')),
            vertical_alignment=MainAxisAlignment.START,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            spacing=26)
        page.update()
# Buttons for Sidebar                  |
# ABOVE crossreferences indexes below  |
            # ONLY creates buttons     V        

    # Buttons for Sidebar #
    page.drawer = ft.NavigationDrawer(bgcolor="white",
    controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label="Home",
                icon=ft.icons.DOOR_BACK_DOOR_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.DOOR_BACK_DOOR),
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.MAIL_OUTLINED),
                label="Recent",
                selected_icon=ft.icons.MAIL,
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.PHONE_OUTLINED),
                label="PHONE",
                selected_icon=ft.icons.PHONE,
            ),
        ],
    )
    page.drawer.on_change = change_Content
# Adds buttons to the page    |
# Above,we only created them  V
    
    def show_drawer(e):
        page.drawer.open = True
        page.drawer.update()

    page.add(ft.ElevatedButton("Show drawer", on_click=show_drawer))


    page.horizontal_alignment = page.vertical_alignment = "START"

    page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.ADD)
    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

    page.appbar = ft.AppBar(
        title=ft.Text("Bottom AppBar Demo"),
        center_title=True,
        bgcolor=ft.colors.GREEN_300,
        automatically_imply_leading=False,
    )
    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=ft.colors.BLUE,
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                FilledTonalButton(text='Profile', icon="person", on_click=lambda _: page.go('/store')),
                ft.Container(expand=True),
                ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE, on_click=show_drawer),
                ft.IconButton(icon=ft.icons.FAVORITE, icon_color=ft.colors.WHITE),
            ]
        ),
    )

    page.add(ft.Text("Body!"))

    # def route_change(e: RouteChangeEvent) -> None:
    #     page.views.clear()

    #     page.views.append(
    #         View(
    #             route='/',
    #             controls=[
    #                 AppBar(title=Text('Home'), bgcolor='blue'),
    #                 Text(value='Home', size=30),

    #                 FilledTonalButton(text='Go to store', icon="person", on_click=lambda _: page.go('/store')),
    #                 FilledTonalButton(text='Go to search', icon="search", on_click=lambda _: page.go('/search')),
    #                 FilledTonalButton(text="Recent Books", icon='local_library_outlined', on_click=lambda _: page.go('/Recent'))  # navigate to '/search' 
    #             ],
    #             vertical_alignment=MainAxisAlignment.START,
    #             horizontal_alignment=CrossAxisAlignment.START,
    #             padding = 5,
    #             spacing=26
    #         )
    #     ),
        

    #     #When in Store page
    #     if page.route == '/store':
    #         page.views.append(
    #             View(
    #             route='/store',
    #             controls=[
    #             AppBar(title=Text('Home'), bgcolor='red'),
    #             Text(value='Store', size=30),

    #             ElevatedButton(text='Home', on_click=lambda _: page.go('/'))
                
    #             ],
    #             vertical_alignment=MainAxisAlignment.START,
    #             horizontal_alignment=CrossAxisAlignment.START,
    #             spacing=26))
        
    #     if page.route == '/search':
    #         page.views.append(
    #             View(
    #             route='/search',
    #             controls=[
    #             AppBar(title=Text('Search'), bgcolor='yellow'),
    #             Text(value="Hom", size=30),
    #             ElevatedButton(text='Home', on_click=lambda _: page.go('/'))
    #             ],
                
    #             vertical_alignment=MainAxisAlignment.START,
    #             horizontal_alignment=CrossAxisAlignment.CENTER,
    #             spacing=26))
            
    #     if page.route == '/recent':
    #         page.views.append(
    #             View(
    #             route='/recent',
    #             controls=[
    #             AppBar(title=Text('Library mf'), bgcolor='white'),
    #             Text(value="Hom", size=30),
    #             ElevatedButton(text='Home', on_click=lambda _: page.go('/'))
    #             ],
                
    #             vertical_alignment=MainAxisAlignment.START,
    #             horizontal_alignment=CrossAxisAlignment.CENTER,
    #             spacing=26)
    #         )
    #     page.update()
    # def view_pop(e: ViewPopEvent) -> None:
    #     page.views.pop()
    #     top_view: View = page.views[-1]
    #     page.go(top_view.route)

    # page.on_route_change = route_change
    # page.on_view_pop = view_pop
    # page.go(page.route)

if __name__ == "__main__":
    ft.app(target=main)

    # def route_change(e: RouteChangeEvent) -> None:
    #     page.views.clear()

    #     page.views.append(
    #         View(
    #             route='/',
    #             controls=[
    #                 AppBar(title=Text('Home'), bgcolor='blue'),
    #                 Text(value='Home', size=30),

    #                 FilledTonalButton(text='Go to store', icon="person", on_click=lambda _: page.go('/store')),
    #                 FilledTonalButton(text='Go to search', icon="search", on_click=lambda _: page.go('/search')),
    #                 FilledTonalButton(text="Recent Books", icon='local_library_outlined', on_click=lambda _: page.go('/Recent'))  # navigate to '/search' 
    #             ],
    #             vertical_alignment=MainAxisAlignment.START,
    #             horizontal_alignment=CrossAxisAlignment.START,
    #             padding = 5,
    #             spacing=26
    #         )
    #     ),
        

    #     #When in Store page
    #     if page.route == '/store':
    #         page.views.append(
    #             View(
    #             route='/store',
    #             controls=[
    #             AppBar(title=Text('Home'), bgcolor='red'),
    #             Text(value='Store', size=30),

    #             ElevatedButton(text='Home', on_click=lambda _: page.go('/'))
                
    #             ],
    #             vertical_alignment=MainAxisAlignment.START,
    #             horizontal_alignment=CrossAxisAlignment.START,
    #             spacing=26))
        
    #     if page.route == '/search':
    #         page.views.append(
    #             View(
    #             route='/search',
    #             controls=[
    #             AppBar(title=Text('Search'), bgcolor='yellow'),
    #             Text(value="Hom", size=30),
    #             ElevatedButton(text='Home', on_click=lambda _: page.go('/'))
    #             ],
                
    #             vertical_alignment=MainAxisAlignment.START,
    #             horizontal_alignment=CrossAxisAlignment.CENTER,
    #             spacing=26))
            
    #     if page.route == '/recent':
    #         page.views.append(
    #             View(
    #             route='/recent',
    #             controls=[
    #             AppBar(title=Text('Library mf'), bgcolor='white'),
    #             Text(value="Hom", size=30),
    #             ElevatedButton(text='Home', on_click=lambda _: page.go('/'))
    #             ],
                
    #             vertical_alignment=MainAxisAlignment.START,
    #             horizontal_alignment=CrossAxisAlignment.CENTER,
    #             spacing=26)
    #         )
    #     page.update()
    # def view_pop(e: ViewPopEvent) -> None:
    #     page.views.pop()
    #     top_view: View = page.views[-1]
    #     page.go(top_view.route)

    # page.on_route_change = route_change
    # page.on_view_pop = view_pop
    # page.go(page.route)

if __name__ == "__main__":
    ft.app(target=main)
