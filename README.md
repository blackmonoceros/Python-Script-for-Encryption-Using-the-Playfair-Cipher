# Python-Script-for-Encryption-Using-the-Playfair-Cipher
The Playfair cipher is a digraph substitution cipher that encrypts pairs of letters. To use it, you first create a 5x5 table based on a secret keyword. Below is a Python implementation of the Playfair cipher.

Explanation of the Code:


Key Table Creation:


The key is processed to remove duplicates and replace the letter J with I.
A 5x5 table is created using the key and the remaining letters of the alphabet.


Text Preparation:


The plaintext is converted to uppercase, spaces are removed, and J is replaced with I.
The text is split into pairs of letters. If a pair is incomplete (e.g., a single letter), an X is added.


Encryption Rules:


If the letters are in the same row, they are replaced by the letters to their immediate right (wrapping around if necessary).
If the letters are in the same column, they are replaced by the letters immediately below them (wrapping around if necessary).
If the letters form a rectangle, they are replaced by the letters at the opposite corners of the rectangle.


Result:


The encrypted text is returned as the output.


Example:


For the key CIPHER and plaintext EXAMPLE TEXT, the script will generate the encrypted text according to the Playfair cipher rules.
