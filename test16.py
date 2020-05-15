# This program is designed to understand dictionary and working of functions
def emoji_converter(msg):
    words = msg.split(" ")
    emoji = {
        ":)": "hehe!!!",
        ":(": "ew"
    }
    o = ""
    for word in words:
        o += emoji.get(word, word) + " "
    return o
