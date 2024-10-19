import ctypes
import winreg


def reload():
    SPI_SETCURSORS = 0x0057
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETCURSORS, 0, 0, 0)


def set_cursor():
    # Open the registry key
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Control Panel\Cursors",
        0,
        winreg.KEY_ALL_ACCESS,
    )

    # Set the value
    winreg.SetValueEx(key, "Arrow", 0, winreg.REG_SZ, r"D:\src\customcursor\py\33.cur")

    # Close the key
    winreg.CloseKey(key)

    reload()


def reset_cursor():
    # Open the registry key
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Control Panel\Cursors",
        0,
        winreg.KEY_ALL_ACCESS,
    )

    # Set the value
    winreg.SetValueEx(
        key, "Arrow", 0, winreg.REG_SZ, r"C:\Windows\Cursors\aero_arrow.cur"
    )

    # Close the key
    winreg.CloseKey(key)

    reload()


if __name__ == "__main__":
    from pynput import mouse

    def on_move(x, y):
        # -2874, 363
        print("Pointer moved to {0}".format((x, y)))
        if -128 > x > -2874 + 128 or 60 < x:
            set_cursor()
        else:
            reset_cursor()

    with mouse.Listener(on_move=on_move) as listener:
        listener.join()
