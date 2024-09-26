import numpy as np
values = [0,1,2,3,4,5,8]
frequency = [12,17,21,24,20,3,3]

extend_list = np.repeat(values,frequency)
print(extend_list.tolist())