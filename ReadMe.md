# Valid Sentence Generator

Using common lexical rules of the English language, generates a random grammatical sentence from a set of passed in words. 

Can be customized for different languages by editing the rules specified in `rules.txt` along with the set of possible words in `menu.txt`.

### `rules.txt`

All lexical rules must be defined as follows to be considered valid:

$A \space\text{->}\space {A_1} \space {A_2} \space ... \space {A_n}$

where $A$ defines the result, and $A_1 \space A_2 \space ... \space A_n$ defines the members who form the result.

e.g., 

$\text{S -> NP VP}$ defines the case in which a sentence is composed of a noun phrase and verb phrase. 

exaxmple `rules.txt`:

```plaintext
S -> NP VP
S -> SV S
NP -> Det N
N -> Adj N
.
.
.
```

### `menu.txt`

All words should be on their own line, followed by their lexical class, separated by a comma.

e.g., `menu.txt`:

```plaintext
this, Det
is, Det
an, Det
example, Adj
file, N
.
.
.
```
