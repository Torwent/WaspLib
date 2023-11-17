## [15.0.1](https://github.com/Torwent/WaspLib/compare/v15.0.0...v15.0.1) (2023-11-17)


### Bug Fixes

* **AlchHandler:** better timer logic ([3cfd419](https://github.com/Torwent/WaspLib/commit/3cfd419c7bf9cf450ca3ba7620f564fba1502268))



# [15.0.0](https://github.com/Torwent/WaspLib/compare/v14.13.0...v15.0.0) (2023-11-16)


### Bug Fixes

* scoped enums and ERSConsumable renames ([b08a199](https://github.com/Torwent/WaspLib/commit/b08a199b789dbe243e51b6586ebcb501b01de7c2))


### BREAKING CHANGES

* WaspLib utils are now scoped. Other enums will be scoped at a later time.
* ERSConsumables were renamed to remove the prepended "_CONSUMABLE".
Example of old vs new usage:
```pascal
//old usage:
Inventory.ContainsConsumable(FOOD_CONSUMABLE);
Inventory.Consume(FOOD_CONSUMABLE);
//new usage:
Inventory.ContainsConsumable(ERSConsumable.FOOD);
Inventory.Consume(ERSConsumable.FOOD);
```



# [14.13.0](https://github.com/Torwent/WaspLib/compare/v14.12.7...v14.13.0) (2023-11-13)


### Features

* **walker:** can now setup a map as a region ([b4639ec](https://github.com/Torwent/WaspLib/commit/b4639ecda552e8602d0602d0836dc633ceffc8ad))



## [14.12.7](https://github.com/Torwent/WaspLib/compare/v14.12.6...v14.12.7) (2023-11-13)


### Bug Fixes

* **waspweb:** read notes ([d9a98c1](https://github.com/Torwent/WaspLib/commit/d9a98c11980a2b9a3f0ae971bf575586424d1c8c))



## [14.12.6](https://github.com/Torwent/WaspLib/compare/v14.12.5...v14.12.6) (2023-11-11)


### Bug Fixes

* **combathandler:** should have slightly less delay when attacking things when it's not in combat ([dcfbfb3](https://github.com/Torwent/WaspLib/commit/dcfbfb365cab24b5e7968dd3d6fa577cb45cd2c6))



