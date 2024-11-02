import threading
import time
import LFPM_Algorithm_in_def as lfpm

exitFlag = 0


class AlgorithmThread(threading.Thread):
    def __init__(self, threadID, name, fr_table, text, pattern, word_len, cut):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.fr_table = fr_table
        self.text = text
        self.pattern = pattern
        self.word_len = word_len
        self.cut = cut

    def run(self):
        # print("Starting preprocessing in " + self.name)
        index_min = lfpm.preprocessing_ph1(self.fr_table, self.pattern, self.word_len)
        windows, windows_num = lfpm.preprocessing_ph2(self.text, self.pattern, index_min, self.word_len)
        # print("window_index is:" + str(windows))
        # print("num_window is:" + str(windows_num))

        # print("Starting Matching in " + self.name)
        index_match = lfpm.matching(self.text, self.pattern, windows, windows_num, self.word_len)
        new_match = []

        if self.threadID == 1:
            new_match = index_match
        else:
            for item in index_match:
                new_match.append(item + self.cut)

        print("match_index from {1} is {0} ".format(str(new_match), self.name))
        # print("match_num is:" + str(len(index_match)))

        return new_match


if __name__ == '__main__':
    main_string = 'CCCCAGACTAAAAGTCTCGGGGATTAACGCGTAAATTTAGTGAAAGTAAAGTAGTCCTAAGTACAGTGATGAGTGAAAGTAAAATAATTAACGCGTAGTACATCCAGTATACAGTACCCCAAGTAAGCAGTAGCTTTAGTAGGCCCCCAAGTAAGTAATTTTTTCCCCAGGGGGGGGGGAAATTCCCCAGACTAGTGTCGGGTAACGTAGTGACCTGATGAAAGCCTAAGTACAAAGTATTAACGCGTACAGTAGGGTAACGTAAAAATGGGAAATTTTGGTTAAAAAAAAAAAGTGATGTAATTTTTTAGCTTGGTAGTGTACCAGTAGTACGATAGTACAGTAGTCAGTAGTAGTAAGCCGTACGGGTATAATATAAAATATATGCGCGCAGAGACTCGGGTAACGTATTAGTCCGTAAAGGGTTTTTTTTTTTAAAAAGGCGTAGATAGCAGTAGAGAGAGGACACACACACACTTTTTGTAGCTAGTGATGATGAT'
    main_pattern = 'CCCCAAGTAA'
    alphabet = ['A', 'C', 'G', 'T']
    len_word = 4

    frequency_table = lfpm.create_freq_table(alphabet, len_word)
    frequency_table = lfpm.fill_freq_table(main_string, frequency_table, len_word)

    start_time = time.time()

    x = int(len(main_string) / 2)
    str1 = main_string[:x]
    str2 = main_string[x:]
    str3 = main_string[x - len(main_pattern) + 1:x + len(main_pattern) - 1]

    # Create new threads
    thread1 = AlgorithmThread(1, "Thread-1", frequency_table, str1, main_pattern, len_word, x)
    thread2 = AlgorithmThread(2, "Thread-2", frequency_table, str2, main_pattern, len_word, x)
    thread3 = AlgorithmThread(3, "Thread-3", frequency_table, str3, main_pattern, len_word, x - len(main_pattern) + 1)

    # Start new Threads
    match1 = thread1.start()
    match2 = thread2.start()
    match3 = thread3.start()

    print("\nExiting Main Thread")

    print("--- totally in %s seconds ---" % (time.time() - start_time))
