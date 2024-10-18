from pynput import mouse

def on_move(x, y):
    print('Pointer moved to {0}'.format((x, y)))

with mouse.Listener(on_move=on_move) as listener:
    listener.join()