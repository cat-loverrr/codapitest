from flask import Flask, jsonify

app = Flask(__name__)

characters = {
    "price": {
        "name": "Captain John Price",
        "games": ["Modern Warfare (2007)", "Modern Warfare 2 (2009)", "Modern Warfare (2019)"],
        "faction": "Task Force 141",
        "first_appearance": "Call of Duty 4: Modern Warfare",
        "wiki_url": "https://callofduty.fandom.com/wiki/John_Price"
    },
    "soap": {
        "name": "John 'Soap' MacTavish",
        "games": ["Modern Warfare (2007)", "Modern Warfare 2 (2009)", "Modern Warfare 3 (2011)"],
        "faction": "Task Force 141",
        "first_appearance": "Call of Duty 4: Modern Warfare",
        "wiki_url": "https://callofduty.fandom.com/wiki/John_%22Soap%22_MacTavish"
    }
}

@app.get("/characters/<name>")
def get_character(name):
    key = name.lower()
    if key in characters:
        return jsonify(characters[key])
    return jsonify({"error": "Character not found"}), 404

@app.get("/characters")
def list_characters():
    return jsonify(list(characters.keys()))

if __name__ == "__main__":
    app.run(debug=True)

