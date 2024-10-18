import ctypes
import winreg
import argparse


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
    parser = argparse.ArgumentParser()
    parser.add_argument("--reset", action="store_true", default=False)
    args = parser.parse_args()

    if args.reset:
        reset_cursor()
    else:
        set_cursor()
