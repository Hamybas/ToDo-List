import webbrowser

user_term = input('Enter a search: ').replace(' ', '+')

webbrowser.open('https://www.google.com/search?q=' + user_term)
