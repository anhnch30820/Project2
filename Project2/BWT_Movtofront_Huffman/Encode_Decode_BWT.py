import os







class suffix:
    def __init__(self):
        self.index = 0
        self.rank = [0, 0]


    # This is the main function that takes a
    # string 'txt' of size n as an argument,
    # builds and return the suffix array for
    # the given string
    def buildSuffixArray(self, txt):
        txt = txt + "$"
        n = len(txt)
        # A structure to store suffixes
        # and their indexes
        suffixes = [suffix() for _ in range(n)]

        # Store suffixes and their indexes in
        # an array of structures. The structure
        # is needed to sort the suffixes alphabatically
        # and maintain their old indexes while sorting
        for i in range(n):
            suffixes[i].index = i
            suffixes[i].rank[0] = (ord(txt[i]) -
                                   ord("a"))

            suffixes[i].rank[1] = (ord(txt[i + 1]) -
                                   ord("a")) if ((i + 1) < n) else -1

        # Sort the suffixes according to the rank
        # and next rank
        suffixes = sorted(
            suffixes, key=lambda x: (
                x.rank[0], x.rank[1]))
        # for i in range(n):
        #     print(suffixes[i].rank)
        # At this point, all suffixes are sorted
        # according to first 2 characters. Let
        # us sort suffixes according to first 4
        # characters, then first 8 and so on
        ind = [0] * n  # This array is needed to get the
        # index in suffixes[] from original
        # index.This mapping is needed to get
        # next suffix.
        k = 4
        while (k < 2 * n):

            # Assigning rank and index
            # values to first suffix
            rank = 0
            prev_rank = suffixes[0].rank[0]
            suffixes[0].rank[0] = rank
            ind[suffixes[0].index] = 0

            # Assigning rank to suffixes
            for i in range(1, n):

                # If first rank and next ranks are
                # same as that of previous suffix in
                # array, assign the same new rank to
                # this suffix
                if (suffixes[i].rank[0] == prev_rank and
                        suffixes[i].rank[1] == suffixes[i - 1].rank[1]):
                    prev_rank = suffixes[i].rank[0]
                    suffixes[i].rank[0] = rank

                # Otherwise increment rank and assign
                else:
                    prev_rank = suffixes[i].rank[0]
                    rank += 1
                    suffixes[i].rank[0] = rank
                ind[suffixes[i].index] = i
                # print(ind)

            # Assign next rank to every suffix
            for i in range(n):
                # print(suffixes[i].rank)
                nextindex = suffixes[i].index + k // 2
                suffixes[i].rank[1] = suffixes[ind[nextindex]].rank[0] if (nextindex < n) else -1
            # for i in range(n):
            #     print(suffixes[i].rank)

            # Sort the suffixes according to
            # first k characters
            suffixes = sorted(
                suffixes, key=lambda x: (
                    x.rank[0], x.rank[1]))

            k *= 2

        # Store indexes of all sorted
        # suffixes in the suffix array
        suffixArr = [0] * n

        for i in range(n):
            suffixArr[i] = suffixes[i].index

        # Return the suffix array
        return "".join(txt[v - 1] for v in suffixArr)




    def compress(self):
        f_i = open("input.txt", 'r')
        output_path = "input_encode_BWT.txt"
        w_e = open(output_path, "w")

        s = f_i.read()
        encode = self.buildSuffixArray(s)
        print("Compressed successful BWT")
        w_e.write(encode)

        return output_path

    def FMIndex(self, bwt):
        fm = [{c: 0 for c in bwt}]
        # print(fm)
        for c in bwt:
            row = {symbol: count + 1 if (symbol == c) else count for symbol, count in fm[-1].items()}
            fm.append(row)
        offset = {}
        N = 0
        for symbol in sorted(row.keys()):
            offset[symbol] = N
            N += row[symbol]

        return fm, offset

    # bwt = "annb$aa"
    # FM, Offset = FMIndex(bwt)
    # print ("%2s,%2s,%2s,%2s" % tuple([symbol for symbol in sorted(Offset.keys())]))
    # for row in FM:
    #     print ("%2d,%2d,%2d,%2d" % tuple([row[symbol] for symbol in sorted(row.keys())]))
    # print(Offset)

    def recoverSuffix(self, i, BWT, FMIndex, Offset):
        suffix = ''
        c = BWT[i]
        predec = Offset[c] + FMIndex[i][c]
        suffix = c + suffix
        while (predec != i):
            c = BWT[predec]
            # print(predec)
            predec = Offset[c] + FMIndex[predec][c]
            suffix = c + suffix
        return suffix

    # recall that the FM-index that we built was "annb$aa", the BWT of "banana$"
    def inver_BWT(self, bwt):
        FM, Offset = self.FMIndex(bwt)
        i = bwt.index("$")
        s = self.recoverSuffix(i, bwt, FM, Offset)
        return s[:-1]

    def decompress(self, input_path):
        output_path = input_path[:-4] + "_BWT.txt"
        f_d = open(input_path, 'r')
        w_d = open(output_path, 'w')


        s = f_d.read()
        decode = self.inver_BWT(s)
        w_d.write(decode)
        print("Decompressed successful BWT")
        return output_path





# a = BWT()
# a.compress(100)
# f_d = open("input_encode_BWT.txt", "r")
# print(len(f_d.read()))

# a = BWT()
#
# encode_path = a.compress(100)
# q = a.decompress(100)


