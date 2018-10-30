import operator

class Heap():
    
    def __init__(self, array, is_max_heap=None, comparator=None):
        self.array = array[:]
        self.is_max_heap = is_max_heap
        self.comparator = comparator # операция больше / меньше
        self._build_heap()
                    
    def add(self, elem_with_priority):
        self.array.append(elem_with_priority)
        self._build_heap()
    
    def _build_heap(self):
        for i in range(1, len(self.array)):
            cur_index = i
            while cur_index > 0:
                parent_index = (cur_index - 1) // 2 # индекс родителя
                if self.comparator(self.array[cur_index], self.array[parent_index]): # сравнение
                    # меняем местами
                    self.array[cur_index], self.array[parent_index] = self.array[parent_index], self.array[cur_index]
                    cur_index = parent_index
                else:
                    break

    def cut_heap(self, n):
        self.array = self.array[:n]
                    
    def show_tree(self, total_width=33, fill=' '):
        # метод для поможет отлаживаться
        
        tree = self.array
        
        import math
        from io import StringIO
        output = StringIO()
        last_row = -1
        for i, n in enumerate(tree):
            if i:
                row = int(math.floor(math.log(i+1, 2)))
            else:
                row = 0
            if row != last_row:
                output.write('\n')
            columns = 2**row
            col_width = int(math.floor((total_width * 1.0) / columns))
            output.write(str(n).center(col_width, fill))
            last_row = row
        print (output.getvalue())
        print ('-' * total_width)
        print()
                    
class MinHeap(Heap):

    def __init__(self, array):
        super().__init__(array, False, operator.lt)

    def extract_minimum(self):
        min = self.array[0]
        self.array.pop(0)
        self._build_heap()
        return min






distance = np.sqrt( (self.X[:,0]-sex)**2 + (self.X[:,1]-age)**2 + (self.X[:,2]-pclass)**2 + 
                              (self.X[:,4]-fare)**2 + (self.X[:,5]-famsize)**2 + (self.X[:,6]-embarked_0)**2 + 
                               (self.X[:,7]-embarked_1)**2 + 
                               (self.X[:,8]-embarked_2)**2 )