import webbrowser

question = input("Question? ")
url = "https://www.google.com/search?q=" + question.replace(" ", "+")
print(url)
webbrowser.open(url)
