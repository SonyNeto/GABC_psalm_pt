def accent_2(hemi_syl: list, pre_note_1, pre_note_2, pre_note_3, accent_note, cava_note, cadence_note, second: bool, second_accent, pattern):
    syl_index = -1
    for syllable in reversed(hemi_syl[-3:]):
        if '[' in syllable:
            if syl_index == -1:
                if '[' in hemi_syl[-5] and '[' not in hemi_syl[-4] and '[' not in hemi_syl[-3] and '[' in hemi_syl[-2] and second_accent != None:
                    hemi_syl[-2] = '<b>' + hemi_syl[-2] + '</b>'
                    hemi_syl[-2] += accent_note
                    hemi_syl[-1] += cadence_note
                elif second:
                    accent_note = accent_note.replace(")", "", 1)
                    cadence_note = cadence_note.replace("(", "", 1)
                    hemi_syl[-1] = '<b>' + hemi_syl[-1] + '</b>'
                    hemi_syl[-1] += accent_note + cadence_note
                # elif '[' in hemi_syl[-4] and '[' not in hemi_syl[-3]:
                #     accent_note = accent_note.replace(")", "", 1)
                #     cadence_note = cadence_note.replace("(", "", 1)
                #     hemi_syl[-1] += accent_note + cadence_note
                # elif '[' in hemi_syl[-5] and hemi_parity == 2:
                #     hemi_syl[-2] += accent_note
                #     hemi_syl[-1] += cadence_note
                elif '[' in hemi_syl[-2]:
                    hemi_syl[-2] = '<b>' + hemi_syl[-2] + '</b>'
                    hemi_syl[-2] += accent_note
                    hemi_syl[-1] += cadence_note
                elif pattern == 2:
                    hemi_syl[-3] = '<b>' + hemi_syl[-3] + '</b>'
                    hemi_syl[-3] += cava_note
                    hemi_syl[-2] += accent_note
                    hemi_syl[-1] += cadence_note
                else:
                    hemi_syl[-3] = '<b>' + hemi_syl[-3] + '</b>'
                    hemi_syl[-3] += accent_note
                    hemi_syl[-2] += cava_note
                    hemi_syl[-1] += cadence_note
            elif syl_index == -2:
                hemi_syl[-2] = '<b>' + hemi_syl[-2] + '</b>'
                hemi_syl[-2] += accent_note
                hemi_syl[-1] += cadence_note
            elif pattern == 2:
                hemi_syl[-3] = '<b>' + hemi_syl[-3] + '</b>'
                hemi_syl[-3] += cava_note
                hemi_syl[-2] += accent_note
                hemi_syl[-1] += cadence_note
            else:
                hemi_syl[-3] = '<b>' + hemi_syl[-3] + '</b>'
                hemi_syl[-3] += accent_note
                hemi_syl[-2] += cava_note
                hemi_syl[-1] += cadence_note
            break
        elif syl_index == -3:
            hemi_syl[syl_index + 1] = '<b>' + hemi_syl[syl_index + 1] + '</b>'
            hemi_syl[syl_index + 1] += accent_note
            hemi_syl[-1] += cadence_note
        syl_index += -1

    syl_index = 0
    if pre_note_3 != None:
        for syllable in reversed(hemi_syl):
            if '(' not in syllable:
                hemi_syl[len(hemi_syl) - 1 - syl_index] += pre_note_3
                break
            syl_index += 1
    syl_index = 0
    if pre_note_2 != None:
        for syllable in reversed(hemi_syl):
            if '(' not in syllable:
                hemi_syl[len(hemi_syl) - 1 - syl_index] += pre_note_2
                break
            syl_index += 1
    syl_index = 0
    if pre_note_1 != None:
        for syllable in reversed(hemi_syl):
            if '(' not in syllable:
                hemi_syl[len(hemi_syl) - 1 - syl_index] += pre_note_1
                break
            syl_index += 1

    return hemi_syl
