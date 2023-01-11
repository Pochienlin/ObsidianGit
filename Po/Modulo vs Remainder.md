# Modulo vs Remainder
UID: 202301112245
Tags: #🌱 
Links: [[Programming for CT]]

----
#### Different types of floor division
-   floored division, where the quotient is floored toward negative infinity and the remainder has the same sign as the divisor.
-   truncated division, where the quotient is truncated toward zero and the remainder as the same sign as the dividend.
-   Euclidean division, where the quotient is truncated in whichever direction leaves the remainder positive.

Example:
```python
import numpy as np
import math as m

print(np.remainder(-23,22)) # Gives 21, like python's native modulo
print(m.remainder(-23,22)) # Gives -1.0, by truncated division
```