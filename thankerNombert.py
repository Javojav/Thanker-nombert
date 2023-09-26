sys.stdout.flush()
wait()

def print_fast(str):
for letter in str:
sys.stdout.write(letter)
sys.stdout.flush()
wait()

def print_art():
print_fast("  _______ _                 _               _   _                 _               _   \n")
print_fast(" |__   __| |               | |             | \ | |               | |             | |  \n")
print_fast("    | |  | |__   __ _ _ __ | | _____ _ __  |  \| | ___  _ __ ___ | |__   ___ _ __| |_ \n")
print_fast("    | |  | '_ \ / _` | '_ \| |/ / _ \ '__| | . ` |/ _ \| '_ ` _ \| '_ \ / _ \ '__| __|\n")
print_fast("    | |  | | | | (_| | | | |   <  __/ |    | |\  | (_) | | | | | | |_) |  __/ |  | |_ \n")
print_fast("    |_|  |_| |_|\__,_|_| |_|_|\_\___|_|    |_| \_|\___/|_| |_| |_|_.__/ \___|_|   \__|\n")
def print_color(str):
for letter in str:
sys.stdout.write(random.choice(['\033[92m', '\033[93m', '\033[91m', '\033[95m', '\033[96m', '\033[94m']) + letter + '\033[0m')
sys.stdout.flush()
wait()
def print_color_slow(str):
for letter in str:
sys.stdout.write(random.choice(['\033[92m', '\033[93m', '\033[91m', '\033[95m', '\033[96m', '\033[94m']) + letter + '\033[0m')
sys.stdout.flush()
time.sleep(0.1)
def print_color_fast(str):
for letter in str:
sys.stdout.write(random.choice(['\033[92m', '\033[93m', '\033[91m', '\033[95m', '\033[96m', '\033[94m']) + letter + '\033[0m')
sys.stdout.flush()
wait()
def print_art_color():
print_color_fast("  _______ _                 _               _   _                 _               _   \n")
print_color_fast(" |__   __| |               | |             | \ | |               | |             | |  \n")
print_color_fast("    | |  | |__   __ _ _ __ | | _____ _ __  |  \| | ___  _ __ ___ | |__   ___ _ __| |_ \n")
print_color_fast("    | |  | '_ \ / _` | '_ \| |/ / _ \ '__| | . ` |/ _ \| '_ ` _ \| '_ \ / _ \ '__| __|\n")
print_color_fast("    | |  | | | | (_| | | | |   <  __/ |    | |\  | (_) | | | | | | |_) |  __/ |  | |_ \n")
print_color_fast("    |_|  |_| |_|\__,_|_| |_|_|\_\___|_|    |_| \_|\___/|_| |_| |_|_.__/ \___|_|   \__|\n")
while True:
clear()
print_art_color()
wait()

