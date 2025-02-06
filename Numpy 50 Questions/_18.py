# 18. Create a checkerboard pattern using NumPy’s tile function.
import numpy as np
chekerboard = np.tile([[0,1],[1,0]] ,(4,4))
print(chekerboard)
