# GABC_psalm_pt
Psalm Tone Tool for portuguese language.

# Usage
* Exporting a PDF named "psalm_tp.pdf" with the Tonus Paschalis:
```
$python main.py -p psalm.txt -t tp -e -f psalm_tp
```    

* Printing GABC to be used in an editor:
```
$python main.py -p psalm.txt -t tp -g
```

* Commands:
```
-p, --psalm PSALM  Psalm text file, e.g. -p psalm.txt.
-t, --tone TONE    Psalm Tones (L.U.):tone_1d, tone_1d2, tone_1f, tone_1g, tone_1g2, tone_1g3, tone_1a, tone_1a2, tone_1a3, tone_2, tone_3b, tone_3a, tone_3a2, tone_3g, tone_3g2, tone_4, tone_4e, tone_4alt_c, tone_4alt_a, tone_4alt_a2, tone_4alt_d, tone_5, tone_6, tone_6alt, tone_7a, tone_7b, tone_7c, tone_7c2, tone_7d, tone_8g, tone_8g2, tone_8c, tp
-e, --export       Export to PDF.
-f, --file FILE    Name of the file to export.
-g, --gabc         Print GABC.
```
# Dependencies:
* This program uses the algorithm 'ceci' from the project [Pɛtɾʊs (PhonEtic TRanscriber for User Support)](alessandrobokan/PETRUS) to separate the syllables and mark the stressed syllable.
* To export a PDF file, LuaTeX is needed and has to be in the system PATH.
