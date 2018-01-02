import hashlib, json, random, sys

def hash(msg=''):
  if type(msg) != str:
    msg = json.dumps(msg, sort_keys=True)

  return unicode(hashlib.sha256(msg).hexdigest(), 'utf-8')

def make_transaction(max_value=3):
  """Creates a random valued transaction deposit / withdrawal pair."""
  sign = int(random.getrandombits(1))*2 - 1
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


def main():
  transaction_buffer = [make_transaction() for _ in range(30)]

