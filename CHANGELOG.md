## [15.0.4](https://github.com/Torwent/WaspLib/compare/v15.0.3...v15.0.4) (2023-11-24)


### Bug Fixes

* **Inventory:** Randomitem methods now properly support composite items like Cake(1..3) ([7f0d0fd](https://github.com/Torwent/WaspLib/commit/7f0d0fdf6adb894ea5c474dbd321652034a66257))



## [15.0.3](https://github.com/Torwent/WaspLib/compare/v15.0.2...v15.0.3) (2023-11-21)


### Bug Fixes

* Iowerth warriors coordinates ([dd873e0](https://github.com/Torwent/WaspLib/commit/dd873e0f30f8dd557f19476aa693135fa98a3d8c))



## [15.0.2](https://github.com/Torwent/WaspLib/compare/v15.0.1...v15.0.2) (2023-11-18)


### Bug Fixes

* read notes ([2bfd68f](https://github.com/Torwent/WaspLib/commit/2bfd68f36f232a4947d39a3138bde603137ed1f1))



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



