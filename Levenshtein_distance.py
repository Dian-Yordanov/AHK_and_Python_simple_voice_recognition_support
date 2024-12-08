import Levenshtein

def median_sentence(sentences):
    num_sentences = len(sentences)
    
    # Calculate pairwise distances
    distances = [[Levenshtein.distance(sentences[i], sentences[j]) for j in range(num_sentences)] for i in range(num_sentences)]
    
    # Sum the distances for each sentence
    total_distances = [sum(distances[i]) for i in range(num_sentences)]
    
    # Find the sentence with the smallest total distance
    median_index = total_distances.index(min(total_distances))
    return sentences[median_index]

# Example sentences
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "A swift auburn fox leaps over the sleepy dog.",
    "The fast brown fox jumps over the tired dog."
]

sentence = [
    "2021 albums 3 ff",
    "2021 3albums 4 ff" ,
    "2020 albums 3 bb ff",
]

median = median_sentence(sentences)
print("The median sentence is:", median)

median = median_sentence(sentence)
print("The median sentence is:", median)
