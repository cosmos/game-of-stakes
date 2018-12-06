# Game Of Stakes

![Game Of Stakes](GameOfStakes.png)


Game of Stakes es una testnet de Cosmos incentivada.

Aquí puedes encontrar:

[Reglas](RULES.md)

Archivos del genesis.

Instrucciones para el inicio de la red.

## Enviar una transacción de génesis.

Estamos tratando de maximizar las posibilidades de un comienzo justo del Game of Steaks. Esto permitirá a los jugadores estar vinculados y en línea desde el principio.

Para vincularse a Génesis, es necesario generar una transacción del Génesis y presentarla al final del día, hora del Pacífico, el viernes 7 de diciembre.

La versión final del genesis.json será lanzada a las 6:00 am UTC el lunes 10 de diciembre.

Recomendamos descargar el archivo del génesis, iniciar el servidor y conectarse a los seeds nodes lo antes posible.

## Para generar una transacción del génesis:

[docs](https://github.com/cosmos/cosmos-sdk/blob/develop/docs/gaia/validators/validator-setup.md)

Instalar `v0.27.1` del SDK de Cosmos.

Ejecutar `gaiad init` 

Descargar el [genesis](https://github.com/cosmos/game-of-stakes/blob/master/genesis.json) a `$HOME/.gaiad/config/genesis.json` 

Después ejecutar

```
gaiad gentx \
  --amount 10000STAKE \
  --commission-rate "0.10" \
  --commission-max-rate "1.00" \
  --commission-max-change-rate "0.01" \
  --pubkey $(gaiad tendermint show-validator)  \
  --name <key-id>
```

Esto generará un archivo similar a `$HOME/.gaiad/config/gentx/gentx-c00ce0b868bd5d5576d23f0ad1090f3f478b7961.json`

Por favor, envíe este archivo situado en la carpeta `gentx` con un Pull Request a este repositorio. 






