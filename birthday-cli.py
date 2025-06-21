import time
import datetime
from termcolor import colored
from pyfiglet import Figlet
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def animate_text(text, delay=0.03, color="cyan"):
    for char in text:
        print(colored(char, color), end='', flush=True)
        time.sleep(delay)
    print()

def heart_ascii():
    heart = [
        "  ***     ***  ",
        "******* *******",
        "***************",
        " ************* ",
        "  ***********  ",
        "   *********   ",
        "    *******    ",
        "     *****     ",
        "      ***      ",
        "       *       "
    ]
    for line in heart:
        print(colored(line.center(50), "red"))
        time.sleep(0.07)

def bottle_ascii():
    bottle = [
        "     ||      ||     ",
        "     ||      ||     ",
        "     ||      ||     ",
        "    [##]    [##]    ",
        "    |##|    |##|    ",
        "    |##|    |##|    ",
        "    |##|    |##|    ",
        "    |##|    |##|    ",
        "    |##|    |##|    ",
        "    |##|    |##|    ",
        "    |__|    |__|    ",
        "   /____\\  /____\\   "
    ]
    for line in bottle:
        print(colored(line.center(50), "yellow"))
        time.sleep(0.07)

def cake_ascii():
    cake = [
        "        i i i        ",
        "      |:H:a:p:p:y:|   ",
        "    __|___________|__ ",
        "   |^^^^^^^^^^^^^^^^^|",
        "   |:B:i:r:t:h:d:a:y:|",
        "   |                 |",
        "   ~~~~~~~~~~~~~~~~~~~"
    ]
    for line in cake:
        print(colored(line.center(50), "magenta"))
        time.sleep(0.07)

def fireworks():
    fire = [
        "      .''.       ",
        "     :_\\/_:      ",
        " .''.: /\\ :.''.  ",
        ":_\\/_:'.::.' :   ",
        ": /\\ : :::::  :  ",
        " '..'  '::'   :  ",
        "     *         *",
        "   *     *    *  ",
        " *   *   *   *   ",
    ]
    for _ in range(2):
        for line in fire:
            print(colored(line.center(50), "cyan"))
        time.sleep(0.3)

def sparkle_animation():
    sparkles = ["✨", "💫", "🌟", "🎉", "🎊", "🥳"]
    for _ in range(3):
        line = ''.join([colored(char, "blue") for char in sparkles])
        print(line.center(50))
        time.sleep(0.2)

def show_rich_birthday_card(name):
    today = datetime.datetime.now().strftime("%A, %d %B %Y")
    message = f"""
🎉 Happy Birthday {name}! 🎉

💖 Wishing you a joyful day filled with love, fun, and dreams come true!

🎂 Enjoy your cake and 🍾 celebrate with style!

📅 Date: {today}

-- From your Python CLI Bot 🤖
"""
    card = Panel(Text(message, justify="center"), title="🎈 Birthday Wishes 🎈", border_style="bold magenta")
    console.print(card)

def show_birthday(name):
    animate_text(f"🎉 Hello {name}!", color="magenta")
    time.sleep(0.5)

    # Render name in big CLI style
    fig_name = Figlet(font='big')
    print(colored(fig_name.renderText(name), "cyan"))
    time.sleep(1)

    fig = Figlet(font='slant')
    print(colored(fig.renderText("Happy Birthday!"), "green"))
    time.sleep(1)

    today = datetime.datetime.now().strftime("%A, %d %B %Y")
    animate_text(f"📅 Today is: {today}", 0.04, "blue")
    print()

    sparkle_animation()
    heart_ascii()
    time.sleep(1)

    cake_ascii()
    time.sleep(1)

    bottle_ascii()
    time.sleep(1)

    animate_text(f"Dear {name},", 0.03, "yellow")
    animate_text("Wishing you a fantastic day full of joy, love, and cake 🎂!", 0.03, "cyan")
    animate_text("May your dreams come true and your smile shine bright 💖", 0.03, "green")
    print()

    fireworks()
    animate_text("✨ With Love, Your Python CLI Friend  🤖", 0.04, "magenta")
    print()

    show_rich_birthday_card(name)

def main():
    print(colored("💖 Welcome to the Ultimate Birthday CLI Tool 💖", "blue", attrs=["bold"]))
    print()
    name = input(colored("🎈 What's your name? ", "cyan"))
    show_birthday(name)

if __name__ == "__main__":
    main()