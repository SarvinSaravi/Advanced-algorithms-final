# Algorithm 1 FLPM Algorithm
import time

start_time = time.time()
text = "CCCCAGACTAAAAGTCTCGGGGATTAACGCGTAAATTTAGTGAAAGTAAAGTAGTCCTAAGTACAGTGATGAGTGAAAGTAAAATAATTAACGCGTAGTACATCCAGTATACAGTACCCCAAGTAAGCAGTAGCTTTAGTAGGCCCCCAAGTAAGTAATTTTTTCCCCAGGGGGGGGGGAAATTCCCCAGACTAGTGTCGGGTAACGTAGTGACCTGATGAAAGCCTAAGTACAAAGTATTAACGCGTACAGTAGGGTAACGTAAAAATGGGAAATTTTGGTTAAAAAAAAAAAGTGATGTAATTTTTTAGCTTGGTAGTGTACCAGTAGTACGATAGTACAGTAGTCAGTAGTAGTAAGCCGTACGGGTATAATATAAAATATATGCGCGCAGAGACTCGGGTAACGTATTAGTCCGTAAAGGGTTTTTTTTTTTAAAAAGGCGTAGATAGCAGTAGAGAGAGGACACACACACACTTTTTGTAGCTAGTGATGATGAT"
pattern = "TTTCG"

n = len(text)
m = len(pattern)


# Input: Text and pattern
# Output: The number of windows identified in this phase and their start indexes.
def preprocessing_flpm():
    num_window = 0
    window_index = []
    for count in range(n - m + 1):
        if text[count] == pattern[0] and text[count + m - 1] == pattern[m - 1]:
            window_index.append(count)
            num_window = num_window + 1
    return num_window, window_index


# Input: The number of windows identified in the preprocessing phase and their start indexes.
# Output: The start index for all occurrences of pattern p in
def matching_flpm(num_window, window_index):
    num_match = 0
    match_index = []
    for count in range(num_window):
        s = window_index[count]
        c = 1
        while c <= m - 2:
            if pattern[c] != text[s + c]:
                break
            c = c + 1
        if c == m - 1:
            match_index.append(s)
            num_match = num_match + 1
    return num_match, match_index


print("MAIN TEXT : {0}".format(text))
print("MAIN TEXT LENGTH: {0}".format(str(n)))
print("MAIN PATTERN : {0}".format(pattern))
print("MAIN PATTERN LENGTH: {0}".format(str(m)))

print("FLMP_ALGORITHM ==> Start Preprocessing Phase ===================================>")
num_window, window_index = preprocessing_flpm()
print("window_index is:" + str(window_index))
print("num_window is:" + str(num_window))

print("FLMP_ALGORITHM ==> Start Matching Phase ========================================>")
num_match, match_index = matching_flpm(num_window, window_index)
print("match_index is:" + str(match_index))
print("num_match is:" + str(num_match))

print("--- %s seconds ---" % (time.time() - start_time))
