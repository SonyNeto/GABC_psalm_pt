"use strict";
// @filename: syllable.ts
/**
 * Separates the word using pt-br standard
 *
 * @param word The word to be separated
 * @returns The word separated by '@' characters
 */
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
exports.default = syllable;
var VOGAIS_FRACAS = "iouïöüy";
var VOGAIS_FORTES = "aeáéóàèòãẽõâêôäëöíúìùĩũîû";
var CONSOANTES_FORTES = "bcdfgjkpqtvwxyzç";
var CONSOANTES_LIQUIDAS = "lr";
var CONSOANTES_NASAIS = "mn";
var VOGAIS = VOGAIS_FRACAS + VOGAIS_FORTES + "e";
var CONSOANTES = CONSOANTES_FORTES + CONSOANTES_LIQUIDAS + CONSOANTES_NASAIS + "s";
var CONSOANTES_FRACAS = CONSOANTES_LIQUIDAS + CONSOANTES_NASAIS + "s";
var LETRAS = VOGAIS + CONSOANTES;
var DIGRAFOS = ["ch", "lh", "nh", "gu", "qu"];
function is_digraph(text, pos) {
    for (var _i = 0, DIGRAFOS_1 = DIGRAFOS; _i < DIGRAFOS_1.length; _i++) {
        var digraph = DIGRAFOS_1[_i];
        if (text.substring(pos, pos + digraph.length) === digraph) {
            return [true, digraph];
        }
    }
    return [false, null];
}
function text_to_chars(text) {
    var chars = [];
    var i = 0;
    while (i < text.length) {
        var _a = is_digraph(text, i), isDig = _a[0], digraph = _a[1];
        if (isDig) {
            chars.push("@" + digraph);
            i += digraph.length;
        }
        else {
            // Handle UTF-8 characters (TypeScript strings are UTF-16, but this handles common cases)
            // For full Unicode grapheme cluster support, a library might be needed.
            var char = text.charAt(i);
            chars.push(char);
            i += char.length;
        }
    }
    return chars;
}
function char_in_set(char, set_spec) {
    return set_spec.includes(char);
}
function match_pattern(chars, pos, pattern) {
    if (pos < 0 || pos + pattern.length > chars.length) {
        return false;
    }
    for (var i = 0; i < pattern.length; i++) {
        var pattern_char = pattern[i];
        var actual_char = chars[pos + i];
        if (pattern_char === "@") {
            if (actual_char !== "@") {
                return false;
            }
        }
        else if (!char_in_set(actual_char, pattern_char)) {
            return false;
        }
    }
    return true;
}
function create_rule(chars, index) {
    var newChars = __spreadArray([], chars, true);
    newChars.splice(index, 0, "@");
    return newChars;
}
function cleanup_rule(chars, index) {
    var newChars = __spreadArray([], chars, true);
    newChars.splice(index, 1);
    return newChars;
}
var SYLLABIFICATION_RULES = [
    { position: 1, pattern: [VOGAIS, "o"] },
    { position: 1, pattern: [VOGAIS_FRACAS, VOGAIS_FORTES] },
    { position: 1, pattern: ["aeí", VOGAIS_FORTES] },
    { position: 0, pattern: [CONSOANTES_FORTES] },
    { position: 0, pattern: [CONSOANTES_FRACAS, VOGAIS] },
    { position: 0, pattern: ["bd", "s"] },
];
var CLEANUP_RULES = [
    { position: 2, pattern: [CONSOANTES_FORTES, "@", CONSOANTES_LIQUIDAS] },
    { position: 1, pattern: ["@", CONSOANTES_FORTES, "@", CONSOANTES_NASAIS + "s"] },
    { position: 1, pattern: ["@", CONSOANTES_FORTES, "@", CONSOANTES_FORTES] },
    { position: 2, pattern: ["ã", "@", "o"] },
];
function syllabify_letters(word) {
    var lowerWord = word.toLowerCase();
    var chars = text_to_chars(lowerWord);
    var exceptions = ["ao", "aos", "caos"];
    for (var i = 0; i < exceptions.length; i++) {
        if (lowerWord == exceptions[i]) {
            return word;
        }
    }
    if (chars.length <= 1) {
        return word;
    }
    // Apply syllabification rules
    var separators = {};
    for (var i = 0; i < chars.length - 1; i++) {
        for (var _i = 0, SYLLABIFICATION_RULES_1 = SYLLABIFICATION_RULES; _i < SYLLABIFICATION_RULES_1.length; _i++) {
            var rule = SYLLABIFICATION_RULES_1[_i];
            if (match_pattern(chars, i, rule.pattern)) {
                var insert_pos = i + rule.position;
                if (insert_pos >= 0 && insert_pos <= chars.length) {
                    separators[insert_pos] = true;
                    break; // Apply first matching rule at each position
                }
            }
        }
    }
    // Insert separators
    var result_chars = [];
    for (var i = 0; i < chars.length; i++) {
        var charToPush = chars[i];
        if (charToPush !== undefined) {
            result_chars.push(chars[i]);
        }
        var separatorValue = separators[i + 1];
        if (separatorValue === true && i < chars.length - 1) {
            result_chars.push("@");
        }
    }
    // Apply cleanup rules
    var processedChars = result_chars;
    for (var _a = 0, CLEANUP_RULES_1 = CLEANUP_RULES; _a < CLEANUP_RULES_1.length; _a++) {
        var rule = CLEANUP_RULES_1[_a];
        // Iterate from the end to avoid issues with changing array length
        for (var i = processedChars.length - rule.pattern.length; i >= 0; i--) {
            if (match_pattern(processedChars, i, rule.pattern)) {
                var atIndexInPattern = -1;
                for (var k = 0; k < rule.pattern.length; k++) {
                    if (rule.pattern[k] === '@') {
                        atIndexInPattern = k;
                        break;
                    }
                }
                if (atIndexInPattern !== -1) {
                    processedChars = cleanup_rule(processedChars, i + atIndexInPattern);
                }
            }
        }
    }
    // Post-processing (as new rules or direct string manipulations)
    var finalResult = processedChars.join("");
    finalResult = finalResult.replace(/([aeou])(i[nmrlz])$/, "$1@$2");
    finalResult = finalResult.replace(/@bs@/g, "bs@");
    finalResult = finalResult.replace(/([aei])([oui])([mn])/g, "$1@$2$3");
    finalResult = finalResult.replace(/([aeo])in/g, "$1@in");
    finalResult = finalResult.replace(/([aeou])i@nh/g, "$1@i@nh");
    finalResult = finalResult.replace(/@+/g, "@");
    finalResult = finalResult.replace(/^@/g, "");
    return finalResult;
}
function syllable(word) {
    if (word.includes('-')) {
        return word.split('-').map(function (part) { return syllable(part); }).join('-@');
    }
    var originalChars = text_to_chars(word);
    var letterChars = [];
    originalChars.forEach(function (char) {
        if (char_in_set(char.toLowerCase(), LETRAS)) {
            letterChars.push(char);
        }
    });
    if (letterChars.length === 0) {
        return word;
    }
    var letterWord = letterChars.join('');
    var syllabifiedLetterWord = syllabify_letters(letterWord);
    var syllabifiedLetterChars = text_to_chars(syllabifiedLetterWord);
    var finalChars = [];
    var syllabifiedCursor = 0;
    for (var _i = 0, originalChars_1 = originalChars; _i < originalChars_1.length; _i++) {
        var originalChar = originalChars_1[_i];
        if (char_in_set(originalChar.toLowerCase(), LETRAS)) {
            while (syllabifiedCursor < syllabifiedLetterChars.length &&
                (syllabifiedLetterChars[syllabifiedCursor] === '@' || syllabifiedLetterChars[syllabifiedCursor] === '-')) {
                finalChars.push(syllabifiedLetterChars[syllabifiedCursor]);
                syllabifiedCursor++;
            }
            finalChars.push(originalChar);
            if (syllabifiedCursor < syllabifiedLetterChars.length &&
                syllabifiedLetterChars[syllabifiedCursor].toLowerCase() === originalChar.toLowerCase()) {
                syllabifiedCursor++;
            }
        }
        else {
            finalChars.push(originalChar);
        }
    }
    while (syllabifiedCursor < syllabifiedLetterChars.length) {
        var char = syllabifiedLetterChars[syllabifiedCursor];
        if (char === '@' || char === '-') {
            finalChars.push(char);
        }
        syllabifiedCursor++;
    }
    var finalResult = finalChars.join('');
    finalResult = finalResult.replace(/@d@q/g, "d@q");
    finalResult = finalResult.replace(/([gq])u@([ei])/g, "$1u$2");
    finalResult = finalResult.replace(/@([sn])@([qg])/g, "$1@$2");
    finalResult = finalResult.replace(/@([cnl]h)@([aeiou])/g, "@$1$2");
    finalResult = finalResult.replace(/-/g, "-@");
    finalResult = finalResult.replace(/@+/g, "@");
    return finalResult;
}
