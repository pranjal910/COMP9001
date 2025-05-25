import time

# === Color Utilities === #
def color(text, fg=None, style=None):
    codes = {
        'reset': "\033[0m",
        'bold': "\033[1m",
        'underline': "\033[4m",
        'red': "\033[31m",
        'green': "\033[32m",
        'yellow': "\033[33m",
        'blue': "\033[34m",
        'magenta': "\033[35m",
        'cyan': "\033[36m"
    }
    c = ""
    if style: c += codes.get(style, '')
    if fg: c += codes.get(fg, '')
    return f"{c}{text}{codes['reset']}"

def slow_print(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def print_header(title):
    print("\n" + "="*40)
    print(color(f"{title.center(40)}", fg='cyan', style='bold'))
    print("="*40 + "\n")

def print_intro():
    print(color(r"""

 ██▒   █▓▄▄▄      █    ██ ██▓ ▄▄▄█████▓    ▒█████   █████▒     ██████ ██░ ██ ▄▄▄     ▓█████▄ ▒█████  █     █░ ██████ 
▓██░   █▒████▄    ██  ▓██▓██▒ ▓  ██▒ ▓▒   ▒██▒  ██▓██   ▒    ▒██    ▒▓██░ ██▒████▄   ▒██▀ ██▒██▒  ██▓█░ █ ░█▒██    ▒ 
 ▓██  █▒▒██  ▀█▄ ▓██  ▒██▒██░ ▒ ▓██░ ▒░   ▒██░  ██▒████ ░    ░ ▓██▄  ▒██▀▀██▒██  ▀█▄ ░██   █▒██░  ██▒█░ █ ░█░ ▓██▄   
  ▒██ █░░██▄▄▄▄██▓▓█  ░██▒██░ ░ ▓██▓ ░    ▒██   ██░▓█▒  ░      ▒   ██░▓█ ░██░██▄▄▄▄██░▓█▄   ▒██   ██░█░ █ ░█  ▒   ██▒
   ▒▀█░  ▓█   ▓██▒▒█████▓░██████▒██▒ ░    ░ ████▓▒░▒█░       ▒██████▒░▓█▒░██▓▓█   ▓██░▒████▓░ ████▓▒░░██▒██▓▒██████▒▒
   ░ ▐░  ▒▒   ▓▒█░▒▓▒ ▒ ▒░ ▒░▓  ▒ ░░      ░ ▒░▒░▒░ ▒ ░       ▒ ▒▓▒ ▒ ░▒ ░░▒░▒▒▒   ▓▒█░▒▒▓  ▒░ ▒░▒░▒░░ ▓░▒ ▒ ▒ ▒▓▒ ▒ ░
   ░ ░░   ▒   ▒▒ ░░▒░ ░ ░░ ░ ▒  ░ ░         ░ ▒ ▒░ ░         ░ ░▒  ░ ░▒ ░▒░ ░ ▒   ▒▒ ░░ ▒  ▒  ░ ▒ ▒░  ▒ ░ ░ ░ ░▒  ░ ░
     ░░   ░   ▒   ░░░ ░ ░  ░ ░  ░         ░ ░ ░ ▒  ░ ░       ░  ░  ░  ░  ░░ ░ ░   ▒   ░ ░  ░░ ░ ░ ▒   ░   ░ ░  ░  ░  
      ░       ░  ░  ░        ░  ░             ░ ░                  ░  ░  ░  ░     ░  ░  ░       ░ ░     ░         ░  
     ░                                                                                ░                              

  """, fg = 'red'))

    print(color("Welcome to the Vault of Shadows. Choose wisely. Lives: 3\n", fg='yellow', style='bold'))
