"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var tonic_1 = require("./tonic");
var syllable_1 = require("./syllable");
function printUsage() {
    console.log("\nUsage: bun run index.ts --word <word> [--tonic] [--syllable] [--full]\n\nOptions:\n  --word WORD      The word to analyze (required)\n  --tonic          Run tonic analysis\n  --syllable       Run syllabification\n  --full           Enable full output mode\n");
}
function main(args) {
    var word = null;
    var runTonic = false;
    var runSyllable = false;
    var full = false;
    var i = 0;
    while (i < args.length) {
        var arg = args[i];
        if (arg === "--word") {
            i++;
            if (i < args.length) {
                word = args[i];
            }
            else {
                console.error("Error: --word requires a value.");
                printUsage();
                return 1;
            }
        }
        else if (arg === "--tonic") {
            runTonic = true;
        }
        else if (arg === "--syllable") {
            runSyllable = true;
        }
        else if (arg === "--full") {
            full = true;
        }
        else {
            console.error("Error: Unknown argument: ".concat(arg));
            printUsage();
            return 1;
        }
        i++;
    }
    if (!word) {
        console.error("Error: --word is required.");
        printUsage();
        return 1;
    }
    // If neither --tonic nor --syllable specified, default to both
    if (!runTonic && !runSyllable) {
        runTonic = true;
        runSyllable = true;
    }
    var syllables = [];
    if (runSyllable || runTonic) {
        syllables = (0, syllable_1.default)(word).split("@");
    }
    if (full) {
        // Consolidated and pretty output for full mode
        console.log("┌───────────────────────────────────┐");
        console.log("│         Análise de palavra        │");
        console.log("└───────────────────────────────────┘");
        console.log("Palavra: ".concat(word));
        console.log("───────────────────────────────────");
        if (runSyllable) {
            console.log("S\u00EDlabas: ".concat(syllables.join(" - ")));
        }
        if (runTonic) {
            var tonicNumber = (0, tonic_1.default)(syllables);
            var tonicSyllableText = syllables[syllables.length - tonicNumber];
            var tipoSilaba = void 0;
            if (tonicNumber === 1) {
                tipoSilaba = "oxítona";
            }
            else if (tonicNumber === 2) {
                tipoSilaba = "paroxítona";
            }
            else if (tonicNumber === 3) {
                tipoSilaba = "proparoxítona";
            }
            else {
                tipoSilaba = "???";
            }
            console.log("S\u00EDlaba t\u00F4nica: '".concat(tonicSyllableText, "' (").concat(tipoSilaba, " #").concat(tonicNumber, ")"));
        }
        console.log("───────────────────────────────────");
        console.log(""); // Add a newline for better visual separation
    }
    else {
        // Original non-full output behavior
        if (runSyllable) {
            console.log(syllables.join("-"));
        }
        if (runTonic) {
            var tonicNumber = (0, tonic_1.default)(syllables);
            console.log(tonicNumber);
        }
    }
    return 0;
}
// Start the program
process.exit(main(process.argv.slice(2)));
