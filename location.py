import nltk
import spacy
from nltk.tokenize import sent_tokenize

nltk.download('punkt')  # for sentence tokenization
nlp = spacy.load('en_core_web_sm')  # loading spaCy model

data = """Kathmandu, Nepal, 4 - went with an influential group w high security, brief time to expose
Bangkok, Pattaya, Thailand, 3.5 - tourist scams, political struggle/royal family, etc
Guangzhou, some border cities, China, 4 - high central security, some cyber crime, too many scammy sale tactic, fear of wrong/ unintended political expression that could lead to trouble, but other than that nothing unsafe unsafe. General/daily life pretty safe
Ho Chi Minh, Vietnam, 3.8 or 4 - unsafe for women @ night in certain area/ high assault rate as seen for female expat, petty crime, less random fight from street argument than hanoi, but nothing a Viet cant handle
..."""  # your data here

sentences = sent_tokenize(data)  # split the text into sentences

location_safety_dict = {}

for sentence in sentences:
    doc = nlp(sentence)
    for ent in doc.ents:
        if ent.label_ == 'GPE':  # GPE is Geo-Political Entity, used by spaCy for locations
            location_safety_dict[ent.text] = sentence

for location, comment in location_safety_dict.items():
    print(f'Location: {location}\nComment: {comment}\n')
