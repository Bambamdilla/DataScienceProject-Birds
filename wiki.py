import webbrowser
import predict

# Wyświetlenie strony z wiki na podstawie predykcji
def get_wiki():
    bird_name = predict.predict()
    name = bird_name.lower().capitalize().split()
    if name[0][-1:] == 's':  # Abert%27s_towhee
        wiki_name = name[0][:-1] + '%27s_'
        name = name[1:]
        wiki_name += '_'.join(name)
    else:
        wiki_name = '_'.join(name)
    url = "https://en.wikipedia.org/wiki/{}".format(wiki_name)

    return url


webbrowser.register('chrome', None,
                    webbrowser.BackgroundBrowser("C://Program files//Google//Chrome//Application//chrome.exe"))
webbrowser.get('chrome').open(get_wiki())

