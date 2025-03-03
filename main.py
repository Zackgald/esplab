import time
import my_oled
state = 0;
while True: 
  pass
  time.sleep(1);
  state = state+1;
  if (state = 0) {
  my_oled.print_text("test", 0,0)
  }
  if (state =1) {
     my_oled.print_text("something else", 3,3)
  }
