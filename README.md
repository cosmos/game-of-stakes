# Game Of Stakes

![Game Of Stakes](GameOfStakes.png)


Game of Stakes is Cosmos's incentivized testnet.

Here you will find:

[Rules](RULES.md)

[Genesis File](genesis.json)

Dec 18th 06:00 UTC is the current target for GoS.

chat here: [Riot](https://matrix.to/#/!RKBbCjMEiDPKKewRIE:matrix.org?via=matrix.org&via=t2bot.io)



## Updates

### Upgrade 1.
>brought to you by Zaki and Certus One

We chose a very conservative initial blocksize of `50kb` for the initial game of stakes launch as a conservative starting.

With 199 validators online, the signatures in blockheader now take up most of the block.

We will be doing the first network upgrade.

To upgrade, **install the new gaiad version** `v0.29.0` and download the new genesis to your config folder.
`git fetch --tags`
`git checkout v0.29.0`
`make get_vendor_deps && make install`

`gaiad version` should return: `0.29.0-0-g2b3842c5`

`gaiad unsafe-reset-all` <- this is safe since we are starting a new chain

`gaiad start` with command line flags as appropriate for your node type.

Genesis time will be 2018-12-20 15:00 UTC.

Your node will idle after `gaia start` and then automatically begin connecting.

### Launch policy

We are delaying Game of Stakes launch based on the demands of the validator community to run a 48hr testnet.
Chat here: [Riot](https://matrix.to/#/!RKBbCjMEiDPKKewRIE:matrix.org?via=matrix.org&via=t2bot.io)

The genensis file has been released.  Keep reading...

If you're a validator who had to submit a "Simulated Event" form to your cloud services provider, you may want to contact the provider with updated dates for the challenge or resubmit your form to ensure that you are in compliace with your provider's terms of service.

## Instructions for Launching Game of Stakes


### Welcome to the Launch of Game of Stakes.

You are about to be part of largest experiment in byzantine fault tolernant computer science. Today you an going to help launh the largest Byzantine Fault Tolerant network in history.

This be is the first large scale adversarial BFT network ever.

This will network will be the first demonstration of cartel behavior and censorship in an incentivized network.

We are going to do a decentralized network start.  I expect it will take us at least 24 hours. If we don’t start in 24 hours, we will bump the chain id and require new gen-txs. The window to submit a gen-tx will be 2-3 hours if we don't launch.

Doing a decentralized network start of this scale will push Tendermint to it’s limits. I believe it will be possible but every participant is going to have to take enormous care to get their configuration right.

First, triple check your software versions.

```
gaiad version
0.29.0-0-g2b3842c5
```
Just a note gaia `v0.29.0` has been tested to be fully compatible with this chain. You can choose to use the version at launch and we will shorly reccomend all players upgrade.

Next check the timeouts in your `config.toml`

```
timeout_propose = "3s"
timeout_propose_delta = "500ms"
timeout_prevote = "1s"
timeout_prevote_delta = "500ms"
timeout_precommit = "1s"
timeout_precommit_delta = "500ms"
timeout_commit = "5s"
```

Finally,  make sure you have the correct `genesis.json`

`shasum -a 256 genesis.json `

`e12cfd40f58653c69cee8d9d8d649f96d875dcab1ee24799cbbf3b9c98b510b1 genesis.json`


Once you have double checked all this, `gaiad unsafe-reset-all`
We recommend setting min fees on your sentry nodes via the commandline or gaiad.toml. `gaiad start --minimum_fees=1STAKE,1photino`.  
We would also very much appreciate logs being kept on validator nodes via `gaiad start  --log_level="consensus:debug,mempool:debug,*:info"`.
After you have `gaiad start` do not run a reset all again unless we have decided to switch to a new chain id.

### Seed Nodes

I'll accept seed nodes as pull requests here.

- `c04d6c2bd5b8cfa1523ea167686f7bad152d6fe7@35.233.162.22:26656`(cryptiumlabs1)
- `3ae23cf4cc791043d8aa2165f013c17c58f28083@35.242.246.54:26656`(cryptiumlabs2)
- `68f695585e46ba097816a84ac7f682f917248ae4@35.240.142.49:26656`(cryptiumlabs3)
- `ba3bacc714817218562f743178228f23678b2873@public-seed-node.gos.certus.one:26656`
- `db02715d74e68c48884aad9e9c7dac6bc7f3c7cd@35.239.245.16:26656`
- `343f3d9f1851df44acf976ac832c3633ab49e001@54.146.83.223:26656`
