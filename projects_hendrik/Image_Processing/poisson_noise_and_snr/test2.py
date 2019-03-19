import numpy as np
all_polys = [[5,6],
             [8,9]]
all_polys = np.append(all_polys,[ [1,2] ], axis=0)
print(all_polys)
#Output=
#all_polys = [[5,6],
#             [8,9],
#             [1,2]]