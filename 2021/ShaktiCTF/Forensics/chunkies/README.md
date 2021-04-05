# chunkies

The given PNG file was corrupted. We easily see the missing `\x89` at the top of the file before the `PNG` chunk. Then browsing the image again we see the `IADT` and the `INED` chunks. Using

```
sed -i 's/IADT/IDAT/g' fix.png
sed -i 's/INED/IEND/g' fix.png
```

is enough to fix every chunks. Last error is a CRC corruption as `pngcheck` shows:

```
$ pngcheck -v fix.png
...
CRC error in chunk IHDR (computed 5a7b8dc, expected 5a9b8dc)
...
```

Let's manually change the value from what it gets to what it expects, and get our flag!

![flag](fix.png)

```
shaktictf{Y4YyyyY_y0u_g0t_1T}
```
