#!/usr/bin/env python3

import json, sys, math

if len(sys.argv) != 3:
  print('Usage: ./v0.29-to-v0.30.py [exported_genesis.json] [new_genesis.json]')
  sys.exit(1)

raw = open(sys.argv[1]).read()
raw = raw.replace('STAKE', 'stake')

print('Renamed "STAKE" to "stake"')

old = json.loads(raw)
new = sys.argv[2]

# Delete old distribution fields

del old['app_state']['distr']['validator_dist_infos']
del old['app_state']['distr']['delegator_dist_infos']

print('Cleared old distribution state')

old['app_state']['staking'] = old['app_state']['stake']
del old['app_state']['stake']

print('Renamed "stake" to "staking"')

# Dec -> Int

old['app_state']['staking']['pool']['not_bonded_tokens'] = str(int(math.floor(float(old['app_state']['staking']['pool']['loose_tokens']))))
del old['app_state']['staking']['pool']['loose_tokens']
old['app_state']['staking']['pool']['bonded_tokens'] = str(int(math.floor(float(old['app_state']['staking']['pool']['bonded_tokens']))))

for v in old['app_state']['staking']['validators']:
  v['tokens'] = str(int(math.floor(float(v['tokens']))))

print('Converted sdk.Dec to sdk.Int for validators, and renamed "loose_tokens" to "not_bonded_tokens"')

# Create new distribution fields

# All validators
validators = [v['operator_address'] for v in old['app_state']['staking']['validators']]

def shares_to_tokens(d):
  val = d['validator_addr']
  val = [v for v in old['app_state']['staking']['validators'] if v['operator_address'] == val][0]
  tokens = float(val['tokens'])
  shares = float(val['delegator_shares'])
  del_tokens = float(d['shares']) * tokens / shares
  return str(int(math.floor(del_tokens)))

# All delegations
delegations = [(d['delegator_addr'], d['validator_addr'], shares_to_tokens(d)) for d in old['app_state']['staking']['bonds']]

# Delete val accum
del old['app_state']['distr']['fee_pool']['val_accum']
del old['app_state']['distr']['fee_pool']['val_pool']

print('Deleted val accum & val pool')

# No outstanding rewards
old['app_state']['distr']['outstanding_rewards'] = None

print('Set outstanding rewards')

# One starting info per delegation
old['app_state']['distr']['delegator_starting_infos'] = [{
  'delegator_addr': d,
  'validator_addr': v,
  'starting_info': {
    'previous_period': '1',
    'stake': s,
    'height': '0'
  }
} for (d, v, s) in delegations]

print('Set delegator starting infos')

# One starting period per validator
old['app_state']['distr']['validator_historical_rewards'] = [{
  'validator_addr': v,
  'period': '1',
  'rewards': None
} for v in validators]

print('Set validator historical rewards')

# Zero starting accumulated commission
old['app_state']['distr']['validator_accumulated_commissions'] = [{
  'validator_addr': v,
  'accumulated': None
} for v in validators]

print('Set validator accumulated commissions')

# Zero starting current rewards for each validator
old['app_state']['distr']['validator_current_rewards'] = [{
  'validator_addr': v,
  'rewards': {
    'rewards': None,
    'period': '2'
  }
} for v in validators]

print('Set validator current rewards')

# No slash events
old['app_state']['distr']['validator_slash_events'] = []

print('Set validator slash events')

# Set new required auth params

old['app_state']['auth']['params'] = {
  "MemoCostPerByte": "3",
  "MaxMemoCharacters": "256",
  "TxSigLimit": "7",
  "SigVerifyCostED25519": "590",
  "SigVerifyCostSecp256k1": "1000"
}

print('Set auth params')

# Update slashing params

old['app_state']['slashing']['params']['downtime-jail-duration'] = '600000000000'
del old['app_state']['slashing']['params']['downtime-unbond-duration']

print('Renamed slashing params')

# Sort community pool coins

old['app_state']['distr']['fee_pool']['community_pool'] = old['app_state']['distr']['fee_pool']['community_pool'][::-1]

for elem in old['app_state']['distr']['fee_pool']['community_pool']:
  elem['amount'] = str(int(round(float(elem['amount'])) + 1))

print('Sorted community pool and rounded amounts')

# Set exported to false

old['app_state']['staking']['exported'] = False

print('Set exported = false (necessary to initialize correct distribution state)')

# Sort coins in accounts

for account in old['app_state']['accounts']:
  # apparently they were all just sorted in reverse
  if account['coins'] is not None:
    account['coins'] = account['coins'][::-1]

# Set chain ID

old['chain_id'] = 'game_of_stakes_4'

print('Set chain ID to game_of_stakes-4')

json.dump(old, open(new, 'w'), indent = True)

print('Wrote {}!'.format(new))
