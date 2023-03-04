# WaspLib
 WaspLib is a include for Simba to bot OldSchool RuneScape.
 
 WaspLib v2 is intended to work with [Simba 1400](https://github.com/ollydev/Simba) and [SRL-Development](https://github.com/ollydev/SRL-Development).

 If you are having problems I suggest you try [my fork of SRL-Development](https://github.com/Torwent/SRL) due to code changing too frequently in Olly's SRL-Development and something might be incompatible for a while.
 I also recommend you join my discord server and ask around there for help: [WaspBot](https://discord.gg/YMYUahmww9).
 
 For documentation refer to: [Documentation](https://torwent.github.io/WaspLib).
 
# What is WaspLib for?
 As mentioned earlier, to bot OldSchool RuneScape. It's purpose is to make writting scripts faster as it includes lot's of commonly used code throughout my scripts.
 
 Some things in WaspLib could be coming to SRL in the future but others are just too custom to ever be accepted there and will remain here.


 # What can I expect to get with WaspLib?

 ## Better walker maps
 WaspLib includes custom runescape maps that are more reliable and contain way more locations than the original SRL-Development maps.
 The reason I say they are more reliable is because it has proper edges around the map edges unlike SRL-Development.
 A good example of this would be the western edge of the desert, if you ever tried using RSWalker around the map edges in the desert you know it doesn't work properly.
 With my maps it should accurately walk around most edges.

 My maps also include way more locations and it conyains nearly everything I consider useful.
 The only missing parts are Keldagrim and GWD that can be included separately if needed and a couple upstairs locations and minigames.
 And unless you need one of those maps you should be able to find everything in my world and zeah map:
 - Tzhaar
 - Rooftop courses
 - Waterbirth
 - Lumbridge castle
 - Slayer tower
 - Much much more

 ![Image of WaspLib Map](https://github.com/Torwent/WaspLib/raw/master/osr/walker/map.png)
 
 ## WalkActions
 WaspLib also has a way of doing actions while walking.
 A lot of things can be done with it but some of the best uses for this are:
 - [x] Walk alching
 - [ ] Walk magic imbue
 - [x] Walk drop
 - [ ] Walk fletch
 - [ ] Walk crush dark essence

 ## Tile accurate object, npc and ground item detection
 WaspLib also provides tile accurate object and npc detection framework.
 You can use this when you want to find something only in one specific tile.
 For example if you are doing smithing on Varrock West and only want to use the southern most bank and the northern most anvil. WaspLib let's you do that easily.
 
 ![Image of rsobjects0](https://github.com/Torwent/WaspLib/raw/master/docs/images/rsobjects/rsobjects0.png)
 ![Image of rsobjects1](https://github.com/Torwent/WaspLib/raw/master/docs/images/rsobjects/rsobjects1.png)
 ![Image of rsobjects2](https://github.com/Torwent/WaspLib/raw/master/docs/images/rsobjects/rsobjects2.png)

 ## Extra Interfaces
 WaspLib supports several interfaces that SRL does not.
 Examples of this are:
 - [x] Anvil
 - [x] Collect box
 - [x] Furniture builder
 - [x] Crafting
 - [x] Silver
 - [x] Shop
 - [ ] Tanner

