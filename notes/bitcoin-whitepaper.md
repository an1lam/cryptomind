[Link](https://bitcoin.org/bitcoin.pdf)
Author: Satoshi Nakamoto

# Relevant Background
- Ralph Merkle's [Protocols for public key cryptosystems](http://www.merkle.com/papers/Protocols.pdf)
  on Merkle Trees.
- Adam Back's [Hashcash](http://www.hashcash.org/papers/hashcash.pdf) for the original description
  of proof-of-work.
- H. Massias, X.S. Avila, and J.-J. Quisquater's 
  [Design of a secure timestamping service with minimal trust requirements](http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=DEB67A072F93E39B60CE2E9436A2815F?doi=10.1.1.13.6228&rep=rep1&type=pdf)
  for how timestamp servers work.
- Wei Dai's [Bmoney](http://www.weidai.com/bmoney.txt) for the requirement that transactions
  be publicly announced.

# Terms Not Covered By Background
- Double-Spending Problem
- Binomial Random Walk
- Gambler's Ruin
- Poisson Distribution

# Thoughts
- Interesting that lowering the cost of transactions was an original goal of Bitcoin.
- You can get rough anonymity with Bitcoin by switching keys for every transaction.

# Questions
- How does proof-of-work difficulty increase?
- How do nodes "catch up" when they fall behind? Nodes will jump to the longest branch of
  transactions.
- How does the mining algorithm decide whether to add an incentive to a transaction?
- Where does the q<sub>z</sub> equation come from?
- How does having more nodes in the network work on one chain make it "win"?
- Can two nodes ever disagree on which transactions belong in a block or on the order they belong?

# Summary
The Bitcoin White Paper describes how Bitcoin solves the double-spending problem by trading a
trusted third-party for verification by many nodes in the network. Bitcoin solves this problem by
validating transactions based on proof-of-work. Nodes "in the network" validate transactions by
computing a random string which, attached to the existing transaction bytes, produces a hash value
with a certain number of leading zeroes. Because nodes in the network also attach new blocks to the
longest chain of blocks in the network, an attacker must own >50% of the network in order to create
a fraudulent block.
