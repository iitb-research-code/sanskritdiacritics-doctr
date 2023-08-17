import unicodedata

filename="combined_diatrics_input.txt" #input file name which contains list of words

corpusString = open(filename, "r", encoding="utf-8").read()

#vocabs = "".join(list(set(corpus)))

#print("vocabs: ", vocabs)


vocabString="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~°£€¥¢฿'(-0123456789:A[abcdeghijklmnoprstuvy|ñāēīōśū̥̄̐।॥ḍḥṁṃṅṇṛṣṭरचख़३ॾऍृेञलॻॉऴषॐॢ१य०ॽएा२ई।ग़७टऐय़॥तोदऽभुनओऒ-ठँ.ौ्८ॼझॠविःक़ी॰छॅॊऩऱ़थजशळङअऋखबफउ५फ़६ऊॲॆज़कढ़मूस॓इऔह॑ैगढॣधआड़९ं४डणपॄघऑऀँंःऄअआइईउऊऋऌऍऎएऐऑऒओऔकखगघङचछजझञटठडढणतथदधनऩपफबभमयरऱलळऴवशषसहऺऻ़ऽािीुूृॄॅॆेैॉॊोौ्ॎॏॐ॒॑॓क़ख़ग़ज़ड़ढ़फ़य़ॠॢॣ।॥०१२३४५६७८९॰ॱॲॳॴॵॶॷॸॹॺॻॼॽॾॿ"


vocab=x=[i for i in vocabString]
print("vocab", vocab)
#vocab = ['a', 'b', 'c', 'd', 'e']
#corpus = ['apple', 'bad', 'cake', 'deep', 'elephant', 'fence', 'dog']

corpus =corpusString.split()

print ("corpus type", type(corpus) )

print ("corpus:\n", corpus[100000:100005] )

updated_corpus = []
ood_corpus = []

#unicodedata.normalize("NFKD", string_)

for word in corpus:
    #word=unicodedata.normalize("NFKD", word) #print("word", word)
    valid = True
    for char in word:
        if char not in vocab:
            #print("char not in vocab",char)
            valid = False
            break
    if valid:
        updated_corpus.append(word)
    else:
        ood_corpus.append(word)

# Printing the results
print("Original Corpus", len(corpus))
print("Updated Corpus:", len(updated_corpus))
print("OOD Corpus:", len(ood_corpus))

filename = "combined_diatrics_input_vocabcompliant.txt"

# Open the file in write mode with UTF-8 encoding
with open(filename, "w", encoding="utf-8") as file:
    # Iterate through the list and write each string to the file
    for item in updated_corpus:
        file.write(item + "\n")  # Add a newline after each string


filename1 = "combined_diatrics_input_vocabNonComp.txt"

# Open the file in write mode with UTF-8 encoding
with open(filename1, "w", encoding="utf-8") as file:
    # Iterate through the list and write each string to the file
    for item in ood_corpus:
        file.write(item + "\n")  # Add a newline after each string

filename2="combined_diatrics_input_vocabcompliant.txt" #input file name which contains list of words

mycorpus = open(filename2, "r", encoding="utf-8").read()

myvocabs = "".join(list(set(mycorpus)))

print("myvocabs: ", myvocabs)

print(set(myvocabs).difference(set(vocabString)))





