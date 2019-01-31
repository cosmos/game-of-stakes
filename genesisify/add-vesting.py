#!/usr/bin/env python3

import json, sys

if len(sys.argv) != 3:
    print('Usage: ./add-vesting.py [genesis.json] [new_genesis.json]')
    sys.exit(1)

raw = open(sys.argv[1]).read()
old = json.loads(raw)

addrs = set([x for x in json.load(open('addrs.json'))])
print('{} whitelisted accounts'.format(len(addrs)))

# Add vesting coins to whitelisted accounts
for account in old['app_state']['accounts']:
  if account['address'] in addrs:
    print('Account {} matched'.format(account['address']))
  else:
    print('Account {} did not match'.format(account['address']))

new = sys.argv[2]
json.dump(old, open(new, 'w'), indent = True)

print('Wrote {}'.format(new))
