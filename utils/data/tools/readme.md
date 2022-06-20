Due to technical issues with Simba dealing with JSON files
I had to make the formatter tool in 2 separate scripts.

objectsformatter1.simba and objectsformatter2.simba

And they need to be ran in that order.

"objectsformatter1.simba" is intended to run on a raw
objects.json file.
Said file has to be named "objects-raw.json" and has to be
placed in "Simba\Includes\WaspLib\utils\data\tools\".

This first will join all JSON Objects withe the same "name"
key into a single one.
And will generate a new JSON file named "objects-temp.json".
When the tool is done running it will give an error of some
internal thing in Simba. I'm not sure what causes this,
might be due to not freeing JSONObjects/Arrays properly,
but I couldn't figure it out and that's why I had to make
this in 2 scripts.
The error can be ignored.

Once we have "objects-temp.json" we should run
"objectsformatter2.simba".

This will look through each of out JSONObjects and join
common RSObject IDs into a single one, only keeping their
unique coordinates.
When the tool is done running, once again you will get
an internal error in Simba.
You can ignore this error.

And now you will have the final clean
"Simba\Includes\WaspLib\utils\data\objects.json" created.
