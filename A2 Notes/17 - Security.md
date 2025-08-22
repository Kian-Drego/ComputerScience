# 17 - Security
- Symmetric Cryptography
- Asymmetric Cryptography
- Quantum Cryptography
- SSL & TLS
- Digital Signatures
- Digital Certificates

- One 7 - 10 marks on Paper 3

## Key Cryptography
- Ensures message is authentic
- Ensures message come from trusted source
- Ensures message wasn't altered during transmission
- Makes sure only the intended recipient can understand message
- Involves keys - strings of alphanumeric text used to decrypt and encrypt messages

## Symmetric Cryptography
- Requires text to be encrypted (plaintext), a secret key and an encryption algorithm
- secret key - random alphanumeric string

1) Input the secret key and plain text into the encryption algorithm to get your encrypted text, which should appear as a random set of numbers and letters (ciphertext).
2) Send the ciphertext to the recipient who should already have the same secret key and decryption algorithm.
3) The secret key and cipher text are input into the decryption algorithm to yield the original plaintext

- Main problem is securely sharing key between sender and recipient (key distribution problem)

![](Assets/Pasted%20image%2020250823011126.png)

## Asymmetric Cryptography
1) Both sender and receiver generate private and public key using an algorithm. The public key can only be generated and verified using the private key.
	a) public key - alphanumeric text, shared with others
	b) private key - alphanumeric text, kept to oneself
2) The sender sends their public key to the recipient which the recipient uses to encrypt their message into ciphertext
3) The recipient sends the ciphertext to the sender, who can use their private key to decrypt the message, which was encrypted with their own public key.
- If the recipient want to receive a message from the sender, they need to complete the same process, first sending their own public key
![](Assets/Pasted%20image%2020250823012153.png)

## Symmetric Cryptography vs Asymmetric Cryptography
![](Assets/Pasted%20image%2020250823012248.png)