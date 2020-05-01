from math import ceil, log2, inf
class SegmentTree:

    def __init__(self, array, operation, useful_value):
        self.useful_value = useful_value
        self.operation = operation
        # Size of segment_array is 2 ^ ceil(log(size)) * 2 - 1
        # Example for perfect size of 8 size is = 2^log(8) * 2 - 1 = 2^3 * 2 - 1 
        if len(array) > 0:
            segment_array_size = 2 ** ceil(log2(len(array))) * 2 - 1
        else:
            self.segment_array = []
            return

        self.segment_array = [None for x in range(segment_array_size)]

        # fill the array to bottom of segment_array

        for i in range(len(self.segment_array) // 2, len(self.segment_array) // 2 + len(array)):
            self.segment_array[i] = array[i - len(self.segment_array) // 2 ]
        # fill remaining entries with Useful value
        # Useful value vary depending on problem ex Min Query ST usefulvalue = -inf

        for i in range(i + 1, len(self.segment_array)):
            self.segment_array[i] = self.useful_value

        # Build from bottom up fasion so old values are ready
        for i in range(len(self.segment_array) // 2 - 1, -1, -1):
            self.segment_array[i] = self.operation(self.segment_array[2 * i + 1], self.segment_array[2 * i + 2])

        print(self.segment_array)

    @staticmethod
    def left(i):
        return 2 * i + 1

    @staticmethod
    def right(i):
        return 2 * i + 2

    @staticmethod
    def parent(i):
        if i == 0:
            return -1
        return ceil(i / 2) - 1

    def rangeQuery(self, l, r):
        # represent array[i] l_i and r_i are range the array[i] represents
        # l and r are actual range query l and r
        def helper(i, l, r, l_i, r_i):
            if l <= l_i <= r_i <= r:
                return self.segment_array[i]
            if r < l_i:
                return self.useful_value
            if l > r_i:
                return self.useful_value
            return self.operation(helper(SegmentTree.left(i), l, r, l_i, (l_i + r_i) // 2), helper(SegmentTree.right(i), l, r, (l_i + r_i) // 2 + 1, r_i))

        return helper(0, l, r, 0, len(self.segment_array) // 2)

    def update(self, i, value):
        logical_pos = len(self.segment_array) // 2 + i
        self.segment_array[logical_pos] = value 
        temp = logical_pos
        while temp != 0:
            parent = SegmentTree.parent(temp)
            self.segment_array[parent] = self.operation(self.segment_array[SegmentTree.left(parent)], self.segment_array[SegmentTree.right(parent)])
            temp = parent
        print(self.segment_array)

def main():
    array = []
    # st = SegmentTree(array, lambda x, y: min(x, y), useful_value=inf) # Min Range ST
    st = SegmentTree(array, lambda x, y: x + y, useful_value=0) # Min Range ST
    # st = SegmentTree(array, lambda x, y: min(x, y), useful_value=inf) # Max Range ST

    # st.update(0, -)
    for i in range(len(array)):
        for j in range(i, len(array)):
            print(i, j, st.rangeQuery(i, j))

    # st.update(0, 10)

if __name__ == '__main__':
    main()