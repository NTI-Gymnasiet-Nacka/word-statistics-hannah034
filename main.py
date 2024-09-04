# Ordstatistik
# Din uppgift är att läsa in text från filen som är angiven.
# Därefter ska ditt program räkna ut följande:
# - Antal ord
# - Mest frekventa ord
# - Genomsnittlig ordlängd
# Gör en funktion för varje.

# Bonus, gör en i taget, skapa en funktion för varje: 
# - Längsta och kortaste ordet - om det finns flera, bestäm själv om du skriver ut ett eller flera
# - Räkna antalet unika ord (alltså ord som bara förekommer en gång)


def read_from_file(path: str):
    """Reads a file with the given parameter path and returns the file as a list of strings, split on newline (\n).

    Args:
        path (str): the path of the readable file

    Returns:
        list(str): list of strings
    """
    with open(path, "r" ,encoding="utf-8") as f:
        return f.readlines()

def antal_ord(sentences):
    text = ' '.join(sentences)
    text = text.strip()
    words = text.split(' ') 
    return len(words)

def frekventa_ord(sentences):    
    text = ' '.join(sentences)
    text = text.strip()
    words = text.split(' ')
    störst_antal = 0
    mest_frekventa = ''
    for i in words:
        antal = words.count(i)
        if antal > störst_antal:
            mest_frekventa = i
            störst_antal = antal
    return mest_frekventa

def genomsnittlig_längd(sentences):
    text = ' '.join(sentences)
    text = text.strip()
    words = text.split(' ')
    medelvärde = []
    for i in words:
        medelvärde.append(len(i))
    medelvärde = int(sum(medelvärde) / len(words))
    return medelvärde

def main():
    
    sentences = read_from_file("en_resa_genom_svenska_skogen.txt") # Här har du nu en lista av strängar från den inlästa filen.
    print(antal_ord(sentences))
    print(frekventa_ord(sentences))
    print(genomsnittlig_längd(sentences))
    
if __name__ == "__main__":
    main()