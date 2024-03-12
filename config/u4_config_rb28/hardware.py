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
        'version': 'y_axis_tornado',
        'name': 'y_axis',
        'max_speed': 60_000,
        'min_position': -0.068,
        'max_position': 0.068,
        'axis_offset': 0.075,
        'steps_per_m': 599251,
        'step_pin': 5,
        'dir_pin': 4,
        'alarm_pin': 13,
        'end_r_pin': 19,
        'end_l_pin': 21,
        'motor_on_expander': False,
        'end_stops_on_expander': True,
    },
    'z_axis': {
        'version': 'tornado',
        'name': 'tornado',
        'min_position': -0.068,
        'z_can_address': 0x500,
        'turn_can_address': 0x400,
        'm_per_tick': 0.025/12.52,
        'end_top_pin': 32,
        'end_bottom_pin': 5,
        'ref_motor_pin': 33,
        'ref_gear_pin': 4,
        'ref_t_pin': 35,
        'ref_b_pin': 18,
        'motors_on_expander': False,
        'end_stops_on_expander': True,
        'is_z_reversed': True,
        'is_turn_reversed': True,
        'speed_limit': 1.0,
        'turn_speed_limit': 1.0,
        'current_limit': 30,
    },
    'flashlight': {
        'version': 'flashlight_pwm',
        'name': 'flashlight',
        'pin': 2,
        'on_expander': True,
        'rated_voltage': 23.0,
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
    }
}
config = {'wheels':
          {'version': 'double_wheels',
           'name': 'wheels',
           'left_back_can_address': 0,
           'left_front_can_address': 256,
           'right_back_can_address': 512,
           'right_front_can_address': 768,
           'is_left_reversed': False,
           'is_right_reversed': True},
          'y_axis':
          {'version': 'y_axis_tornado',
           'name': 'y_axis',
              'max_speed': 60000,
           'min_position': -0.068,
           'max_position': 0.068,
           'axis_offset': 0.075,
                      'steps_per_m': 599251,
           'step_pin': 5,
           'dir_pin': 4,
           'alarm_pin': 13,
           'end_r_pin': 19,
           'end_l_pin': 21,
           'motor_on_expander': False,
           'end_stops_on_expander': True},
          'z_axis': {'version': 'tornado',
                     'name': 'tornado',
                     'min_position': -0.068,
                     'z_can_address': 1280,
                     'turn_can_address': 1024,
                     'm_per_tick': 0.0019968051118210866,
                                'end_top_pin': 32,
                     'end_bottom_pin': 5,
                     'ref_motor_pin': 33,
                     'ref_gear_pin': 4,
                     'ref_t_pin': 35,
                     'ref_b_pin': 18,
                     'motors_on_expander': False,
                     'end_stops_on_expander': True,
                     'is_z_reversed': True,
                     'is_turn_reversed': True,
                     'speed_limit': 1.0,
                     'turn_speed_limit': 1.0,
                     'current_limit': 30},
          'flashlight': {'version': 'flashlight_pwm',
                         'name': 'flashlight',
                         'pin': 2,
                         'on_expander': True,
                         'rated_voltage': 23.0},
          'estop': {'name': 'estop',
                    'pins': {'1': 34, '2': 35}},
          'bms': {'name': 'bms',
                  'on_expander': True,
                  'rx_pin': 26,
                  'tx_pin': 27,
                  'baud': 9600,
                  'num': 2},
          'battery_control': {'name': 'battery_control',
                              'on_expander': True,
                              'reset_pin': 15,
                              'status_pin': 13},
          'bumper': {'name': 'bumper',
                     'on_expander': True,
                     'pins': {'front_top': 22, 'front_bottom': 12, 'back': 25}},
          'status_control': {'name': 'status_control'}}
