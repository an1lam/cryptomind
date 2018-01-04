[Link](https://www.igvita.com/2014/05/05/minimum-viable-block-chain/)
Author: Ilya Grigorik

# Important Terms
- Paxos
- 2-Phase Commit
- Sybil Attack

# Questions
- How does Bitcoin's proof-of-work system force redoing all work to change the chain?

# Summary
The minimum viable block chain requires:
- PKI infrastructure that guarantees integrity, authentication, and non-repudiation of
  transactions.
- A peer-to-peer network that allows participants to announce transactions to other participants on
  the network. The p2p network must be a connected graph (the paper doesn't mention this but it's
  true).
- A proof-of-work system that creates an asymmetry between the work required to create a
  transaction and the work required to verify one. This asymmetry serves to raise the cost of
  foul play.
- A block chaining system that allows blocks of transactions to be chained into an ordered linked
  list.
- Peers that track block announcements and merge them into their ledgers.

# Sections
## Securing Transactions with Triple-Entry Bookkeeping
The three main requirements for asynchronous transactions (Bob giving Alice a red stamp without her
giving him anything in exchange) are:
- Authentication: The participants are who they say they are.
- Non-Repudiation: Neither participant can later claim the transaction never happened.
- Integrity: Neither participant can modify the transaction after the fact.

## Securing Transactions with PKI
PKI satisfies our requirements when Alice signs her receipt with her private key because:
- Bob can prove Alice took his stamp because only she could sign the receipt.
- Alice signed the receipt so she clearly participated. Bob has no incentive to say he didn't
  participate.
- Bob can't fake or modify the transaction because he can't resign it after decrypting it.
Note that Alice could say "that's not my key". Connecting identity to keys is apparently the job of
a PKI.

## Balance = Sum(Transactions)
We can improve this by adding values for different stamp colors. This allows us to compute each
person's balance as a function of the ordered transactions that have occurred in the network.

## Double-Spending and Distributed Consensus
When we have >2 ledgers, it's possible to trick other parties by quickly offering the same receipt
to multiple other parties.

### Distributed Consensus Network Requirements
The hardest problems to solve are: achieving strong consistency (prevent partition tolerance),
working effectively without knowing about global state (number of participants and their statuses),
and protecting against Sybil attacks.

What if we relax the requirement of strong consistency?
Then we get the following requirements:
- Some ledges will be out-of-sync.
- The system must converge on a global ordering of transactions (linearizable).
- The system must have certain global invariants, no double-spending for example.
- The system must predictably resolve ledger conflicts.
- The system must be secure against Sybil-like attacks.

### Protecting Against Sybil Attacks
We need to make forging identities hard enough the benefit's less than the cost. Think about how
hard it is to forge a passport.

### Proof-of-work as a participation requirement
We can use proof-of-work in the form of requiring hash values with a certain number of leading
zeroes (or other characters) to make forging transactions hard. If psi were real, an anonymous
psychic could make a ton of money on BTC mining!

## Building the minimum viable blockchain
We can create a modified form of consensus where verifying transactions costs more than sending
them for verification. This tips the balance in favor of being an honest participant but creates a
new problem: validating transactions now can cost as much as the transactions themselves.

### Adding "blocks" & transaction fee incentives
Blocks of transactions allow us to get around the problem of transaction fees being high enough as
to incentivize foul play.

In this system, we have transaction announcers and block creators.

### Racing to claim the transaction fees
We can get zero-coordination verification if we just let everyone race to verify blocks and
announce them to the network. Other verifiers will drop their current work and restart every time
this happens. But this leaves us with one issue: what happens when two verifiers create different
blocks at the exact same time?

### Resolving chain conflicts
If we let different workers process different newest blocks, eventually one sub-chain will become
longer (the one that gets worked on more). We can thus have a rule that all workers process the
longest chain.

### Blocks are never "final"
From this, we get an interesting conclusion: blocks can always be invalidated if a longer chain not
including them appears. That said, the deeper the block is in the chain, the more work is required
to create a chain that excludes it.
