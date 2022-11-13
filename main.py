#!/usr/bin/env python3
import rosys
from nicegui import ui

import hardware
import interface
import log

log = log.configure()


try:
    robot = hardware.RobotHardware()
except:
    robot = hardware.RobotSimulation()
steerer = rosys.driving.Steerer(robot, speed_scaling=0.5)

odometer = rosys.driving.Odometer(robot)
driver = rosys.driving.Driver(robot, odometer)
driver.parameters.linear_speed_limit = 0.5
driver.parameters.angular_speed_limit = 0.5
automator = rosys.automation.Automator(robot, steerer)


@ui.page('/', shared=True)
async def index():
    ui.colors(primary='#6E93D6', secondary='#53B689', accent='#111B1E', positive='#53B689')
    interface.navigation_bar(robot)

    with ui.row().classes('items-stretch justify-items-stretch').style('flex-wrap:nowrap'):
        interface.operation(steerer, automator, odometer)
    with ui.card():
        if robot.is_real:
            robot.robot_brain.developer_ui()
            robot.robot_brain.communication.debug_ui()
            rosys.on_startup(robot.robot_brain.lizard_firmware.ensure_lizard_version)
        else:
            rosys.simulation_ui()

ui.run(title='Field Friend', port=80 if robot.is_real else 8080)
