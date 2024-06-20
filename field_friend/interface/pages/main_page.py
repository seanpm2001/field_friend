from typing import TYPE_CHECKING

import rosys
from nicegui import binding, ui

from field_friend.system import System

from ..components import camera_card, leaflet_map, operation, robot_scene


class main_page():

    def __init__(self, page_wrapper, system: 'System') -> None:
        self.system = system

        @ui.page('/')
        def page() -> None:
            page_wrapper()
            self.content(devmode=False)

    def content(self, devmode) -> None:
        page_height = '50vh' if devmode else 'calc(100vh - 170px)'
        ui.colors(primary='#6E93D6', secondary='#53B689', accent='#111B1E', positive='#53B689')
        with ui.row().style(f'height:{page_height}; width: calc(100vw - 2rem); flex-wrap: nowrap;'):
            with ui.column().classes('h-full w-1/2 p-2'):
                leaflet = leaflet_map(self.system, False)
                leaflet.m.classes('h-full w-full')
                if self.system.field_navigation.field is not None:
                    leaflet.active_field = self.system.field_navigation.field.id
                binding.bind_to(self.system.field_navigation, 'field', leaflet, 'active_field',
                                lambda f: f.id if f else None)
                with ui.row():
                    leaflet.buttons()
            with ui.row().classes('h-full ml-2 m-2').style('width: calc(100% - 1rem)'):
                operation(self.system)
                with ui.column().classes('h-full').style('width: calc(45% - 2rem); flex-wrap: nowrap;'):
                    camera_card(self.system.usb_camera_provider,
                                self.system.automator,
                                self.system.detector,
                                self.system.plant_locator,
                                self.system.field_friend,
                                self.system.puncher)
                    robot_scene(self.system, self.system.field_navigation.field)
                    with ui.row().style("margin: 1rem; width: calc(100% - 2rem);"):
                        with ui.column():
                            ui.button('emergency stop', on_click=lambda: self.system.field_friend.estop.set_soft_estop(True)).props('color=red') \
                                .classes('py-3 px-6 text-lg').bind_visibility_from(self.system.field_friend.estop, 'is_soft_estop_active', value=False)
                            ui.button('emergency reset', on_click=lambda: self.system.field_friend.estop.set_soft_estop(False)) \
                                .props('color=red-700 outline').classes('py-3 px-6 text-lg') \
                                .bind_visibility_from(self.system.field_friend.estop, 'is_soft_estop_active', value=True)
                        ui.space()
                        with ui.row():
                            rosys.automation.automation_controls(self.system.automator)
