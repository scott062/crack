def urlify(text):
    text_copy = text.strip()
    return text_copy.replace(" ", "%20")

def urlify_python(text, length):
    return text[:length].replace(" ", "%20")

# urlify python, using the assumed length can avoid the replace complexity
# by simly looping through the necessary length
print(urlify_python("Scott BBBBBBB", 13))
print(urlify_python("Scott is so cool     ", 16))
