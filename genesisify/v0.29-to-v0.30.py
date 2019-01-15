#!/usr/bin/env python3

import json, sys

if len(sys.argv) != 3:
  print('Usage: ./v0.29-to-v0.30.py [exported_genesis.json] [new_genesis.json]')
  sys.exit(1)

old = json.loads(sys.argv[1])
new = sys.argv[2]

# Delete old distribution fields

del old['distr']['validator_dist_infos']
del old['distr']['delegator_dist_infos']

# Create new distribution fields

# All validators
validators = [v['operator_address'] for v in old['staking']['validators']]

def shares_to_tokens(d):
  val = d['validator_addr']
  val = [v for v in old['staking']['validators'] if v['operator_address'] == val][0]
  tokens = int(val['tokens'])
  shares = int(val['delegator_shares'])
  del_tokens = int(d['shares']) * tokens / shares
  return str(del_tokens)

# All delegations
delegations = [(d['delegator_addr'], d['validator_addr'], shares_to_tokens(d)) for d in old['staking']['validators']]

# No outstanding rewards
old['distr']['outstanding_rewards'] = None

# One starting info per delegation
old['distr']['delegator_starting_infos'] = [{
  'delegator_addr': d,
  'validator_addr': v,
  'starting_info': {
    'previous_period': 1,
    'stake': s,
    'height': 0
  }
} for (d, v, s) in delegations]

# One starting period per validator
old['distr']['validator_historical_rewards'] = [{
  'validator_addr': v,
  'period': 1,
  'rewards': None
} for v in validators]

# Zero starting accumulated commission
old['distr']['validator_accumulated_commissions'] = [{
  'validator_addr': v,
  'accumulated': None
} for v in validators]

# Zero starting current rewards for each validator
old['distr']['validator_current_rewards'] = [{
  'validator_addr': v,
  'rewards': {
    'rewards': None,
    'period': 2
  }
} for v in validators]

# No slash events
old['distr']['validator_slash_events'] = []

json.dump(old, open(new, 'w'))

print('Wrote {}!\n'.format(new))
