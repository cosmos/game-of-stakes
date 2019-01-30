# Game Of Stakes

![Game Of Stakes](GameOfStakes.png)


Game of Stakes is Cosmos's incentivized testnet.

Here you will find:

[Rules](RULES.md)

[Genesis File](genesis.json)

Dec 18th 06:00 UTC is the current target for GoS.

chat here: [Riot](https://matrix.to/#/!RKBbCjMEiDPKKewRIE:matrix.org?via=matrix.org&via=t2bot.io)



## Updates

### Game of Stakes 4 The Endgame

We are targeting a manadatory software upgrade to Game of Stakes 4 at 12:00UTC on Friday Feb 1st. We will be also adding vesting stake to all game of stakes participants.

The last valid block for scoring on Game of Stakes 3 will be 12:00 UTC 12:00UTC on Thursday Jan 31st.




### Game of Stakes 3 the restart

We are excited to resume Game of Stakes in the new year at 15:00 UTC on Jan 3rd.

The new genesis file for Game of Stakes 3 is up.

We are expecting validators to run `0.29.1-0-g6bff708` which is a state machine compatible release that fixes an exploitable coin minting bug.

```
shasum -a 256 genesis.json
1dc332f04bb09e29fed2b596f85d7e43ebfc9247278cd12546ac5b9f4318ab0e  genesis.json
```

We are expecting to launch GoS 3 this week and possibly do a hard fork upgrade on Jan 10th.



### The holiday hiatus and Game of Stakes 3

We are on a holiday hiatus for Game of Stakes till Jan 3rd.

Check out short video [play by play](https://www.youtube.com/watch?v=orEQY2sMdlI) 

Here is what we are doing during the holiday hiatus.

- `genki-4000` is running. https://github.com/certusone/genki-4000

- The `genki-4001` upgrade is being planned for Dec 28th. This provide some additional stress testing of export to genesis process that has been a struggle to Q&A.

- I expect to be posting the GoS 3 genesis.json file before Jan 2nd with a genesis time of Jan 3rd. I am thinking of picking a more asia friendly time. https://github.com/certusone/genki-4000/issues/3

- We will be assessing the shortfalls in our QA process on the upgrade process after holidays but I think we can have confidence in a launch of the 3rd because of the prveious two steps.



### Upgrade 2.
>brought to you by Zaki and Certus One

The genesis time experiment in Upgrade 1 worked perfectly and caused us to start producing blocks and achieve consensus at exactly 2018-12-20 15:00 UTC.

However a bug in the gaiad export for zero height logic caused the chain to halt while committing block 30.

The genesis file could be fixed manually by resetting every height in the genesis file to 0.


To upgrade please **download the updated genesis.json**. We are still using version `0.29.0-0-g2b3842c58`

`gaiad unsafe-reset-all` <- this is safe since we are starting a new chain

`gaiad start` with command line flags as appropriate for your node type.

Genesis time will be 2018-12-21 15:00 UTC.

Your node will idle after `gaia start` and then automatically begin connecting.

### Upgrade 1.
>brought to you by Zaki and Certus One

We chose a very conservative initial blocksize of `50kb` for the initial game of stakes launch as a conservative starting.

With 199 validators online, the signatures in blockheader now take up most of the block.

We will be doing the first network upgrade.

To upgrade, **install the new gaiad version** `v0.29.0` and download the new genesis to your config folder.
`git fetch --tags`
`git checkout v0.29.0`
`make get_vendor_deps && make install`
`gaiad version`
`0.29.0-0-g2b3842c58`

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
0.28.0-0-g68019bef
```
Just a note gaia `v0.28.1` has been tested to be fully compatible with this chain. You can choose to use the version at launch and we will shorly reccomend all players upgrade.

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

`0e7132b284e8fc8c8e51a90e158204b376d6203e5f12c14e253edbfb38dbebef genesis.json`


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
- `735120d143424734f48692097731f95b5b1d04c1@35.193.88.20:26656`

### Scoring

Games of Stakes scoring will take place at an preannounced blockheight on GoS 4.

Scoring will primarily consider the number of times a validator has been jailed and the duration of jailing across GoS 1 and GoS3.

Among player who are in the top tier of min jailing instances , we will will looks at signed pre commits and accumulated stake for scoing.

Finally there will be bonuses in the allocation for valdiators who have contributed in interesting ways to Game of Stakes and the retrospective