Authors: Gerald J. Popek & Charles S. Kline  
[Link](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.127.5172&rep=rep1&type=pdf)  

# Background
- Diffie Hellman and RSA encryption algorithms.

# Notes
## Introduction
- Networks introduce new security challenges because we can't trust the hardware on which our
  communications travel.

## Encryption Algorithms
- Ideal encryption algorithms produce encrypted text with flat n-gram probability distributions. For
  any given input T, it's no more likely that my encryption algorithm produces "foo" than it is that
  it produces "bar".
- Diffie and Hellman introduced encryption by key pairs where `E = F(D, K)` and `D = F'(D, K')` (`F`
  and `F'` can be applied in the reverse order) and `K'` is not derive-able from `K`. This is
  typically called public-key encryption because it allows us to widely distribute one of `K` or
  `K'`.
- The origin of the term block chain may be this paper. The paper describes Feistel's "block
  chaining" where each encrypted block includes a chunk of the prior encrypted block.
- Stream ciphers have the bad property that `F[i] = F(S[i], F[i-1])`. This means we can't decrypt
  select sections of an encrypted text.

## Encryption Applications
- Digital signatures should be unforgeable, authentic, un-repudiable, cheap, and convenient.
- Any system that stores keys is vulnerable. It's vulnerabilities all the way down.

## Authentication
- Zero-trust authentication requires that two users who don't trust each other be able to verify
  each other's identities. User B can verify user A's identity with the following exchange:
  1) B sends A a random unique data item, a timestamp for example.
  2) A encrypts the random data item and sends the ciphertext to B.
  3) B decrypts A's authentication message using A's key and compares it with his original
     cleartext. If they match, A is A (hehe).

## Key Management
- Safely distributing keys is a bootstrapping problem: how can we distribute keys to create a safe
  channel in a safe channel? Get around this by all recipients have a secure channel to the
  distribution center.
- Encrypting and reencrypting at gateway points sounds insecure. What prevents a man-in-the-middle
  attack on the gateway?

![Public-Key Distribution Diagram](https://cl.ly/021b1z2y0A1d)
*Key distribution and conversation establishment in a public-key algorithm.*

- They don't mention this, but another advantage of the public-key algorithm is that the KDC can't
  man-in-the-middle A and B's communication.
- Public-key encrypted algorithms do fan-out the security problem to all the clients. The KDC is a
  trusted third party, but that trust may be more deserved. For example, anyone who gets into my
  Compass laptop can access my RSA private key.
- I disagree with their playing down of the KDC's ability to listen in on private communications
  when using conventional key distribution.

## Levels of Integration
- End-to-end encryption is where we treat the user as A and the receiving program (regardless of
  where it's running) as B.
- The fact that `G(F(F(G(c)))) = c` for all used encryption algorithms is underratedly awesome.
- End-to-end encryption prevents abstraction leaks - for better or worse. For example, if I encrypt
  user input cleartext in my application and then want to transmit it over the network, I can't
  trust that my communication layer will buffer on newline.

## Encryption Protocols
- Mentions a bunch of abstract questions that I need to see concrete examples of.

## Confinement

# Questions
- How to intuitively explain the desire for the probability distribution of n-grams to be as flat as
  possible?
- Why are encryption algorithms excellent error detection mechanisms?
- Why do perfect ciphers requires "keys of length equal to the data they encode"?
- What do they mean when they talk about "error detection"? What creates these errors? Is it bad
  ordering over the network?
- How does encryption prevent man-in-the-middle replay attacks?
- How does encryption with check bits work? How does the recipient know what check bits to expect?
- Why can't we copy the conventional key algorithm for distributing public keys and eliminate the
  two messages between B and the KDI? Can't the KDI include in its reply A's public key encrypted
  using B's public key?
