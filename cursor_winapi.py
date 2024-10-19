import win32api
import win32con
import win32gui


def get_monitor_info():
    """
    Gets information about all connected monitors.

    Returns:
      A list of dictionaries, where each dictionary represents a monitor and
      contains the following keys:
        - 'index': The index of the monitor.
        - 'left': The x-coordinate of the left edge of the monitor.
        - 'top': The y-coordinate of the top edge of the monitor.
        - 'width': The width of the monitor.
        - 'height': The height of the monitor.
    """
    monitors = []
    index = 0

    def callback(hMonitor, hdcMonitor, lprcMonitor):
        nonlocal index
        r = lprcMonitor
        left, top, right, bottom = lprcMonitor
        monitors.append(
            {
                "index": index,
                "left": left,
                "top": top,
                "width": right - left,
                "height": bottom - top,
            }
        )
        index += 1

    r = win32api.EnumDisplayMonitors(None, None)
    for i in r:
        print(i)
        callback(*i)
    return monitors


def get_mouse_pos_relative_to_screens():
    """
    Gets the mouse position relative to each screen.

    Returns:
      A list of tuples, where each tuple represents the mouse position relative to
      a screen and contains the following values:
        - x: The x-coordinate of the mouse relative to the screen.
        - y: The y-coordinate of the mouse relative to the screen.
    """
    monitors = get_monitor_info()
    cursor_x, cursor_y = win32api.GetCursorPos()
    positions = []
    for monitor in monitors:
        x = cursor_x - monitor["left"]
        y = cursor_y - monitor["top"]
        positions.append((x, y))
    return positions


if __name__ == "__main__":
    positions = get_mouse_pos_relative_to_screens()
    for i, pos in enumerate(positions):
        print(f"Screen {i+1}: {pos}")
