import random

filename="combined_diatrics_input_IASTcompliant.txt" #input file name which contains list of words

corpusString = open(filename, "r", encoding="utf-8").read()
corpus =corpusString.split()

print ("corpus type", type(corpus) )

print ("corpus:\n", corpus[10000:10005] )

max_char_length = 1000
filtered_corpus = [sample for sample in corpus if len(sample) <= max_char_length]

random_seed = 42  # Set the seed to any desired value
random.seed(random_seed)
random.shuffle(filtered_corpus)

split_ratio = 0.80
split_index = int(len(filtered_corpus) * split_ratio)

training_data = filtered_corpus[:split_index]
testing_data = filtered_corpus[split_index:]


# Open the file in write mode with UTF-8 encoding
with open(filename.split(".txt")[0]+"_train.txt", "w", encoding="utf-8") as file:
    # Iterate through the list and write each string to the file
    for item in training_data:
        file.write(item + "\n")  # Add a newline after each string

# Open the file in write mode with UTF-8 encoding
with open(filename.split(".txt")[0]+"_test.txt", "w", encoding="utf-8") as file:
    # Iterate through the list and write each string to the file
    for item in testing_data:
        file.write(item + "\n")  # Add a newline after each string


