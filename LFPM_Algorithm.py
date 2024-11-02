import time

start_time = time.time()

sigma = ['A', 'C', 'G', 'T']
word_len = 4

freq_table = []

# creating the frequency table
# from itertools import product
# res = list(product(('A', 'C', 'G', 'T'), repeat=8))
for i in range(len(sigma)):
    for j in range(len(sigma)):
        for p in range(len(sigma)):
            for q in range(len(sigma)):
                freq_table.append([sigma[i], sigma[j], sigma[p], sigma[q], 0])


count = 0
REF_string = 'AGCCCAACATTTAAGTTTAAAAATCAAGCGTAAAATACAGAAGCTGGAAGCA'
REF_len = len(REF_string)


# filling the frequency table
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


t = REF_string
n = REF_len
p = 'AAGCGTA'
m = len(p)

# PREPROCESSING PHASE ==> step 1
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


# PREPROCESSING PHASE ==> step 2
count = min_index
num_window = 0
window_index = []

while count <= n - (m - min_index):
    if t[count: count + word_len] == p[min_index: min_index + word_len]:
        window_index.append(count - min_index)
        num_window += 1
    count += 1


# MATCHING PHASE
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
        if p[c:c + w - 1] != t[s + c: s + c + w - 1]:
            break
        c = c + w
    if c == m:
        match_index.append(s)
        num_match += 1
    count += 1

print(match_index)

print("--- %s seconds ---" % (time.time() - start_time))


