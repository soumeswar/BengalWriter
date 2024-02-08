import pyautogui as pg
import pyperclip
import time
import keyboard

# Initialize a variable to keep track of the previous key pressed
prev_key = None

def on_key_press(event):
    global prev_key
    key = event.name
    
    time.sleep(0.1)  # Adjust the sleep duration as needed
    
    if prev_key == 'r' and key == 'i':  # Check for the sequence 'ri'
        handle_input_separated(bengali_ri)
        prev_key = None  # Reset prev_key after handling the combination
    elif prev_key == 'o' and key == 'i':
        handle_input_separated(bengali_oi)
    elif prev_key == 'o' and key == 'u':
        handle_input_separated(bengali_ou)
    elif prev_key == 'k' and key == 'o':
        handle_input_separated(bengali_ko)
    elif prev_key == 'k' and key == 'h':
        handle_input_separated(bengali_kh)
    elif prev_key == 'g' and key == 'h':
        handle_input_separated(bengali_gh)
    elif prev_key == 'g' and key == 'o':
        handle_input_separated(bengali_go)
    elif prev_key == 'g' and key == 'a':
        handle_input_separated(bengali_go+aakar)
    else:
        prev_key = key  # Update prev_key to the current key pressed

        if key == 'a':
            handle_input(bengali_a)
        elif key == 'A':
            handle_input(bengali_aa)
        elif key == 'i':
            handle_input(bengali_i)
        elif key == 'I':
            handle_input(bengali_ii)
        elif key == 'u':
            handle_input(bengali_u)
        elif key == 'U':
            handle_input(bengali_uu)
        elif key == 'r':
            handle_input(bengali_ri)  # Handle 'r' immediately
        elif key == 'e':
            handle_input(bengali_e)
        elif key == 'o':
            handle_input(bengali_o)








def handle_input_separated(unicode_char):
    pg.hotkey('backspace')
    pg.hotkey('backspace')
    pyperclip.copy(unicode_char)
    pg.hotkey('ctrl', 'v')
    pyperclip.copy('')

def handle_input(unicode_char):
    pg.hotkey('backspace')
    pyperclip.copy(unicode_char)
    pg.hotkey('ctrl', 'v')
    pyperclip.copy('')

# Define Bengali Unicode characters
# Your definitions...
bengali_a = '\u0985'
bengali_aa = '\u0986'
bengali_i = '\u0987'
bengali_ii = '\u0988'
bengali_u = '\u0989'
bengali_uu = '\u098A'
bengali_ri = '\u098B'
bengali_e = '\u098F'
bengali_oi = '\u0990'
bengali_o = '\u0993'
bengali_ou = '\u0994'
bengali_ko = '\u0995'
bengali_kh = '\u0996'
bengali_go = '\u0997'
bengali_gh = '\u0998'
bengali_ng = '\u0999'
bengali_ch = '\u099A'
bengali_chh = '\u099B'
bengali_jo = '\u099C'
bengali_jho = '\u099D'
bengali_nyo = '\u099E'
bengali_to = '\u099F'
bengali_tho = '\u09A0'
bengali_do = '\u09A1'
bengali_dho = '\u09A2'
bengali_no = '\u09A3'
bengali_po = '\u09A4'
bengali_pho = '\u09A5'
bengali_bo = '\u09A6'
bengali_bho = '\u09A7'
bengali_mo = '\u09A8'
bengali_yo = '\u09AF'
bengali_ro = '\u09B0'
bengali_lo = '\u09B2'
bengali_sh = '\u09B6'
bengali_sso = '\u09B7'
bengali_so = '\u09B8'
bengali_ho = '\u09B9'
bengali_rro = '\u09DC'
bengali_rroh = '\u09DD'
bengali_ryo = '\u09DF'
bengali_ttho = '\u09CE'
bengali_n = '\u0982'
bengali_h = '\u0983'
bengali_chandrabindu = '\u0981'

# Symbols
aakar = '\u09BE'

keyboard.on_press(on_key_press)
keyboard.wait('esc')
