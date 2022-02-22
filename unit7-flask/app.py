from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return "Hi there, how ya doin?"

@app.route('/anagrams/<word>')
def anagrams(word):
    f = open('words.txt')
    wordlist = map(lambda x: x.strip(), f.readlines())
    f.close()

    anagrams = []
    for w in wordlist:
        if sorted(word.upper()) == sorted(w.upper()):
            anagrams.append(w)
    return str(anagrams)

if __name__ == "__main__":
    app.run()
