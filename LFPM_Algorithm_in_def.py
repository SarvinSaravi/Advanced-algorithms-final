import time


# creating the list of frequency table
def create_freq_table(sigma, word_len):
    # from itertools import product
    # res = list(product(('A', 'C', 'G', 'T'), repeat=word_len))
    freq_table = []
    for i in range(len(sigma)):
        for j in range(len(sigma)):
            for p in range(len(sigma)):
                for q in range(len(sigma)):
                    freq_table.append([sigma[i], sigma[j], sigma[p], sigma[q], 0])
    return freq_table


# Input:The string of reference and list of frequency table and word length of problem
# Output:The fill table with computed word frequency.
# filling the frequency table
def fill_freq_table(ref_str, freq_table, word_len):
    REF_string = ref_str
    REF_len = len(ref_str)
    count = 0
    while count <= (REF_len - word_len):
        row_count = 0
        col_count = 0
        w = REF_string[count:count + word_len]
        while col_count < word_len:
            # if w[col_count] == 'A':
            if w[col_count] == 'C':
                row_count += 1 * (4 ** (word_len - col_count - 1))
            if w[col_count] == 'G':
                row_count += 2 * (4 ** (word_len - col_count - 1))
            if w[col_count] == 'T':
                row_count += 3 * (4 ** (word_len - col_count - 1))

            col_count += 1
        freq_table[row_count][word_len] += 1
        count += 1
    return freq_table


# Input: The list of frequency table
# and string pattern p stored in the string of p[0..m−1]
# and word length
# Output: The first index for possible window occurrences in pattern p. (least frequency word in pattern)
# PREPROCESSING PHASE ==> step 1
def preprocessing_ph1(freq_table, pattern, word_len):
    p = str(pattern)
    m = len(p)
    count = 0
    min_value = 117000  # infinite number
    min_index = -1
    while count <= m - word_len:
        row_count = 0
        col_count = 0
        w = p[count: count + word_len]
        while col_count < word_len:
            # if w[col_count] == 'A':
            if w[col_count] == 'C':
                row_count += 1 * (4 ** (word_len - col_count - 1))
            if w[col_count] == 'G':
                row_count += 2 * (4 ** (word_len - col_count - 1))
            if w[col_count] == 'T':
                row_count += 3 * (4 ** (word_len - col_count - 1))

            col_count += 1
        if freq_table[row_count][word_len] < min_value:
            min_value = freq_table[row_count][word_len]
            min_index = count
        count += 1

    return min_index


# Input: string Text t and string pattern p stored in the string arrays of t[0..n−1] and p[0..m−1]
# and min index that represent index of least frequency word in pattern
# and word length
# Output: Array of first index for possible windows occurrences of pattern p in text t
# and length of this array
# PREPROCESSING PHASE ==> step 2
def preprocessing_ph2(text, pattern, min_index, word_len):
    t = str(text)
    n = len(t)
    p = str(pattern)
    m = len(p)
    count = min_index
    num_window = 0
    window_index = []

    while count <= n - (m - min_index):
        if t[count: count + word_len] == p[min_index: min_index + word_len]:
            window_index.append(count - min_index)
            num_window += 1
        count += 1

    return window_index, num_window


# Input: string Text t and string pattern p stored in the string arrays of t[0..n−1] and p[0..m−1]
# and array of first index for possible windows occurrences of pattern p in text t
# and length of this array
# and word length
# Output: The first indexes for all occurrences of pattern p in text t.
# MATCHING PHASE
def matching(text, pattern, window_index, num_window, word_len):
    t = str(text)
    n = len(t)
    p = str(pattern)
    m = len(p)
    count = 0
    num_match = 0
    k = m % word_len
    match_index = []

    while count < num_window:
        s = window_index[count]
        c = 0
        w = word_len
        while c <= m - 1:
            if c > m - word_len:
                w = k
            if p[c:c + w] != t[s + c: s + c + w]:
                break
            c = c + w
        if c == m:
            match_index.append(s)
            num_match += 1
        count += 1

    return match_index


if __name__ == '__main__':
    main_string = 'CCCCAGACTAAAAGTCTCGGGGATTAACGCGTAAATTTAGTGAAAGTAAAGTAGTCCTAAGTACAGTGATGAGTGAAAGTAAAATAATTAACGCGTAGTACATCCAGTATACAGTACCCCAAGTAAGCAGTAGCTTTAGTAGGCCCCCAAGTAAGTAATTTTTTCCCCAGGGGGGGGGGAAATTCCCCAGACTAGTGTCGGGTAACGTAGTGACCTGATGAAAGCCTAAGTACAAAGTATTAACGCGTACAGTAGGGTAACGTAAAAATGGGAAATTTTGGTTAAAAAAAAAAAGTGATGTAATTTTTTAGCTTGGTAGTGTACCAGTAGTACGATAGTACAGTAGTCAGTAGTAGTAAGCCGTACGGGTATAATATAAAATATATGCGCGCAGAGACTCGGGTAACGTATTAGTCCGTAAAGGGTTTTTTTTTTTAAAAAGGCGTAGATAGCAGTAGAGAGAGGACACACACACACTTTTTGTAGCTAGTGATGATGAT'
    main_pattern = 'TAAAA'
    alphabet = ['A', 'C', 'G', 'T']
    len_word = 4

    frequency_table = create_freq_table(alphabet, len_word)
    frequency_table = fill_freq_table(main_string, frequency_table, len_word)

    start_time = time.time()
    # start = datetime.now()
    print("MAIN TEXT : {0}".format(main_string))
    print("MAIN TEXT LENGTH: {0}".format(str(len(main_string))))
    print("MAIN PATTERN : {0}".format(main_pattern))
    print("MAIN PATTERN LENGTH: {0}".format(str(len(main_pattern))))

    print("LFPM_ALGORITHM ==> Start Preprocessing Phase ===================================>")
    index_min = preprocessing_ph1(frequency_table, main_pattern, len_word)
    windows, windows_num = preprocessing_ph2(main_string, main_pattern, index_min, len_word)
    print("window_index is:" + str(windows))
    print("num_window is:" + str(windows_num))

    print("LFPM_ALGORITHM ==> Start Matching Phase ========================================>")
    index_match = matching(main_string, main_pattern, windows, windows_num, len_word)
    print("match_index is:" + str(index_match))
    print("match_num is:" + str(len(index_match)))

    print("--- totally in %s seconds ---" % (time.time() - start_time))
    # print("--- totally %s seconds ---" % (datetime.now() - start))
