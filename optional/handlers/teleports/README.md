
## TUniversalTransport and TTeleportLocation
There are some types in `records.simba` that might be interesting, but the two central parts of this library are the record `TUniversalTransport` in `transport.simba` and the static record `RSTeleports` in `rsteleports.simba`.

On `RSTeleports` you can find many `TTeleportLocation`s for example `RSTeleports.GRAND_EXCHANGE`

If you `WriteLn` this, it looks like:
`{WORLDPOINT = {X = 8040, Y = 2524}, TELEPORTTYPE = JEWELLERY, MAGICLEVEL = 0, ITEM = Ring of Wealth, DESTINATION = Grand Exchange, DISPATCHERRING = False}`

Just ignore `DISPATCHERRING`, but this is the core of `TUniversalTransport`. Each teleport location has a `WorldPoint: TPoint` which maps to `TRSWalker`'s coordinates. You can pass these locations into an initialized `TUniversalTransport` via its `run` method like this:
```pascal
var
    Transport: TUniversalTransport;
    teleportLocation: TTeleportLocation := RSTeleports.GRAND_EXCHANGE;
begin
    Transport.Init(EFairyTeleportItem.DRAMEN, 'ardougne cloak 2');
    Transport.run(teleportLocation);
end;
```

This will look in your inventory and equipment for the teleport's item (or teleport tab), if it can't find it you must get that item. Here's an example for how the Transport can assist in getting your item by using `Transport.genericJewelleryBankTeleport()`, `Transport.desperateBankOpen()` and `Transport.withdrawTeleportItem(teleportLocation)` :

```pascal
var
  Transport: TUniversalTransport;
  teleportLocation: TTeleportLocation := RSTeleports.GRAND_EXCHANGE;
begin
  try
    Transport.Init(EFairyTeleportItem.DRAMEN, 'ardougne cloak 2');
    if not Transport.run(teleportLocation) then
    begin
      Transport.genericJewelleryBankTeleport();
      Transport.desperateBankOpen();
      if not Transport.withdrawTeleportItem(teleportLocation) then
        raise 'You dont have the item needed for ' + teleportLocation.destination
      else Bank.Close(True);
      Transport.run(teleportLocation);
    end;
  except
    WriteLn 'We ending';
    WriteLn GetExceptionMessage();
  end;
end; 
```

Please note that `Transport.Init` takes an `EFairyTeleportItem = (DIARY,DRAMEN,LUNAR,NONE)` and a tier of cloak. Please configure this to fit your character. Leave the cape as `''` if you don't have any diary complete.

If you are feeling spicy and would rather use a `TPoint` than a `TTeleportLocation`, you can try getting an ideal teleport by `TUniversalTransport.getIdealTeleport(destination: TPoint, teleports): TTeleportLocation`. The ideal teleport is the closest teleport to the destination with a connecting web path nearby. Since this returns a `TTeleportLocation` you can withdraw it with `withdrawTeleportItem`. Then use `TUniversalTransport.run(destination: TPoint)`. It will then walk there after the teleport.

## Fairy Rings
If you look at `TTeleportLocation` you will see the field `teleportType: ETeleportType`. 

`ETeleportType = (NORMAL_MAGIC,ANCIENT_MAGICKS,LUNAR_MAGIC,ARCEUUS_MAGIC,JEWELLERY,OTHER,SCROLL,FAIRY_RING)`

This enum is how the teleport handlers are chosen. If a teleport uses `NORMAL_MAGIC, ANCIENT_MAGICKS,LUNAR_MAGIC,ARCEUUS_MAGIC` we use teleport tabs. If a teleport uses JEWELLERY then we use the corresponding item. Other is like diary teleports.

Finally, there is a `FAIRY_RING`. We use RSW to find a nearby fairy ring with a  connecting RSW path. Based on how you ran `Transport.Init` it will make sure the configured item is equipped (dramen/lunar staff). If there isn't a nearby ring, then we try to use the ardy cape configured in `Transport.Init` then we'll walk to the Monastery ring. If you don't have these then you can do something similar and just withdraw them.
