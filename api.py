from flask import Flask, jsonify, request


app = Flask(__name__)


character_list = [
  {
    "name": "John Price",
    "games": ["Modern Warfare (2019)", "Modern Warfare II (2022)", "Modern Warfare III (2023)"],
    "faction": "Task Force 141",
    "first_appearance": "Modern Warfare (2019)",
    "wiki_url": "https://callofduty.fandom.com/wiki/John_Price_(Reboot)"
  },
  {
    "name": "Kyle 'Gaz' Garrick",
    "games": ["Modern Warfare (2019)", "Modern Warfare II (2022)", "Modern Warfare III (2023)"],
    "faction": "Task Force 141",
    "first_appearance": "Modern Warfare (2019)",
    "wiki_url": "https://callofduty.fandom.com/wiki/Kyle_Garrick"
  },
  {
    "name": "Simon 'Ghost' Riley",
    "games": ["Modern Warfare II (2022)", "Modern Warfare III (2023)"],
    "faction": "Task Force 141",
    "first_appearance": "Modern Warfare II (2022)",
    "wiki_url": "https://callofduty.fandom.com/wiki/Simon_Riley_(Reboot)"
  },
  {
    "name": "Johnny 'Soap' MacTavish",
    "games": ["Modern Warfare II (2022)", "Modern Warfare III (2023)"],
    "faction": "Task Force 141",
    "first_appearance": "Modern Warfare II (2022)",
    "wiki_url": "https://callofduty.fandom.com/wiki/Johnny_MacTavish_(Reboot)"
  },
  {
    "name": "Alejandro Vargas",
    "games": ["Modern Warfare II (2022)", "Modern Warfare III (2023)"],
    "faction": "Los Vaqueros; Task Force 141 (ally)",
    "first_appearance": "Modern Warfare II (2022)",
    "wiki_url": "https://callofduty.fandom.com/wiki/Alejandro_Vargas"
  },
  {
    "name": "Rodolfo 'Rudy' Parra",
    "games": ["Modern Warfare II (2022)", "Modern Warfare III (2023)"],
    "faction": "Los Vaqueros",
    "first_appearance": "Modern Warfare II (2022)",
    "wiki_url": "https://callofduty.fandom.com/wiki/Rodolfo_Parra"
  },
  {
    "name": "Farah Karim",
    "games": ["Modern Warfare (2019)", "Modern Warfare II (2022)"],
    "faction": "Urzikstan Liberation Force",
    "first_appearance": "Modern Warfare (2019)",
    "wiki_url": "https://callofduty.fandom.com/wiki/Farah_Karim"
  },
  {
    "name": "Alex Keller",
    "games": ["Modern Warfare (2019)", "Modern Warfare II (2022)"],
    "faction": "CIA; Task Force 141 (ally)",
    "first_appearance": "Modern Warfare (2019)",
    "wiki_url": "https://callofduty.fandom.com/wiki/Alex_Keller"
  },
  {
    "name": "Vladimir Makarov",
    "games": ["Modern Warfare III (2023)"],
    "faction": "Konni Group",
    "first_appearance": "Modern Warfare III (2023)",
    "wiki_url": "https://callofduty.fandom.com/wiki/Vladimir_Makarov_(Reboot)"
  },
  {
    "name": "Hassan Zyani",
    "games": ["Modern Warfare II (2022)"],
    "faction": "Iranian Quds Force (fictionalized)",
    "first_appearance": "Modern Warfare II (2022)",
    "wiki_url": "https://callofduty.fandom.com/wiki/Hassan_Zyani"
  },
  {
    "name": "Graves",
    "games": ["Modern Warfare II (2022)", "Modern Warfare III (2023)"],
    "faction": "Shadow Company",
    "first_appearance": "Modern Warfare II (2022)",
    "wiki_url": "https://callofduty.fandom.com/wiki/Phillip_Graves"
  },
  {
    "name": "Konni Group (General)",
    "games": ["Modern Warfare III (2023)"],
    "faction": "Konni Group",
    "first_appearance": "Modern Warfare III (2023)",
    "wiki_url": "https://callofduty.fandom.com/wiki/Konni_Group"
  },
  {
    "name": "Logan Walker",
    "games": ["Call of Duty: Ghosts"],
    "faction": "Ghosts",
    "first_appearance": "Call of Duty: Ghosts",
    "wiki_url": "https://callofduty.fandom.com/wiki/Logan_Walker"
  },
  {
    "name": "David 'Hesh' Walker",
    "games": ["Call of Duty: Ghosts"],
    "faction": "Ghosts",
    "first_appearance": "Call of Duty: Ghosts",
    "wiki_url": "https://callofduty.fandom.com/wiki/David_Walker"
  },
  {
    "name": "Elias Walker",
    "games": ["Call of Duty: Ghosts"],
    "faction": "Ghosts",
    "first_appearance": "Call of Duty: Ghosts",
    "wiki_url": "https://callofduty.fandom.com/wiki/Elias_Walker"
  },
  {
    "name": "Keegan P. Russ",
    "games": ["Call of Duty: Ghosts"],
    "faction": "Ghosts",
    "first_appearance": "Call of Duty: Ghosts",
    "wiki_url": "https://callofduty.fandom.com/wiki/Keegan_P._Russ"
  },
  {
    "name": "Thomas A. Merrick",
    "games": ["Call of Duty: Ghosts"],
    "faction": "Ghosts",
    "first_appearance": "Call of Duty: Ghosts",
    "wiki_url": "https://callofduty.fandom.com/wiki/Thomas_A._Merrick"
  },
  {
    "name": "Riley",
    "games": ["Call of Duty: Ghosts"],
    "faction": "Ghosts (K9 Unit)",
    "first_appearance": "Call of Duty: Ghosts",
    "wiki_url": "https://callofduty.fandom.com/wiki/Riley_(Ghosts)"
  },
  {
    "name": "Gabriel Rorke",
    "games": ["Call of Duty: Ghosts"],
    "faction": "Federation (former Ghosts)",
    "first_appearance": "Call of Duty: Ghosts",
    "wiki_url": "https://callofduty.fandom.com/wiki/Gabriel_Rorke"
  },
  {
    "name": "Victor Ramos",
    "games": ["Call of Duty: Ghosts"],
    "faction": "Federation",
    "first_appearance": "Call of Duty: Ghosts",
    "wiki_url": "https://callofduty.fandom.com/wiki/Victor_Ramos"
  },
  {
    "name": "Jacob 'Ajax' Hendricks",
    "games": ["Call of Duty: Ghosts"],
    "faction": "Ghosts",
    "first_appearance": "Call of Duty: Ghosts",
    "wiki_url": "https://callofduty.fandom.com/wiki/Ajax_(Ghosts)"
  },
  {
    "name": "Kate Laswell",
    "games": ["Modern Warfare (2019)", "Modern Warfare II (2022)", "Modern Warfare III (2023)"],
    "faction": "CIA; Task Force 141 (ally)",
    "first_appearance": "Modern Warfare (2019)",
    "wiki_url": "https://callofduty.fandom.com/wiki/Kate_Laswell"
  },
  {
    "name": "Kick",
    "games": ["Call of Duty: Ghosts"],
    "faction": "Ghosts",
    "first_appearance": "Call of Duty: Ghosts",
    "wiki_url": "https://callofduty.fandom.com/wiki/Kick"
  },
  {
    "name": "König",
    "games": ["Modern Warfare II (2022)", "Modern Warfare III (2023)"],
    "faction": "KorTac; SpecGru (multiplayer canon)",
    "first_appearance": "Modern Warfare II (2022)",
    "wiki_url": "https://callofduty.fandom.com/wiki/K%C3%B6nig"
  }
]


# -----------------------------
# KEYWORD SEARCH (NO FUZZY)
# -----------------------------
def search_character(query):
    query = query.lower()
    results = []


    for character in character_list:
        combined = (
            character["name"] + " " +
            " ".join(character["games"]) + " " +
            character["faction"] + " " +
            character["first_appearance"]
        ).lower()


        if query in combined:
            results.append(character)


    return results


# -----------------------------
# ROUTES
# -----------------------------


@app.get("/characters/<name>")
def get_character(name):
    results = search_character(name)
    if results:
        return jsonify(results)
    return jsonify({"error": "Character not found"}), 404


@app.get("/characters")
def list_characters():
    return jsonify([c["name"] for c in character_list])


@app.get("/search")
def search():
    query = request.args.get("q", "")
    results = search_character(query)
    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)


