import keyboard
import mouse
import threading
import time
import sys
import os

class AutoKeyPresser:
    def __init__(self, key_combo, interval=0.25):
        self.key_combo = key_combo
        self.interval = interval
        self._is_running = False
        self._thread = None

    def _press_loop(self):
        while self._is_running:
            for key in self.key_combo[:-1]:
                keyboard.press(key)
            keyboard.press_and_release(self.key_combo[-1])
            for key in reversed(self.key_combo[:-1]):
                keyboard.release(key)
            time.sleep(self.interval)

    def toggle(self):
        self._is_running = not self._is_running
        if self._is_running:
            print(f"[ON] Auto-press: {' + '.join(self.key_combo)}")
            self._thread = threading.Thread(target=self._press_loop)
            self._thread.start()
        else:
            print("[OFF] Auto-press stopped")

class AutoClicker:
    def __init__(self, interval=0.25):
        self.interval = interval
        self._is_running = False
        self._thread = None

    def _click_loop(self):
        while self._is_running:
            mouse.click('left')
            time.sleep(self.interval)

    def toggle(self):
        self._is_running = not self._is_running
        if self._is_running:
            print("[ON] Auto-clicking (left mouse)")
            self._thread = threading.Thread(target=self._click_loop)
            self._thread.start()
        else:
            print("[OFF] Auto-clicking stopped")

def auto_keyboard_assist():
    # Initialize modules
    auto_key_presser = AutoKeyPresser(['shift', 'e'], interval=0.25)
    auto_clicker = AutoClicker(interval=0.25)

    # Hotkey bindings
    keyboard.add_hotkey('f1', auto_key_presser.toggle)
    keyboard.add_hotkey('f2', auto_clicker.toggle)

    def exit_program():
        print("\n[EXIT] Program terminated.")
        sys.exit()

    keyboard.add_hotkey('esc', exit_program)

    print("=== Auto Input Module Ready ===")
    print("[F1] Toggle Shift+E auto input")
    print("[F2] Toggle left mouse auto click")
    print("[ESC] Exit the program")

    # Keep program alive
    keyboard.wait()

# Optional main selector
if __name__ == '__main__':
    auto_keyboard_assist()
