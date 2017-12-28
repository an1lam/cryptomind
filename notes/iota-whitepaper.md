## Terms
- Poisson Point Process
- Positive Recurrent Function
- Markov Chain Monte Carlo 
- Cutset

## Questions
- What's the discrimination by participants of which he speaks?
- What does it mean for two transactions to conflict? How does IOTA, and Bitcoin for that matter,
  actally detect double spends?

## Summary
We can successfully model transactions as a DAG, where each transaction is a node with an edge
between itself and the transaction it "approves". Approving a transaction involves finding a proper
nonce to add to a hash value, similar to Bitcoin's block approval algorithm. The DAG approach, when
coupled with a proper tip approval strategy, allows for similar resilience to Bitcoin, but has the
advantages of:
- having participants and approvers be the same people;
- lower computing requirements;
- being more resistant to quantum algorithms.
The DAG approach can due this while ensuring that approval time remains proportionate to propagation
time.
