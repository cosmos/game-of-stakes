# Game Of Stakes

![Game Of Stakes](GameOfStakes.png)


Game of Stakes is Cosmos's incentivized testnet.

Here you will find:

[Rules](RULES.md)

[Genesis File](genesis.json)

Instructions for the Network Start


## Submit a genesis transction.

We are trying to maximize the chances of a fair start to Game of Stakes. This will allow players to be bonded and online from the very begining.

To be bonded at genesis, you need to generate a genesis transaction and submit it by end of day pacific time on Friday December 7th.

The final genesis.json will all the bonded particpants will be released at 6:00 am UTC on Monday December 10th. 

I reccomend that you download the genesis file, start your server and connect to the seed nodes as early as possible.s

### To generate a genesis transaction,

[docs](https://github.com/cosmos/cosmos-sdk/blob/develop/docs/gaia/validators/validator-setup.md)

install `v0.27.1` of the Cosmos SDK.

run `gaiad init`

Download [genesis](genesis.json) to `$HOME/.gaiad/config/genesis.json`

then run 

```
gaiad gentx \
  --amount=10000STAKE \
  --commission-rate="0.10" \
  --commission-max-rate="1.00" \
  --commission-max-change-rate="0.01" \
  --pubkey=$(gaiad tendermint show-validator)  \
  --name=<key-id>
```

This will generate a file roughly like `$HOME/.gaiad/config/gentx/gentx-c00ce0b868bd5d5576d23f0ad1090f3f478b7961.json`

Please submit this file in `gentx` folder in a Pull Request on this repository.




