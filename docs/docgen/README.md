Generates the repository documentation files from comments in the source files.

Example documentation comment:

```
(*
# Mainscreen.PointToMM
\`\`\`pascal
function TRSMainScreen.PointToMM(MS: TPoint; Height: Int32=0; Accuracy:Double=0.2): Vector3;
\`\`\`

Takes a mainscreen point and converts it to a point on the minimap.

Returns a Vector3 which includes input height. Conversion to a TPoint if that's what you need is simply
done by calling `.ToPoint()` on the result.

### Example
\`\`\`pascal
  WriteLn Mainscreen.PointToMM(Point(250,140), 2);
  WriteLn Mainscreen.PointToMM(Point(250,140), 2).ToPoint(); // as a TPoint (lost accuracy)
\`\`\`
*)
```

Usage (Linux):

```bash
sudo apt-get install python3 python3-pip
sudo pip install sphinx furo myst-parser
python3 docgen.py ../../
```
