import logging

import rosys
from rosys.driving import Driver
from rosys.geometry import Point

from ..hardware import ChainAxis, FieldFriend


class Puncher:
    def __init__(self, field_friend: FieldFriend, driver: Driver) -> None:
        self.field_friend = field_friend
        self.driver = driver
        self.log = logging.getLogger('field_friend.puncher')

    async def try_home(self) -> bool:
        if self.field_friend.y_axis is None or self.field_friend.z_axis is None:
            rosys.notify('no y or z axis', 'negative')
            return False
        try:
            if self.field_friend.estop.active:
                rosys.notify('Estop active, relaese first', 'error')
                return False
            if not await self.field_friend.y_axis.try_reference():
                return False
            await rosys.sleep(0.2)
            if not await self.field_friend.z_axis.try_reference():
                return False
            return True
        except Exception as e:
            raise Exception('homing failed') from e
        finally:
            await self.field_friend.y_axis.stop()
            await self.field_friend.z_axis.stop()

    async def drive_to_punch(self, local_target_x: float) -> None:
        if self.field_friend.y_axis is None or self.field_friend.z_axis is None:
            rosys.notify('no y or z axis', 'negative')
            return
        self.log.info(f'Driving to punch at {local_target_x}...')
        if self.field_friend.version == 'ff3':
            work_x = self.field_friend.WORK_X
        elif self.field_friend.version == 'u2':
            work_x = self.field_friend.WORK_X_DRILL
        if local_target_x < work_x:
            self.log.info('Target is behind')
            raise Exception('Target is behind')
        axis_distance = local_target_x - work_x
        local_target = Point(x=axis_distance, y=0)
        world_target = self.driver.odometer.prediction.transform(local_target)
        await self.driver.drive_to(world_target)

    async def punch(self, y: float, depth: float) -> None:
        if self.field_friend.y_axis is None or self.field_friend.z_axis is None:
            rosys.notify('no y or z axis', 'negative')
            return
        try:
            if not self.field_friend.y_axis.is_referenced or not self.field_friend.z_axis.is_referenced:
                rosys.notify('axis are not referenced, homing!', type='info')
                success = await self.try_home()
                if not success:
                    rosys.notify('homing failed!', type='negative')
                    return
                await rosys.sleep(0.5)
            if not self.field_friend.y_axis.MIN_POSITION+0.05 <= y <= self.field_friend.y_axis.MAX_POSITION-0.05:
                rosys.notify('y position out of range', type='error')
                raise Exception('y position out of range')
            await self.field_friend.y_axis.move_to(y)
            await self.field_friend.z_axis.move_to(depth)
            await self.field_friend.z_axis.return_to_reference()
        except Exception as e:
            raise Exception('punching failed') from e
        finally:
            await self.field_friend.y_axis.stop()
            await self.field_friend.z_axis.stop()

    async def clear_view(self) -> None:
        if self.field_friend.y_axis is None:
            rosys.notify('no y axis', 'negative')
            return
        self.log.info('Clearing view...')
        if isinstance(self.field_friend.y_axis, ChainAxis):
            await self.field_friend.y_axis.return_to_reference()
            return
        y = self.field_friend.y_axis.MIN_POSITION if self.field_friend.y_axis.position <= 0 else self.field_friend.y_axis.MAX_POSITION
        await self.field_friend.y_axis.move_to(y)
        await self.field_friend.y_axis.stop()

    async def drive_and_punch(self, x: float, y: float, depth: float = 0.05) -> None:
        if self.field_friend.y_axis is None or self.field_friend.z_axis is None:
            rosys.notify('no y or z axis', 'negative')
            return
        try:
            await self.drive_to_punch(x)
            await self.punch(y, depth)
            # await self.clear_view()
        except Exception as e:
            raise Exception('drive and punch failed') from e

    async def chop(self) -> None:
        if not isinstance(self.field_friend.y_axis, ChainAxis):
            raise Exception('chop is only available for chain axis')
        if self.field_friend.y_axis.position <= 0:
            await self.field_friend.y_axis.move_dw_to_l_ref()
        else:
            await self.field_friend.y_axis.move_dw_to_r_ref()
        await self.field_friend.y_axis.stop()
