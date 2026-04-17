# 🤖 Link Remover Telegram Bot

A simple Python-based Telegram bot that automatically deletes links (URLs) from messages in groups and channels.

---

## 🚀 Features

* 🔗 Automatically deletes links (URLs)
* ✏️ Scans both new and edited messages
* 👑 Admins are ignored (their messages are safe)
* ⚡ Fast and lightweight
* 🛡️ Helps keep groups spam-free

---

## 📁 Project Structure

```
Link_Remover_Bot/
│── main.py
│── bot.py
│── config.py
│── requirements.txt
│── README.md
```

---

## ⚙️ Setup Guide

### 1️⃣ Clone Repository

```
git clone https://github.com/vivekxn/Link_Remover_Telegram_Bot.git
cd Link_Remover_Telegram_Bot
```

---

### 2️⃣ Install Requirements

```
pip install -r requirements.txt
```

---

### 3️⃣ Configure Bot

Open `config.py` and add your details:

```
TOKEN = "YOUR_BOT_TOKEN"

ADMINS = [
    123456789,
    987654321
]
```

### ⚠️ Important:

* Use **numbers** for admin IDs (not strings)
* Get your Telegram ID using bots like userinfobot

---

### 4️⃣ Run the Bot

```
python main.py
```

---

## 🤖 How It Works

* User sends a message with a link → ❌ Bot deletes it
* Admin sends a message with a link → ✅ Allowed
* Edited message → 🔍 Bot checks again

---

## ⚠️ Requirements

* Python 3.7+
* Bot must be **admin in group**
* Enable permission:

  * ✅ Delete Messages

---

## 📦 requirements.txt

```
pyTelegramBotAPI
```

---

## 🛠️ Built With

* Python
* pyTelegramBotAPI

---

## 💡 Future Improvements

* 🚫 Block specific domains only
* ⚠️ Warning system
* 🔇 Auto mute users
* 📊 Logs system
* 🌍 Multi-group support

---

## 👨‍💻 Author

Made with ❤️ by You

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
