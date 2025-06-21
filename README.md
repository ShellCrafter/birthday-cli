✅ README.md
markdown
Copy
Edit
# 🎉 Ultimate Birthday CLI Tool 🎉

A colorful and interactive command-line birthday greeting tool written in Python. It uses rich text, ASCII art, animations, and colors to create a festive birthday celebration right in your terminal or Termux!

---

## 📸 Demo

![Birthday CLI Tool Demo](https://github.com/ShellCrafter/birthday-cli.git)


---

## 💡 Features

- 💖 Animated heart, cake, bottle, and firework ASCII art
- 🎨 Colorful terminal text using `termcolor`, `pyfiglet`, and `rich`
- 🗓️ Auto-detects today’s date
- 🎂 Sends warm wishes in a styled birthday card
- 💻 Runs in Termux, Linux, macOS, and Windows (with Python installed)

---

## 📦 Requirements

Make sure Python 3 is installed. Then install the required packages:

```bash
pip install termcolor pyfiglet rich
If you're on Termux, install Python first:

bash
Copy
Edit
pkg update && pkg upgrade
pkg install python git
pip install termcolor pyfiglet rich
🔧 Installation
📲 For Termux
bash
Copy
Edit
pkg install git python -y
git clone https://github.com/ShellCrafter/birthday-cli.git
cd birthday-cli
pip install -r requirements.txt
python birthday.py
💻 For Linux / macOS
bash
Copy
Edit
sudo apt update && sudo apt install python3 git -y
git clone https://github.com/ShellCrafter/birthday-cli.git
cd birthday-cli
pip3 install -r requirements.txt
python3 birthday.py
🪟 For Windows (Command Prompt / PowerShell)
Install Python

Open Command Prompt:

bash
Copy
Edit
git clone https://github.com/ShellCrafter/birthday-cli.git
cd birthday-cli
pip install -r requirements.txt
python birthday.py
📄 Create requirements.txt
If not present already, create a requirements.txt file with:

rust
Copy
Edit
termcolor
pyfiglet
rich
To generate automatically:

bash
Copy
Edit
pip freeze > requirements.txt
🚀 Usage
Once cloned and dependencies installed, run it with:

bash
Copy
Edit
python birthday.py
It will ask for the person's name, then generate a beautiful animated birthday greeting.

🧪 Example
bash
Copy
Edit
$ python birthday.py
💖 Welcome to the Ultimate Birthday CLI Tool 💖

🎈 What's your name? John

# Output will render animated heart, birthday cake, firework, message, and rich birthday card
