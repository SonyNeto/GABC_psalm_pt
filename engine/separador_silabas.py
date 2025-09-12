import subprocess

def syllabifier(word: str):
    output = subprocess.run(
        ["bun", "separador-silabas-main/cli.js", "--word", word],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    output = output.stdout.split('\n')
    output = list(filter(None, output))

    stress_syllable_index = int(output[-1])
    word = output[0].split('-')
    for syllable in word:
        if word.index(syllable) == len(word) - stress_syllable_index:
            word[word.index(syllable)] = '[' + syllable + ']'
    word = '-'.join(word)
    return word