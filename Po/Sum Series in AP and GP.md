# Sum Series in AP and GP
UID: 202301111935
Tags: #🌱 
Links: [[Computational Thinking]]

----
## Arithmetic Progression series
Sum of arithmetic series $S_n$, by starting with the first term $a$ and successively adding the common difference $d$
$$S_n=T_1+T_2+T_3...+T_n$$
$$\implies S_n=a+(a+d)+(a+2d)+...+[a+(n-1d)]$$
Writing in terms of reverse order...
$$S_n=[a(n-1)d]+...+(a+2d)+(a+d)+a$$
Summing up both identities...
$$2S_n=n[2a+(n-1)d]$$
$$\therefore S_n=\frac{n}{2}[2a+(n-1)d]=\frac{n}{2}[a+a_n]$$
+ Where $a_n=a+(n-1)d$

----
Geometric Progression Series
Sum of arithmetic series $S_n$, by starting with the first term $a$ and successively multiplying the common ratio $r$
$$S_n=T_1+T_2+T_3...+T_n$$
$$\implies S_n=a+ar+ar^{2+...+ar^{(n-1)}},\;r\neq1$$
Multiplying both sides by r...
$$rS_n=ar+ar^2+ar^3+...+ar^n$$

| For r>1, taking the difference between the two results: | For r<1, taking the difference between the two results  |     |
| ------------------------------------------------------- | ------------------------------------------------------- | --- |
| $$(r-1)S_n=a(r^{n-1)\implies}S_n=\frac{a(r^n-1)}{r-1}$$ | $$(1-r)S_n=a(1-r^{n)\implies}S_n=\frac{a(1-r^n)}{1-r}$$ |     |
|                                                         |                                                         |     |



