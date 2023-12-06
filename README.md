# Algorithm of Finding Prime Numbers

Change the N in `find_primes.py` to find primes in different range.

This repository was made to generate the datasets in https://www.kaggle.com/datasets/wellington36/prime-number/data


# Mercenne Primes Finded
A Mersenne number is of the form

$$M_n = 2^n - 1$$

We tested the primality of the first Mersenne numbers with the codes from this repository to the extent possible with some forms

|            | number      | digits | Miller-Rabin (k=1) | Miller-Rabin (k=1000) | Test with 150mi primes |
|------------|-------------|--------|--------------------|-----------------------|------------------------|
| $M_2$      | 3           | 1      | ✔️                  | ✔️                     | ✔️                      |
| $M_3$      | 7           | 1      | ✔️                  | ✔️                     | ✔️                      |
| $M_5$      | 31          | 2      | ✔️                  | ✔️                     | ✔️                      |
| $M_7$      | 127         | 3      | ✔️                  | ✔️                     | ✔️                      |
| $M_{13}$   | 8191        | 4      | ✔️                  | ✔️                     | ✔️                      |
| $M_{17}$   | 131071      | 6      | ✔️                  | ✔️                     | ✔️                      |
| $M_{19}$   | 524287      | 6      | ✔️                  | ✔️                     | ✔️                      |
| $M_{31}$   | 21474836    | 8      | ✔️                  | ✔️                     | ✔️                      |
| $M_{61}$   | 2305...3951 | 19     | ✔️                  | ✔️                     | ✔️                      |
| $M_{89}$   | 6189...2111 | 27     | ✔️                  | ✔️                     | ✔️                      |
| $M_{107}$  | 1622...8127 | 33     | ✔️                  | ✔️                     | ✔️                      |
| $M_{127}$  | 1701...5727 | 39     | ✔️                  | ✔️                     | ✔️                      |
| $M_{521}$  | 6864...7151 | 157    | ✔️                  | ✔️                     | ✔️                      |
| $M_{607}$  | 5311...8127 | 183    | ✔️                  | ✔️                     | ✔️                      |
| $M_{1279}$ | 1040...9087 | 386    | ✔️                  | ✔️                     | ✔️                      |
| $M_{2203}$ | 1475...1007 | 664    | ✔️                  | ✔️                     | ✔️                      |
| $M_{2281}$ | 4460...6351 | 687    | ✔️                  | ✔️                     | ✔️                      |
| $M_{3217}$ | 2591...5071 | 969    | ✔️                  | ✔️                     | ✔️                      |
| $M_{4253}$ | 1907...4991 | 1281   | ✔️                  | ✔️                     | ✔️                      |
| $M_{4423}$ | 2855...0607 | 1332   | ✔️                  | ✔️                     | ✔️                      |
