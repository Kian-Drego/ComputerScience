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

![](../Assets/Pasted%20image%2020250823011126.png)

## Asymmetric Cryptography
1) Both sender and receiver generate private and public key using an algorithm. The public key can only be generated and verified using the private key.
	a) public key - alphanumeric text, shared with others
	b) private key - alphanumeric text, kept to oneself
2) The sender sends their public key to the recipient which the recipient uses to encrypt their message into ciphertext
3) The recipient sends the ciphertext to the sender, who can use their private key to decrypt the message, which was encrypted with their own public key.
- If the recipient want to receive a message from the sender, they need to complete the same process, first sending their own public key
![](../Assets/Pasted%20image%2020250823012153.png)

## Symmetric Cryptography vs Asymmetric Cryptography

| Aspects          | Symmetric                                                                                                              | Asymmetric                                                                                       |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Keys             | One shared secret key for both encryption and decryption                                                               | Two keys: a public key for encrytion and a private key for dectryption                           |
| Efficiency       | More efficient for encrypting and decrypting large amounts of data due to simpler algorithms.                          | Less efficient for bulk data encrytion because of more complex algorithms and longer key lenghts |
| Key Distribution | Difficult to securely distribute the shared secret key, often requiring additional mechanisms (eg. physical exchange). | Public keys can be freely distributed, while private keys must be kept confidential              |
| Security         | Susceptible to key compromise if the secret key is exposed.                                                            | Offers greater security as the private key never leaves the possession of the owner              |

## Quantum Cryptography
- Information is represented in qubits, which can be 1, 0, or both 1 and 0 at the same time
- Each qubit is represented by a photon (unit of light energy) pointing in a specific direction based on its value
- Photons travel between a sender and recipient via fibre optic cable
- Also requires a non-quantum "classical" mode of electronic communication
- Data is transmitted as a stream of photons all in a particular order and orientation
- Any attempt to access this data while being transmitted maker alters the message.
- It is theoretically impossible to intercept a transmission protected by quantum cryptography

| Pros                                                                       | Cons                                                                      |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Security based on laws of physics rather than algorithms, so highly secure | Very expensive -requires specialized equipment and fibre optic connection |
| Unhackable                                                                 | One works over short disances                                             |
| Eavesdropping can be detected                                              | Hight error rate during transmission (new technology)                     |
|                                                                            | Can be used by criminals to hide data transmissions                       |

## Protocols (SSL/TLS)
- SSL - Secure Sockets Lays
- TLS - Transport Layer Security
- Process used by web browser to encrypt communication between browser and a server
- Confirms identity of client and server
- Prevents hackers from interception traffic between client and server
- TLS is newer and more secure than SSL

### SSL/TLS Steps
1) Client (on a web browser) tries to access a website which uses SSL/TLS (a handshake)
2) Websites' server receiver connection and responds with a digital certificate, which contain s a public key and is validated by a certificate authority.
3) The client's browser validates the authenticity of the digital certificate.
4) The browser generates a key for the current session using the public key, which is sent back to the server.
5) The server uses its private key (which is used to generate the public key) to verify the session key
6) Any further communication between the client's browser and server is encrypted (hashed) through the use of this session key

## Digital Signatures
1) The sender uses a mathematical function called a has function to generate a hash value (also known as a message digest).
2) The result is an alphanumeric value of a fixed-length, which is then encrypted using the same private key.
3) This encrypted hash value is the digital signature and is then attached to unhashed version of the recipient.
4) The message is sent to the recipient.
5) The recipient decrypts the signature using their public key and puts the message they received through a hash function.
6) The recipient compares the contents of the decrypted signature and the hashed message and if they are equal, the transmission is authentic

![](../Assets/Pasted%20image%2020250825022914.png)

- Verifies the identity of a website 
- Contains website's public key, identifying information, Certificate Authority Information + CA private key, validity period, etc.
- Browser can verify digital certificate using CA public key 

Obtaining a Digital Certificate
1) A website makes an inquiry to a Certificate Authority (CA)
2) The CA investigates the website and any associated entities
3) The CA verifies the identity and security of the website and issues a public key
4) The website includes this public key in a certificate sent to a client attempting to connect using SSL
5) The client (browser) verifies the certificate using the CAs digital signature in the certificate and communicates with the website by encrypting data with this public key
