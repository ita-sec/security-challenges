## DeFUNct Ransomware Write-up
### Description:
> Santa got infected by a ransomware! His elves managed to extract the public key, but couldn't break it. Help Santa decrypt his memos and save Christmas!
> 
> P.S: given files: *xmasctf-crypto2-file1.txt*, *xmasctf-crypto2-file2.enc*

### Solution:

Looking at the text file, there are 2 variables: *n* and *e.* The challenge is a public key, so the idea is to try and break the RSA.

I initially tried to factor n using [FactorDB](www.factordb.com). I found out n is in the format $n = p^2q^2$. This is uncommon, as n is usually in the format $n = pq$, because it is harder to break and easier to calculate *d*, where $ed \equiv 1 mod(\phi(n))$.

Exploiting that we know *p* and *q*, the only thing left is find out $\phi(n)$.

$$\phi(n) = \phi(p^ 2q^2)=\phi(p^2)\phi(q^2)=p(p-1)q(q-1)$$

Therefore, $d=modinv(e,p(p-1)q(q-1))$, which can be done in a few seconds. The decoded message is simply $decoded = encoded^d mod n$. After that, convert the decoded message from hex to ASCII:

>TODO
>----

>* Stop downloading RAM for the internet.
>* Remove yakuhito from the naughty kids list.
>* Drink all the milk; eat all the cookies
>* Do not forget the flag: X-MAS{yakuhito_should_n0t_b3_0n_th3_n@ughty_l1st_941282a75d89e080}

