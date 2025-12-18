# Valid Sentence Generator

Using common lexical rules of the English language, generates a random grammatical sentence from a set of passed in words. 

Can be customized for different languages by editing the rules specified in `rules.txt` along with the set of possible words in `menu.txt`.

### `rules.txt`

All lexical rules must be defined as follows to be considered valid:

$A \space\text{->}\space {A_1} \space {A_2} \space ... \space {A_n}$

where $A$ defines the result, and $A_1 \space A_2 \space ... \space A_n$ defines the members who form the result.

e.g., 

$\text{S -> NP VP}$ defines the case in which a sentence is composed of a noun phrase and verb phrase. 

### `menu.txt`

All words should be on their own line with a `,` as a delimeter

e.g., `menu.txt`:

```plaintext
this,
is,
an,
example,
file
```
