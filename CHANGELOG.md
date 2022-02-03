## [6.0.2](https://github.com/Torwent/WaspLib/compare/v6.0.1...v6.0.2) (2022-02-03)


### Bug Fixes

* remove inventory background ([238b53d](https://github.com/Torwent/WaspLib/commit/238b53d34ab74b5bfd6ed09556c1fc01a16a696c))



## [6.0.1](https://github.com/Torwent/WaspLib/compare/v6.0.0...v6.0.1) (2022-01-31)


### Bug Fixes

* nake screen walk default ([2801347](https://github.com/Torwent/WaspLib/commit/280134710da5e76f26947265de2d6cb339faf0f2))



# [6.0.0](https://github.com/Torwent/WaspLib/compare/v5.6.0...v6.0.0) (2022-01-31)


### Bug Fixes

* catacomb coordinates ([72ce9aa](https://github.com/Torwent/WaspLib/commit/72ce9aad5607d91090a0af44f3d77a25f86fe99f))
* catacombs of kourend were wrong ([6e5b9d8](https://github.com/Torwent/WaspLib/commit/6e5b9d84f143579924c1eac00f7e3a74b1290ebc))
* coordinates ([e698772](https://github.com/Torwent/WaspLib/commit/e6987720922027417c9097cbc734192645fd9b70))
* coordinates and dark beasts added ([2823637](https://github.com/Torwent/WaspLib/commit/28236379c5e7664f738efc566b6c40a4e92564ed))
* coordinates now match smaller maps ([5651f6f](https://github.com/Torwent/WaspLib/commit/5651f6f9440a17f1c059cd01791d3a6d5358bb03))
* fixed a typo that made loothabdler pick useless stuff. ([047254c](https://github.com/Torwent/WaspLib/commit/047254c8b86306cdb6279ed767a3bfda56a01cb4))
* fixed dotfilter bug ([fa499f8](https://github.com/Torwent/WaspLib/commit/fa499f898868a399b04b547070e7e50aa7e4b473))
* fixed null bracelet error ([67d02f4](https://github.com/Torwent/WaspLib/commit/67d02f4ca5384c294a031614d5486050ce3cd483))
* improved loothandler with colors ([30ba497](https://github.com/Torwent/WaspLib/commit/30ba49705d5743c2d86977f2c4f7e923ce7a3cea))
* low doses consumables will now be properly withdrawn ([5c8d34a](https://github.com/Torwent/WaspLib/commit/5c8d34aa984ecd5f44e317f6378d8ebc1a692e17))
* minor fail safes ([43041d5](https://github.com/Torwent/WaspLib/commit/43041d5a559a2c1f62686e5b47cd67cf20bb0fc4))
* minor improvements to looting ([c59d901](https://github.com/Torwent/WaspLib/commit/c59d9018f0e4665396041c2c0654e047f0d2b608))
* minor improvements to the combat handler ([4da7535](https://github.com/Torwent/WaspLib/commit/4da753569d5ddfbe81b1199e1ee528a7a3d62aec))
* more coordinates fixed and added in the catacombs ([7b06e0a](https://github.com/Torwent/WaspLib/commit/7b06e0a247888824168b503becd35b325e0f7075))
* reordered TRSMMDot variables so debugging rsmonsters don't crash Simba. ([73a41ed](https://github.com/Torwent/WaspLib/commit/73a41edd2c56a10dbb099f4bbedb426a2027088e))
* RSMMDot.WalkerIndex > -1 is always true because 0 is the default. ([3dbf4c9](https://github.com/Torwent/WaspLib/commit/3dbf4c9fac35a63f8f59bc7b7a4ba5a87fb269e6))
* rsmonster.setupcommon now properly sets up uptext everytime. ([03b1bbd](https://github.com/Torwent/WaspLib/commit/03b1bbd8abd838ac25be6a257f8d46adbb38b247))
* slayer task won't be set as completed anymore if we start with the message on the chatbox ([79eb2b9](https://github.com/Torwent/WaspLib/commit/79eb2b9a2dbcb631bb55b3781bfeeb8bc8541007))
* small delay on minimap spam click ([0692441](https://github.com/Torwent/WaspLib/commit/06924413e34f1bdae7e22c60258880d74f9e7bc4))
* typo in stamina 4 ([78b58bb](https://github.com/Torwent/WaspLib/commit/78b58bbf4a3f3cb7db9f11dca2113cecab9a0979))
* wintertodt map ([95a5f59](https://github.com/Torwent/WaspLib/commit/95a5f592c8bcd3559ca66471f6836f0a7aed0dd8))
* **CombatHandler:** Fixed antifire, antipoison and antivenom pots not being used ([ecc3742](https://github.com/Torwent/WaspLib/commit/ecc37426d2277676f10d7a92ca5d395ffb7702e0))
* **DotFilterArray:** Improved dot filters ([596d5c3](https://github.com/Torwent/WaspLib/commit/596d5c3a1b9cf961573468d07121eebef617a3eb))
* **maps:** update wasplib maps ([62c22ea](https://github.com/Torwent/WaspLib/commit/62c22eaf764e1c7faad728bd4efdfe6318a8f957))
* **rsmmdot:** fixed rsmonsters size being overwritten to 1. ([2b064b0](https://github.com/Torwent/WaspLib/commit/2b064b01bfd30dd18843e84b9c9907bdad29ffb8))
* **rsmmdots:** fixed the no height issue I introduced in the last updates. ([b790a46](https://github.com/Torwent/WaspLib/commit/b790a467eb3e2dada5a40670485395f5ed20bf40))


### Features

* add prayer to antiban skills if we have autoburying items ([26d89de](https://github.com/Torwent/WaspLib/commit/26d89debf8a72845c2dbe41c9de0618a13f60d82))
* added an easy way to retrieve map chunk strings ([6e94852](https://github.com/Torwent/WaspLib/commit/6e94852fcd3df44cdb1668c399e2fd4868a8d42b))
* logs are now named with the script name. ([bfadf81](https://github.com/Torwent/WaspLib/commit/bfadf81a0aa1cdbc598b3288d2015ce384511760))
* slayer antiban ([58a456b](https://github.com/Torwent/WaspLib/commit/58a456b0ad6b73c22e2c23d314cb390fe5e87b34))
* sleep time and length fields for the GUIs ([dfde14b](https://github.com/Torwent/WaspLib/commit/dfde14bee6c27c946125ded49344d19b153f29da))
* wrapper function for labeledcheckboxes ([b4f82fb](https://github.com/Torwent/WaspLib/commit/b4f82fb3c6a5c68c9a1f666e690d48b9918dc1c2))
* xpbar setup interface ([0555e93](https://github.com/Torwent/WaspLib/commit/0555e933fceb3c37b17727070ae65d7d46855fb4))
* **CombatHandler:** combat handler can now fully handle combat! ([651f51a](https://github.com/Torwent/WaspLib/commit/651f51ad37c1ba4ab69b6a7dc312be6233a47390))
* **CombatHandler:** emergency shutdown for combat handler ([f3d0d8a](https://github.com/Torwent/WaspLib/commit/f3d0d8a84cd4d75c6f87777d6a2ecdcb45de0764))
* **CombatHandler:** Now drinks boost potions. ([7355916](https://github.com/Torwent/WaspLib/commit/7355916d6972cddba995b941c3f9cd8b3e9d4eff))
* **CombatHandler:** variable to hold slayer task state ([b46035f](https://github.com/Torwent/WaspLib/commit/b46035f70648ccc4a26f13d805d9bd5db87958f5))
* **LootHandler:** Looting is now possible. ([d3a6249](https://github.com/Torwent/WaspLib/commit/d3a6249051d4b30d17fe1b7283ad58365b7e9c88))
* **MMDots:** the new dot filters are now working ([7160954](https://github.com/Torwent/WaspLib/commit/7160954bfe9d0a3c1a1dec5523361ecc0894bff4))


### BREAKING CHANGES

* This probably breaks compatibility with older scripts and includes.



# [5.6.0](https://github.com/Torwent/WaspLib/compare/v5.5.1...v5.6.0) (2022-01-04)


### Bug Fixes

* fixed my previous rushed update that didn't compile ([3e8fcc5](https://github.com/Torwent/WaspLib/commit/3e8fcc54a036517448369932552cecc2e9601536))


### Features

* new mmdot filter. ([2a5f30b](https://github.com/Torwent/WaspLib/commit/2a5f30b0838060bf4bf8c66b6c06a09f43ac8658))



## [5.5.1](https://github.com/Torwent/WaspLib/compare/v5.5.0...v5.5.1) (2022-01-03)


### Bug Fixes

* **CombatHandler:** Ocmmented out missing function ([be46ff1](https://github.com/Torwent/WaspLib/commit/be46ff19e438fb2f7012037c834748c1278f4580))



