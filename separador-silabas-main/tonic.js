"use strict";
var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.default = tonic;
// @filename: tonic.ts
/**
 * Determines the tonic (stressed) syllable of a word based on Portuguese accentuation rules.
 *
 * @param syllables An array of strings, where each string represents a syllable of the word.
 * @returns The 1-indexed position of the tonic syllable, counting from the end of the word.
 *          (e.g., 1 for the last syllable, 2 for the penultimate, 3 for the antepenultimate).
 * @throws Error if the input 'syllables' array is empty.
 */
function tonic(syllables) {
    syllables = syllables.filter(function (syllable) { return typeof syllable === 'string' && syllable.trim() !== ''; });
    // Define accent categories in order of precedence, from strongest/most specific to weakest.
    // Accents are checked from the rightmost syllable towards the left.
    var accentCategories = [
        "áéíóúÁÉÍÓÚ", // Acute accent (agudo) - strong
        "àèìòùÀÈÌÒÙ", // Grave accent (crase) - strong
        "âêîôûÂÊÎÔÛ", // Circumflex accent (circunflexo) - strong
        "ãẽĩõũÃẼĨÕŨ" // Tilde (til) - weak
    ];
    var syllableCount = syllables.length;
    // Handle invalid input: An empty array of syllables cannot have a tonic syllable.
    if (syllableCount === 0) {
        throw new Error("Input 'syllables' array cannot be empty.");
    }
    // Rule 1: Monosyllabic words are always tonic on their single syllable.
    if (syllableCount === 1) {
        return 1;
    }
    var _loop_1 = function (accentChars) {
        // For each accent type, iterate syllables from right to left (last to first).
        for (var i = syllableCount - 1; i >= 0; i--) {
            // Use non-null assertion (!) because 'i' is guaranteed to be a valid index here.
            var currentSyllable = syllables[i];
            // Check if any character in the current syllable matches any character in the current accent category.
            if (__spreadArray([], currentSyllable, true).some(function (char) { return accentChars.includes(char); })) {
                return { value: syllableCount - i };
            }
        }
    };
    // Rule 2: Check for graphic accents (acute, grave, circumflex, tilde).
    // Iterate through accent categories in their defined order of precedence.
    for (var _i = 0, accentCategories_1 = accentCategories; _i < accentCategories_1.length; _i++) {
        var accentChars = accentCategories_1[_i];
        var state_1 = _loop_1(accentChars);
        if (typeof state_1 === "object")
            return state_1.value;
    }
    // Rule 3: If no explicit graphic accents are found, apply general Portuguese accentuation rules.
    // These rules primarily determine if an unaccented word is oxytone (tonic on the last syllable)
    // or paroxytone (tonic on the penultimate syllable).
    // At this point, syllableCount must be > 1 because 0 and 1 were handled.
    // Use non-null assertion (!) because 'syllableCount - 1' is guaranteed to be a valid index.
    var lastSyllable = syllables[syllableCount - 1];
    // Regular expression to identify endings that typically make an unaccented word an 'oxytone'
    // (i.e., tonic on the last syllable). These are exceptions to the general rule that unaccented
    // words are paroxytone. The `(\W+)?$` part accounts for optional trailing non-word characters.
    // The 'i' flag makes the match case-insensitive.
    var oxytoneEndingsRegex = /(i(m|n)?(s)?|u(n|m)?(s)?|z|r|l|x|n|ps|om|on(s)?)(\W+)?$/i;
    // If the last syllable matches one of the oxytone endings (e.g., ends in -i, -u, -r, -l, -m, -x, -z, -ps, -ons, etc.),
    // the word is oxytone, and the last syllable is the tonic one.
    if (oxytoneEndingsRegex.test(lastSyllable)) {
        return 1; // Last syllable is tonic (1-indexed from the end).
    }
    // Otherwise (if the last syllable does NOT match the oxytone endings, meaning it typically ends
    // in -a, -e, -o, -em, -ens, etc., without an accent mark), the word is generally paroxytone.
    // This means the penultimate (second to last) syllable is the tonic one.
    return 2; // Penultimate syllable is tonic (2-indexed from the end).
}
