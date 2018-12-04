# Game of Stakes Rules(DRAFT)

These are the rules for playing Game of Stakes.

They can be updated at any time. Rule changes will be committed here and notifications will occur on [Riot](https://matrix.to/#/!hEuEYSWKomxnWlSKqi:matrix.org?via=matrix.org&via=matrix.bitple.com&via=t2bot.io)
This document is the only authoritative set of rules, superseding all prior announcements.

## Victory Criteria

Victory in Game of Stakes is based on providing a convincing demonstration of interesting attacks on the Cosmos Proof of Stake incentivization layer.

Tendermint staff will be making recommendations to the Interchain Foundation based on the demonstrated performance of validators. The goal of Game of Stakes is to maximize a validators uptime and accumulate stake through manipulation of the inflation, fee distribution and consensus system. Novel, interesting and successful strategies will play a large role in our recommendations.

In general, Tendermint will weight uptime over raw stake for determining winners. 

Only validator operator addresses registered with us are eligible to win. If you need to change your operator address, you must clear it with Tendermint to remain eligible.

## Disqualification

Tendermint will disqualify and, if necessary, fork out players that undermine the goals of Game of Stakes to test interesting strategies for manipulating the incentive system. The most obvious reason for disqualification is trying to "win" through a sybil attack on the registration process. If you simply registered accounts for your friends  and then delegate or transfer all your STAKE to a single or small number of validators, this will disqualify all the participants. Griefing validators by delegating stake to try and get them disqualified is also forbidden. Cartel based attacks that require custom engineering are expressly in bounds.

## Prohibited Behavior

While participants are encouraged to behave adversarially on the network, engaging in the following specific harmful adversarial actions is prohibited and could be cause for disqualification from the game. Some examples of these actions include:

Any attacks against nodes that violate Amazon Web Services Acceptable Use Policy and Google Cloud Platform's Acceptable Use Policy and other specific services you use. Please familiarize yourself with those policies, since violating them could not only disqualify you from GoS, but could also get you suspended or permanently banned from those services.

Social engineering attacks against other validators. Social engineering is the term used for a broad range of malicious activities accomplished through human interactions that use psychological manipulation to trick users into making security mistakes or giving away sensitive information. Activities like phishing, cloud account credential compromise, malware distribution, and physical security attacks on data centers are out of bounds for this competition.

Attacking any testnets other than the official GoS Testnet.

Causing long-term harm to a validator setup.

Exploiting application-level security vulnerabilities in Cosmos + Tendermint code. Any bugs that are discovered should be reported to security@tendermint.com, or through our bug bounty program on HackerOne. Vulnerabilities that are disclosed by GoS participants may be eligible for reward payouts in Atoms, and participants who exploit vulnerabilities to gain stake will be disqualified from the contest.

## Forks

Fork based upgrades can be expected during Game of Stakes. Tendermint will notify players of what chain-id is being used to score players. If a cartel double spends on a chain, players should retain their WAL files and submit them to Tendermint to increase their own standing in the final ranking.

Players are expected to run the software with the latest bug fixes and improvements from the Tendermint developers.

## Governance

Governance is largely not a core piece of Game of Stakes. Governance votes that fail will result in burnt coins. Players can also vote for a network wide upgrade to new versions of the software. Tendermint will change scored chain in accordance with governance. If players vote for a non-Tendermint provided release, there will be a bonus for the player that creates the upgrade.

