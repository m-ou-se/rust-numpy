
import rust_ext
import numpy as np

a = np.array([1.0, 2.0])
rust_ext.mult(3, a)
print(a)
