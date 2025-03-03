import time
import my_oled

state = 0
while True:
    time.sleep(1)
    state = state + 1
    if state == 0:
        my_oled.print_text("test", 0, 0)
    elif state == 1:
        my_oled.print_text("something else", 3, 3)
    elif state == 2:
        my_oled.fill(0)
        my_oled.oled.line(0, 0, 10, 10, 1)
        my_oled.show()
    elif state == 3:
        my_oled.fill(0)
        my_oled.graphics.fill_rect(0, 0, 10, 10, 1)
        my_oled.show()
    if state > 3:
        state = 0  # Reset state after 3
