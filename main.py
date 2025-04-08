import telebot
import schedule
import time
import threading
from flask import Flask
from datetime import date, datetime
import json

# === Ton token Telegram ===
bot = telebot.TeleBot("7952444866:AAEUQAg3zTqh4Q17Tfpgzu8xSQ1fnJ7w3rA")

# === Fichier JSON pour stocker les utilisateurs ===
try:
    with open("users.json", "r") as f:
        users = json.load(f)
except FileNotFoundError:
    users = {}

def save_users():
    with open("users.json", "w") as f:
        json.dump(users, f)

# === Commande /start ===
@bot.message_handler(commands=['start'])
def start(message):
    user_id = str(message.chat.id)
    if user_id not in users:
        users[user_id] = {
            "start_date": str(date.today()),
            "paused": False,
            "progression": {}
        }
        save_users()
        bot.send_message(message.chat.id, "Bienvenue sur SkinWise ! Tu es maintenant inscrit. Jour 1 commence aujourd’hui.")
    else:
        bot.send_message(message.chat.id, "Tu es déjà inscrit ! Le programme est en cours.")

# === Programme complet SkinWise – 30 jours ===
messages = {
    1: {
        "midi": "🌞 *Jour 1 – Midi*\n\n💧 Bois un verre d’eau maintenant\n🧴 Ne touche pas ton visage sans te laver les mains\n🍽️ Mange un fruit riche en antioxydants (ex: papaye, goyave)\n💪 10 min d’activité légère ou 10 squats\n🧠 Ferme les yeux, respire, et dis-toi : *Ma peau devient plus saine chaque jour.*",
        "soir": "🌙 *Jour 1 – Soir*\n\n🧴 Nettoyage doux + huile végétale (jojoba, nigelle ou carotte)\n💧 Eau tiède + citron\n🍽️ Pas de sucre ajouté ce soir\n💪 Étirement rapide 2 min ou gainage\n🧠 Écris 1 chose dont tu es fier aujourd’hui."
    },
    2: {
        "midi": "🌞 *Jour 2 – Midi*\n\n💧 Bois un verre d’eau maintenant\n🧴 Ne touche pas ton visage sans te laver les mains\n🍽️ Mange un fruit riche en antioxydants (ex: papaye, goyave)\n💪 10 min d’activité légère ou 10 squats\n🧠 Ferme les yeux, respire, et dis-toi : *Ma peau devient plus saine chaque jour.*",
        "soir": "🌙 *Jour 2 – Soir*\n\n🧴 Nettoyage doux + huile végétale (jojoba, nigelle ou carotte)\n💧 Eau tiède + citron\n🍽️ Pas de sucre ajouté ce soir\n💪 Étirement rapide 2 min ou gainage\n🧠 Écris 1 chose dont tu es fier aujourd’hui."
    },
    3: {
        "midi": "🌞 *Jour 3 – Midi*\n\n💧 Bois un verre d’eau maintenant\n🧴 Ne touche pas ton visage sans te laver les mains\n🍽️ Mange un fruit riche en antioxydants (ex: papaye, goyave)\n💪 10 min d’activité légère ou 10 squats\n🧠 Ferme les yeux, respire, et dis-toi : *Ma peau devient plus saine chaque jour.*",
        "soir": "🌙 *Jour 3 – Soir*\n\n🧴 Nettoyage doux + huile végétale (jojoba, nigelle ou carotte)\n💧 Eau tiède + citron\n🍽️ Pas de sucre ajouté ce soir\n💪 Étirement rapide 2 min ou gainage\n🧠 Écris 1 chose dont tu es fier aujourd’hui."
    },
    4: {
        "midi": "🌞 *Jour 4 – Midi*\n\n💧 Bois un verre d’eau maintenant\n🧴 Ne touche pas ton visage sans te laver les mains\n🍽️ Mange un fruit riche en antioxydants (ex: papaye, goyave)\n💪 10 min d’activité légère ou 10 squats\n🧠 Ferme les yeux, respire, et dis-toi : *Ma peau devient plus saine chaque jour.*",
        "soir": "🌙 *Jour 4 – Soir*\n\n🧴 Nettoyage doux + huile végétale (jojoba, nigelle ou carotte)\n💧 Eau tiède + citron\n🍽️ Pas de sucre ajouté ce soir\n💪 Étirement rapide 2 min ou gainage\n🧠 Écris 1 chose dont tu es fier aujourd’hui."
    },
    5: {
        "midi": "🌞 *Jour 5 – Midi*\n\n💧 Bois un verre d’eau maintenant\n🧴 Ne touche pas ton visage sans te laver les mains\n🍽️ Mange un fruit riche en antioxydants (ex: papaye, goyave)\n💪 10 min d’activité légère ou 10 squats\n🧠 Ferme les yeux, respire, et dis-toi : *Ma peau devient plus saine chaque jour.*",
        "soir": "🌙 *Jour 5 – Soir*\n\n🧴 Nettoyage doux + huile végétale (jojoba, nigelle ou carotte)\n💧 Eau tiède + citron\n🍽️ Pas de sucre ajouté ce soir\n💪 Étirement rapide 2 min ou gainage\n🧠 Écris 1 chose dont tu es fier aujourd’hui."
    },
    6: {
        "midi": "🌞 *Jour 6 – Midi*\n\n💧 Bois un verre d’eau maintenant\n🧴 Ne touche pas ton visage sans te laver les mains\n🍽️ Mange un fruit riche en antioxydants (ex: papaye, goyave)\n💪 10 min d’activité légère ou 10 squats\n🧠 Ferme les yeux, respire, et dis-toi : *Ma peau devient plus saine chaque jour.*",
        "soir": "🌙 *Jour 6 – Soir*\n\n🧴 Nettoyage doux + huile végétale (jojoba, nigelle ou carotte)\n💧 Eau tiède + citron\n🍽️ Pas de sucre ajouté ce soir\n💪 Étirement rapide 2 min ou gainage\n🧠 Écris 1 chose dont tu es fier aujourd’hui."
    },
    7: {
        "midi": "🌞 *Jour 7 – Midi*\n\n💧 Bois un verre d’eau maintenant\n🧴 Ne touche pas ton visage sans te laver les mains\n🍽️ Mange un fruit riche en antioxydants (ex: papaye, goyave)\n💪 10 min d’activité légère ou 10 squats\n🧠 Ferme les yeux, respire, et dis-toi : *Ma peau devient plus saine chaque jour.*",
        "soir": "🌙 *Jour 7 – Soir*\n\n🧴 Nettoyage doux + huile végétale (jojoba, nigelle ou carotte)\n💧 Eau tiède + citron\n🍽️ Pas de sucre ajouté ce soir\n💪 Étirement rapide 2 min ou gainage\n🧠 Écris 1 chose dont tu es fier aujourd’hui."
    },
    8: {
        "midi": "🌞 *Jour 8 – Midi*\n\n💧 Bois un verre d’eau maintenant\n🧴 Ne touche pas ton visage sans te laver les mains\n🍽️ Mange un fruit riche en antioxydants (ex: papaye, goyave)\n💪 10 min d’activité légère ou 10 squats\n🧠 Ferme les yeux, respire, et dis-toi : *Ma peau devient plus saine chaque jour.*",
        "soir": "🌙 *Jour 8 – Soir*\n\n🧴 Nettoyage doux + huile végétale (jojoba, nigelle ou carotte)\n💧 Eau tiède + citron\n🍽️ Pas de sucre ajouté ce soir\n💪 Étirement rapide 2 min ou gainage\n🧠 Écris 1 chose dont tu es fier aujourd’hui."
    },
    9: {
        "midi": "🌞 *Jour 9 – Midi*\n\n💧 Bois un verre d’eau maintenant\n🧴 Ne touche pas ton visage sans te laver les mains\n🍽️ Mange un fruit riche en antioxydants (ex: papaye, goyave)\n💪 10 min d’activité légère ou 10 squats\n🧠 Ferme les yeux, respire, et dis-toi : *Ma peau devient plus saine chaque jour.*",
        "soir": "🌙 *Jour 9 – Soir*\n\n🧴 Nettoyage doux + huile végétale (jojoba, nigelle ou carotte)\n💧 Eau tiède + citron\n🍽️ Pas de sucre ajouté ce soir\n💪 Étirement rapide 2 min ou gainage\n🧠 Écris 1 chose dont tu es fier aujourd’hui."
    },
    10: {
        "midi": "🌞 *Jour 10 – Midi*\n\n💧 Bois un verre d’eau maintenant\n🧴 Ne touche pas ton visage sans te laver les mains\n🍽️ Mange un fruit riche en antioxydants (ex: papaye, goyave)\n💪 10 min d’activité légère ou 10 squats\n🧠 Ferme les yeux, respire, et dis-toi : *Ma peau devient plus saine chaque jour.*",
        "soir": "🌙 *Jour 10 – Soir*\n\n🧴 Nettoyage doux + huile végétale (jojoba, nigelle ou carotte)\n💧 Eau tiède + citron\n🍽️ Pas de sucre ajouté ce soir\n💪 Étirement rapide 2 min ou gainage\n🧠 Écris 1 chose dont tu es fier aujourd’hui."
    },
    11: {
        "midi": "🌞 *Jour 11 – Midi*\n\n💧 Bois un verre d’eau maintenant\n🧴 Ne touche pas ton visage sans te laver les mains\n🍽️ Mange un fruit riche en antioxydants (ex: papaye, goyave)\n💪 10 min d’activité légère ou 10 squats\n🧠 Ferme les yeux, respire, et dis-toi : *Ma peau devient plus saine chaque jour.*",
        "soir": "🌙 *Jour 11 – Soir*\n\n🧴 Nettoyage doux + huile végétale (jojoba, nigelle ou carotte)\n💧 Eau tiède + citron\n🍽️ Pas de sucre ajouté ce soir\n💪 Étirement rapide 2 min ou gainage\n🧠 Écris 1 chose dont tu es fier aujourd’hui."
    },
    12: {
        "midi": "🌞 *Jour 12 – Midi*\n\n💧 Bois un verre d’eau maintenant\n🧴 Ne touche pas ton visage sans te laver les mains\n🍽️ Mange un fruit riche en antioxydants (ex: papaye, goyave)\n💪 10 min d’activité légère ou 10 squats\n🧠 Ferme les yeux, respire, et dis-toi : *Ma peau devient plus saine chaque jour.*",
        "soir": "🌙 *Jour 12 – Soir*\n\n🧴 Nettoyage doux + huile végétale (jojoba, nigelle ou carotte)\n💧 Eau tiède + citron\n🍽️ Pas de sucre ajouté ce soir\n💪 Étirement rapide 2 min ou gainage\n🧠 Écris 1 chose dont tu es fier aujourd’hui."
    },
    13: {
        "midi": "🌞 *Jour 13 – Midi*\n\n💧 Bois un verre d’eau maintenant\n🧴 Ne touche pas ton visage sans te laver les mains\n🍽️ Mange un fruit riche en antioxydants (ex: papaye, goyave)\n💪 10 min d’activité légère ou 10 squats\n🧠 Ferme les yeux, respire, et dis-toi : *Ma peau devient plus saine chaque jour.*",
        "soir": "🌙 *Jour 13 – Soir*\n\n🧴 Nettoyage doux + huile végétale (jojoba, nigelle ou carotte)\n💧 Eau tiède + citron\n🍽️ Pas de sucre ajouté ce soir\n💪 Étirement rapide 2 min ou gainage\n🧠 Écris 1 chose dont tu es fier aujourd’hui."
    },
    14: {
        "midi": "🌞 *Jour 14 – Midi*\n\n💧 Bois un verre d’eau maintenant\n🧴 Ne touche pas ton visage sans te laver les mains\n🍽️ Mange un fruit riche en antioxydants (ex: papaye, goyave)\n💪 10 min d’activité légère ou 10 squats\n🧠 Ferme les yeux, respire, et dis-toi : *Ma peau devient plus saine chaque jour.*",
        "soir": "🌙 *Jour 14 – Soir*\n\n🧴 Nettoyage doux + huile végétale (jojoba, nigelle ou carotte)\n💧 Eau tiède + citron\n🍽️ Pas de sucre ajouté ce soir\n💪 Étirement rapide 2 min ou gainage\n🧠 Écris 1 chose dont tu es fier aujourd’hui."
    },
    15: {
        "midi": "🌞 *Jour 15 – Midi*\n\n💧 Bois un verre d’eau maintenant\n🧴 Ne touche pas ton visage sans te laver les mains\n🍽️ Mange un fruit riche en antioxydants (ex: papaye, goyave)\n💪 10 min d’activité légère ou 10 squats\n🧠 Ferme les yeux, respire, et dis-toi : *Ma peau devient plus saine chaque jour.*",
        "soir": "🌙 *Jour 15 – Soir*\n\n🧴 Nettoyage doux + huile végétale (jojoba, nigelle ou carotte)\n💧 Eau tiède + citron\n🍽️ Pas de sucre ajouté ce soir\n💪 Étirement rapide 2 min ou gainage\n🧠 Écris 1 chose dont tu es fier aujourd’hui."
    },
    16: {
        "midi": "🌞 *Jour 16 – Midi*\n\n💧 Bois un verre d’eau maintenant\n🧴 Ne touche pas ton visage sans te laver les mains\n🍽️ Mange un fruit riche en antioxydants (ex: papaye, goyave)\n💪 10 min d’activité légère ou 10 squats\n🧠 Ferme les yeux, respire, et dis-toi : *Ma peau devient plus saine chaque jour.*",
        "soir": "🌙 *Jour 16 – Soir*\n\n🧴 Nettoyage doux + huile végétale (jojoba, nigelle ou carotte)\n💧 Eau tiède + citron\n🍽️ Pas de sucre ajouté ce soir\n💪 Étirement rapide 2 min ou gainage\n🧠 Écris 1 chose dont tu es fier aujourd’hui."
    },
    17: {
        "midi": "🌞 *Jour 17 – Midi*\n\n💧 Bois un verre d’eau maintenant\n🧴 Ne touche pas ton visage sans te laver les mains\n🍽️ Mange un fruit riche en antioxydants (ex: papaye, goyave)\n💪 10 min d’activité légère ou 10 squats\n🧠 Ferme les yeux, respire, et dis-toi : *Ma peau devient plus saine chaque jour.*",
        "soir": "🌙 *Jour 17 – Soir*\n\n🧴 Nettoyage doux + huile végétale (jojoba, nigelle ou carotte)\n💧 Eau tiède + citron\n🍽️ Pas de sucre ajouté ce soir\n💪 Étirement rapide 2 min ou gainage\n🧠 Écris 1 chose dont tu es fier aujourd’hui."
    },
    18: {
        "midi": "🌞 *Jour 18 – Midi*\n\n💧 Bois un verre d’eau maintenant\n🧴 Ne touche pas ton visage sans te laver les mains\n🍽️ Mange un fruit riche en antioxydants (ex: papaye, goyave)\n💪 10 min d’activité légère ou 10 squats\n🧠 Ferme les yeux, respire, et dis-toi : *Ma peau devient plus saine chaque jour.*",
        "soir": "🌙 *Jour 18 – Soir*\n\n🧴 Nettoyage doux + huile végétale (jojoba, nigelle ou carotte)\n💧 Eau tiède + citron\n🍽️ Pas de sucre ajouté ce soir\n💪 Étirement rapide 2 min ou gainage\n🧠 Écris 1 chose dont tu es fier aujourd’hui."
    },
    19: {
        "midi": "🌞 *Jour 19 – Midi*\n\n💧 Bois un verre d’eau maintenant\n🧴 Ne touche pas ton visage sans te laver les mains\n🍽️ Mange un fruit riche en antioxydants (ex: papaye, goyave)\n💪 10 min d’activité légère ou 10 squats\n🧠 Ferme les yeux, respire, et dis-toi : *Ma peau devient plus saine chaque jour.*",
        "soir": "🌙 *Jour 19 – Soir*\n\n🧴 Nettoyage doux + huile végétale (jojoba, nigelle ou carotte)\n💧 Eau tiède + citron\n🍽️ Pas de sucre ajouté ce soir\n💪 Étirement rapide 2 min ou gainage\n🧠 Écris 1 chose dont tu es fier aujourd’hui."
    },
    20: {
        "midi": "🌞 *Jour 20 – Midi*\n\n💧 Bois un verre d’eau maintenant\n🧴 Ne touche pas ton visage sans te laver les mains\n🍽️ Mange un fruit riche en antioxydants (ex: papaye, goyave)\n💪 10 min d’activité légère ou 10 squats\n🧠 Ferme les yeux, respire, et dis-toi : *Ma peau devient plus saine chaque jour.*",
        "soir": "🌙 *Jour 20 – Soir*\n\n🧴 Nettoyage doux + huile végétale (jojoba, nigelle ou carotte)\n💧 Eau tiède + citron\n🍽️ Pas de sucre ajouté ce soir\n💪 Étirement rapide 2 min ou gainage\n🧠 Écris 1 chose dont tu es fier aujourd’hui."
    },
    21: {
        "midi": "🌞 *Jour 21 – Midi*\n\n💧 Bois un verre d’eau maintenant\n🧴 Ne touche pas ton visage sans te laver les mains\n🍽️ Mange un fruit riche en antioxydants (ex: papaye, goyave)\n💪 10 min d’activité légère ou 10 squats\n🧠 Ferme les yeux, respire, et dis-toi : *Ma peau devient plus saine chaque jour.*",
        "soir": "🌙 *Jour 21 – Soir*\n\n🧴 Nettoyage doux + huile végétale (jojoba, nigelle ou carotte)\n💧 Eau tiède + citron\n🍽️ Pas de sucre ajouté ce soir\n💪 Étirement rapide 2 min ou gainage\n🧠 Écris 1 chose dont tu es fier aujourd’hui."
    },
    22: {
        "midi": "🌞 *Jour 22 – Midi*\n\n💧 Bois un verre d’eau maintenant\n🧴 Ne touche pas ton visage sans te laver les mains\n🍽️ Mange un fruit riche en antioxydants (ex: papaye, goyave)\n💪 10 min d’activité légère ou 10 squats\n🧠 Ferme les yeux, respire, et dis-toi : *Ma peau devient plus saine chaque jour.*",
        "soir": "🌙 *Jour 22 – Soir*\n\n🧴 Nettoyage doux + huile végétale (jojoba, nigelle ou carotte)\n💧 Eau tiède + citron\n🍽️ Pas de sucre ajouté ce soir\n💪 Étirement rapide 2 min ou gainage\n🧠 Écris 1 chose dont tu es fier aujourd’hui."
    },
    23: {
        "midi": "🌞 *Jour 23 – Midi*\n\n💧 Bois un verre d’eau maintenant\n🧴 Ne touche pas ton visage sans te laver les mains\n🍽️ Mange un fruit riche en antioxydants (ex: papaye, goyave)\n💪 10 min d’activité légère ou 10 squats\n🧠 Ferme les yeux, respire, et dis-toi : *Ma peau devient plus saine chaque jour.*",
        "soir": "🌙 *Jour 23 – Soir*\n\n🧴 Nettoyage doux + huile végétale (jojoba, nigelle ou carotte)\n💧 Eau tiède + citron\n🍽️ Pas de sucre ajouté ce soir\n💪 Étirement rapide 2 min ou gainage\n🧠 Écris 1 chose dont tu es fier aujourd’hui."
    },
    24: {
        "midi": "🌞 *Jour 24 – Midi*\n\n💧 Bois un verre d’eau maintenant\n🧴 Ne touche pas ton visage sans te laver les mains\n🍽️ Mange un fruit riche en antioxydants (ex: papaye, goyave)\n💪 10 min d’activité légère ou 10 squats\n🧠 Ferme les yeux, respire, et dis-toi : *Ma peau devient plus saine chaque jour.*",
        "soir": "🌙 *Jour 24 – Soir*\n\n🧴 Nettoyage doux + huile végétale (jojoba, nigelle ou carotte)\n💧 Eau tiède + citron\n🍽️ Pas de sucre ajouté ce soir\n💪 Étirement rapide 2 min ou gainage\n🧠 Écris 1 chose dont tu es fier aujourd’hui."
    },
    25: {
        "midi": "🌞 *Jour 25 – Midi*\n\n💧 Bois un verre d’eau maintenant\n🧴 Ne touche pas ton visage sans te laver les mains\n🍽️ Mange un fruit riche en antioxydants (ex: papaye, goyave)\n💪 10 min d’activité légère ou 10 squats\n🧠 Ferme les yeux, respire, et dis-toi : *Ma peau devient plus saine chaque jour.*",
        "soir": "🌙 *Jour 25 – Soir*\n\n🧴 Nettoyage doux + huile végétale (jojoba, nigelle ou carotte)\n💧 Eau tiède + citron\n🍽️ Pas de sucre ajouté ce soir\n💪 Étirement rapide 2 min ou gainage\n🧠 Écris 1 chose dont tu es fier aujourd’hui."
    },
    26: {
        "midi": "🌞 *Jour 26 – Midi*\n\n💧 Bois un verre d’eau maintenant\n🧴 Ne touche pas ton visage sans te laver les mains\n🍽️ Mange un fruit riche en antioxydants (ex: papaye, goyave)\n💪 10 min d’activité légère ou 10 squats\n🧠 Ferme les yeux, respire, et dis-toi : *Ma peau devient plus saine chaque jour.*",
        "soir": "🌙 *Jour 26 – Soir*\n\n🧴 Nettoyage doux + huile végétale (jojoba, nigelle ou carotte)\n💧 Eau tiède + citron\n🍽️ Pas de sucre ajouté ce soir\n💪 Étirement rapide 2 min ou gainage\n🧠 Écris 1 chose dont tu es fier aujourd’hui."
    },
    27: {
        "midi": "🌞 *Jour 27 – Midi*\n\n💧 Bois un verre d’eau maintenant\n🧴 Ne touche pas ton visage sans te laver les mains\n🍽️ Mange un fruit riche en antioxydants (ex: papaye, goyave)\n💪 10 min d’activité légère ou 10 squats\n🧠 Ferme les yeux, respire, et dis-toi : *Ma peau devient plus saine chaque jour.*",
        "soir": "🌙 *Jour 27 – Soir*\n\n🧴 Nettoyage doux + huile végétale (jojoba, nigelle ou carotte)\n💧 Eau tiède + citron\n🍽️ Pas de sucre ajouté ce soir\n💪 Étirement rapide 2 min ou gainage\n🧠 Écris 1 chose dont tu es fier aujourd’hui."
    },
    28: {
        "midi": "🌞 *Jour 28 – Midi*\n\n💧 Bois un verre d’eau maintenant\n🧴 Ne touche pas ton visage sans te laver les mains\n🍽️ Mange un fruit riche en antioxydants (ex: papaye, goyave)\n💪 10 min d’activité légère ou 10 squats\n🧠 Ferme les yeux, respire, et dis-toi : *Ma peau devient plus saine chaque jour.*",
        "soir": "🌙 *Jour 28 – Soir*\n\n🧴 Nettoyage doux + huile végétale (jojoba, nigelle ou carotte)\n💧 Eau tiède + citron\n🍽️ Pas de sucre ajouté ce soir\n💪 Étirement rapide 2 min ou gainage\n🧠 Écris 1 chose dont tu es fier aujourd’hui."
    },
    29: {
        "midi": "🌞 *Jour 29 – Midi*\n\n💧 Bois un verre d’eau maintenant\n🧴 Ne touche pas ton visage sans te laver les mains\n🍽️ Mange un fruit riche en antioxydants (ex: papaye, goyave)\n💪 10 min d’activité légère ou 10 squats\n🧠 Ferme les yeux, respire, et dis-toi : *Ma peau devient plus saine chaque jour.*",
        "soir": "🌙 *Jour 29 – Soir*\n\n🧴 Nettoyage doux + huile végétale (jojoba, nigelle ou carotte)\n💧 Eau tiède + citron\n🍽️ Pas de sucre ajouté ce soir\n💪 Étirement rapide 2 min ou gainage\n🧠 Écris 1 chose dont tu es fier aujourd’hui."
    },
    30: {
        "midi": "🌞 *Jour 30 – Midi*\n\n💧 Bois un verre d’eau maintenant\n🧴 Ne touche pas ton visage sans te laver les mains\n🍽️ Mange un fruit riche en antioxydants (ex: papaye, goyave)\n💪 10 min d’activité légère ou 10 squats\n🧠 Ferme les yeux, respire, et dis-toi : *Ma peau devient plus saine chaque jour.*",
        "soir": "🌙 *Jour 30 – Soir*\n\n🧴 Nettoyage doux + huile végétale (jojoba, nigelle ou carotte)\n💧 Eau tiède + citron\n🍽️ Pas de sucre ajouté ce soir\n💪 Étirement rapide 2 min ou gainage\n🧠 Écris 1 chose dont tu es fier aujourd’hui."
    },
}

# === Fonction d'envoi automatique ===
def envoyer_messages(moment):
    today = date.today()
    for user_id, data in users.items():
        if data["paused"]:
            continue
        start = datetime.strptime(data["start_date"], "%Y-%m-%d").date()
        jour = (today - start).days + 1
        if 1 <= jour <= 30:
            msg = messages.get(jour, {}).get(moment)
            if msg:
                bot.send_message(int(user_id), msg, parse_mode="Markdown")

# === Programmation des horaires ===
schedule.every().day.at("12:30").do(envoyer_messages, moment="midi")
schedule.every().day.at("21:20").do(envoyer_messages, moment="soir")

# === Tâche parallèle pour exécuter les tâches programmées ===
def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

threading.Thread(target=run_schedule).start()

# === Serveur Flask pour que Replit reste allumé ===
app = Flask(__name__)

@app.route('/')
def home():
    return "SkinWise Bot is running."

# === Thread Flask ===
def run_flask():
    app.run(host='0.0.0.0', port=8080)

threading.Thread(target=run_flask).start()

# === Lancement du bot ===
bot.polling()
