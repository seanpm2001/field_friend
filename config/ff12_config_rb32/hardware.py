configuration = {
    'wheels': {
        'version': 'double_wheels',
        'name': 'wheels',
        'left_back_can_address': 0x000,
        'left_front_can_address': 0x100,
        'right_back_can_address': 0x200,
        'right_front_can_address': 0x300,
        'is_left_reversed': True,
        'is_right_reversed': False,
    },
    'y_axis': {
        'version': 'y_axis_canopen',
        'name': 'yaxis',
        'can_address': 0x60,
        'max_speed': 2000,
        'reference_speed': 40,
        'min_position': -0.075,
        'max_position': 0.065,
        'axis_offset': 0.08,
        'steps_per_m': 1_481_481.48,  # 4000steps/turn motor; 1/20 gear; 0.054m/u
        'end_r_pin': 19,
        'end_l_pin': 21,
        'motor_on_expander': False,
        'end_stops_on_expander': True,
        'reversed_direction': False,
    },
    'z_axis': {
        'version': 'tornado',
        'name': 'tornado',
        'min_position': -0.085,
        'z_can_address': 0x500,
        'turn_can_address': 0x400,
        'm_per_tick': 0.025/12.52,
        'end_top_pin': 32,
        'end_bottom_pin': 5,
        'ref_motor_pin': 35,
        'ref_gear_pin': 18,
        'ref_knife_stop_pin': 4,
        'ref_knife_ground_pin': 33,
        'motors_on_expander': False,
        'end_stops_on_expander': True,
        'is_z_reversed': True,
        'is_turn_reversed': True,
        'speed_limit': 1.5,
        'turn_speed_limit': 1.5,
        'current_limit': 30,
        'z_reference_speed': 0.0075,
        'turn_reference_speed': 0.25,
    },
    'flashlight': {
        'version': 'flashlight_pwm_v2',
        'name': 'flashlight',
        'on_expander': False,
        'front_pin': 5,
        'back_pin': 4,
    },
    'estop': {
        'name': 'estop',
        'pins': {'1': 34, '2': 35},
    },
    'bms': {
        'name': 'bms',
        'on_expander': True,
        'rx_pin': 26,
        'tx_pin': 27,
        'baud': 9600,
        'num': 2,
    },
    'battery_control': {
        'name': 'battery_control',
        'on_expander': True,
        'reset_pin': 15,
        'status_pin': 13,
    },
    'bumper': {
        'name': 'bumper',
        'on_expander': True,
        'pins': {'front_top': 22, 'front_bottom': 12, 'back': 25},
    },
    'status_control': {
        'name': 'status_control',
    },
    'bluetooth': {
        'name': 'fieldfriend-ff12',
    },
    'serial': {
        'name': 'serial',
        'rx_pin': 26,
        'tx_pin': 27,
        'baud': 115200,
        'num': 1,
    },
    'expander': {
        'name': 'p0',
        'boot': 25,
        'enable': 14,
    },
    'can': {
        'name': 'can',
        'on_expander': False,
        'rx_pin': 32,
        'tx_pin': 33,
        'baud': 1_000_000,
    },
}
