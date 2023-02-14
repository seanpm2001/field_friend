import rosys
from nicegui.events import KeyEventArguments
from rosys import background_tasks
from rosys.automation import Automator
from rosys.driving import Steerer
from rosys.hardware import Wheels

from ..automations import Puncher
from ..hardware import FieldFriend, YAxis, ZAxis
from ..old_hardware import Robot


class KeyControls(rosys.driving.keyboard_control):

    def __init__(self, field_friend: FieldFriend, steerer: Steerer, automator: Automator, puncher: Puncher) -> None:
        super().__init__(steerer)
        self.field_friend = field_friend
        self.wheels = field_friend.wheels
        self.y_axis = field_friend.y_axis
        self.z_axis = field_friend.z_axis
        self.automator = automator
        self.puncher = puncher

    def handle_keys(self, e: KeyEventArguments) -> None:
        super().handle_keys(e)

        if e.modifiers.shift and e.action.keydown:
            if e.key == '!':
                async def try_axis_home():
                    await self.puncher.home()
                self.automator.start(try_axis_home())

        if e.modifiers.shift and e.action.keydown:
            if e.key == 'W':
                background_tasks.create(self.z_axis.move_to(self.z_axis.MAX_Z))
            if e.key == 'S':
                background_tasks.create(self.z_axis.move_to(self.z_axis.MIN_Z))
        if e.modifiers.shift and e.action.keyup:
            if e.key.name in 'WS':
                background_tasks.create(self.z_axis.stop())

        if e.modifiers.shift and e.action.keydown:
            if e.key == 'A':
                background_tasks.create(self.y_axis.move_to(self.y_axis.MAX_Y))
            if e.key == 'D':
                background_tasks.create(self.y_axis.move_to(self.y_axis.MIN_Y))
        if e.modifiers.shift and e.action.keyup:
            if e.key.name in 'AD':
                background_tasks.create(self.y_axis.stop())
                rosys.notify('y axis stopped')

        if e.key == ' ' and e.action.keydown:
            background_tasks.create(self.field_friend.stop())
