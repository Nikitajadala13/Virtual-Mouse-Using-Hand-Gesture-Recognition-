def detect_gesture(fingers):
    if fingers == [0, 1, 0, 0, 0]:
        return 'move'
    elif fingers == [0, 1, 1, 0, 0]:
        return 'left_click'
    elif fingers == [0, 0, 1, 0, 0]:
        return 'right_click'
    elif fingers == [0, 1, 1, 1, 0]:
        return 'double_click'
    elif fingers == [0, 1, 0, 1, 0]:
        return 'scroll_up'
    elif fingers == [0, 0, 1, 1, 0]:
        return 'scroll_down'
    elif fingers == [1, 1, 0, 0, 0]:
        return 'drag'
    elif fingers == [0, 1, 0, 0, 1]:
        return 'drop'
    elif fingers == [0, 0, 0, 0, 0]:
        return 'screenshot'
    else:
        return None