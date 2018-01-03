"""
Basic block chain functionality.

Includes generating and validating blocks. Doesn't include sending to network, proof-of-work, or 
consensus.

Based on tutorial by ecomunsing (http://ecomunsing.com/build-your-own-blockchain).
"""

import hashlib, json, pprint, random, sys

def hash(msg=''):
  if type(msg) != str:
    msg = json.dumps(msg, sort_keys=True)

  return unicode(hashlib.sha256(msg).hexdigest(), 'utf-8')

def make_transaction(max_value=3):
  """Creates a random valued transaction deposit / withdrawal pair."""
  sign = int(random.getrandbits(1))*2 - 1
  amount = random.randint(1, max_value)
  alice_pays = sign * amount
  bob_pays = -1 * alice_pays
  return {u'Alice': alice_pays, u'Bob': bob_pays}

def update_transaction_state(transaction, state):
  state = state.copy()

  for participant in transaction:
    state[participant] = state.get(participant, 0) + transaction[participant]

  return state

def is_valid_transaction(transaction, state):
  # The withdrawal has to equal the deposit.
  if sum(transaction.values()) != 0:
    return False

  # Are the participants good for it? Positive deposits imply the participant is a recipient of the
  # value meaning they'll always be able to "pay" for the transaction.
  for participant, deposit in transaction.iteritems():
    balance = state.get(participant, 0)

    if balance + deposit < 0:
      return False

  return True

def create_genesis_block(initial_state):
  block_contents = {
    u'blockId': 0,
    u'transactionCount': 1,
    u'parentHash': None,
    u'transactions': [initial_state],
  }

  return {u'hash': hash(msg=block_contents), u'contents': block_contents}

def initialize_block_chain(initial_state):
  return [create_genesis_block(initial_state)]

def make_block(transactions, block_chain):
  assert len(block_chain) > 0, "Must have at least a genesis block in chain."
  prior_block = block_chain[-1]
  prior_block_contents = prior_block['contents']

  new_block_contents = {
    u'blockId': prior_block_contents[u'blockId'] + 1,
    u'transactionCount': len(transactions),
    u'parentHash': prior_block[u'hash'],
    u'transactions': transactions,
  }
  new_block = {u'hash': hash(new_block_contents), u'contents': new_block_contents}
  return new_block

def chain_block(transactions, block_chain):
  block_chain.append(make_block(transactions, block_chain))
  return block_chain

def mine_blocks(transactions, state, block_chain, block_size_limit=5):
  while len(transactions) > 0:

    block_transactions_buffer = []
    while len(transactions) > 0 and len(block_transactions_buffer) < block_size_limit:
      next_transaction = transactions.pop()

      if is_valid_transaction(next_transaction, state):
        state = update_transaction_state(next_transaction, state)
        block_transactions_buffer.append(next_transaction)

    block_chain = chain_block(block_transactions_buffer, block_chain)

  return block_chain, state

class InvalidBlockError(Exception):
  pass

def check_block_hash(block):
  if hash(block[u'contents']) != block[u'hash']:
    raise InvalidBlockError(
      'Block %d\'s hash doesn\'t match actual hash of contents.' %
        block[u'contents'][u'blockId'])

def check_block_and_update_state(block, parent_block, state):
  check_block_hash(block)

  if block[u'contents'][u'parentHash'] != parent_block[u'hash']:
    raise InvalidBlockError(
      'Block %d\'s parent_block hash doesn\'t match actual parent\'s hash.' %
        block[u'contents'][u'parentHash'])

  if block[u'contents'][u'blockId'] != parent_block[u'contents'][u'blockId'] + 1:
    raise InvalidBlockError(
      'Block %d\'s ID doesn\'t match parent ID %d plus one.' %
        block[u'contents'][u'blockId'], parent_block[u'contents'][u'blockId'])

  for transaction in block[u'contents'][u'transactions']:
    if not is_valid_transaction(transaction, state):
      raise InvalidBlockError(
        'Bad transaction %r in block %d.' % (transaction, block[u'contents'][u'blockId']))
    state = update_transaction_state(transaction, state)

  return state

def check_chain(block_chain):
  genesis_block = block_chain[0]
  state = {}

  # Validate the genesis block by hand because there's no parent_block hash on it.
  for transaction in genesis_block[u'contents'][u'transactions']:
    state = update_transaction_state(transaction, state)
  check_block_hash(genesis_block)

  parent_block = genesis_block
  for block in block_chain[1:]:
    state = check_block_and_update_state(block, parent_block, state)
    parent_block = block
  return state



def main():
  state = {u'Alice': 50, u'Bob': 50}
  block_chain = initialize_block_chain(state)

  transaction_buffer = [make_transaction() for _ in range(30)]
  chain, state = mine_blocks(transaction_buffer, state, block_chain)
  for block in chain:
    print pprint.pprint(block)
  print state
