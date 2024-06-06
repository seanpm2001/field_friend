configuration = {
    'wheels': {
        'version': 'double_wheels',
        'name': 'wheels',
        'left_back_can_address': 0x000,
        'left_front_can_address': 0x100,
        'right_back_can_address': 0x200,
        'right_front_can_address': 0x300,
        'is_left_reversed': False,
        'is_right_reversed': True,
    },
    'y_axis': {
        'version': 'y_axis_canopen',
        'name': 'yaxis',
        'can_address': 0x70,
        'max_speed': 500,
        'reference_speed': 30,
        'min_position': -0.125,
        'max_position': 0.125,
        'axis_offset': 0.13,
        'steps_per_m': 1_666_666.667,  # 4000steps/turn motor; 1/10 gear; 0.024m/u
        'end_r_pin': 12,
        'end_l_pin': 25,
        'motor_on_expander': False,
        'end_stops_on_expander': True,
        'reversed_direction': False,
    },
    'z_axis': {
        'version': 'z_axis_canopen',
        'name': 'zaxis',
        'can_address': 0x60,
        'max_speed': 500,
        'reference_speed': 30,
        'min_position': -0.197,
        'max_position': 0.0,
        'axis_offset': 0.0,
        'steps_per_m': 4_000_000,  # 4000steps/turn motor; 1/20 gear; 0.02m/u
        'end_t_pin': 22,
        'end_b_pin': 23,
        'motor_on_expander': False,
        'end_stops_on_expander': True,
        'reversed_direction': False,
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
        'pins': {'front_top': 35, 'front_bottom': 18, 'back': 21},
    },
    'status_control': {
        'name': 'status_control',
    },
    'bluetooth': {
        'name': 'uckerbot-u6',
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
    }

}
