#!/usr/bin/env python3

import json, sys

if len(sys.argv) != 3:
    print('Usage: ./add-vesting.py [genesis.json] [new_genesis.json]')
    sys.exit(1)

raw = open(sys.argv[1]).read()
old = json.loads(raw)

addrs = set([x for x in json.load(open('addrs.json'))])
print('{} whitelisted accounts'.format(len(addrs)))

supply_diff = 0

def add_vesting_account(addr):
  global supply_diff
  found = [x for x in old['app_state']['accounts'] if x['address'] == addr]
  if len(found) > 0:
    found = found[0]
    if found['coins'] is None:
      st = []
      found['coins'] = []
    else:
      st = [x for x in found['coins'] if x['denom'] == 'stake']
    if len(st) > 0:
      st = st[0]
      st['amount'] = str(int(st['amount']) + 500000)
    else:
      found['coins'].append({'denom': 'stake', 'amount': '500000'})
    found['original_vesting'] = [{'denom': 'stake', 'amount': '500000'}]
    found['start_time'] = '1548970600'
    found['end_time'] = '1550180200'
    print('Address {} found'.format(addr))
    supply_diff = supply_diff + 500000
  else:
    print('Address {} not found, skipping'.format(addr))

# Add vesting coins to whitelisted accounts
for addr in addrs:
  add_vesting_account(addr)

# Update supply
old['app_state']['staking']['pool']['not_bonded_tokens'] = str(int(old['app_state']['staking']['pool']['not_bonded_tokens']) + supply_diff)

new = sys.argv[2]
json.dump(old, open(new, 'w'), indent = True)

print('Wrote {}'.format(new))
