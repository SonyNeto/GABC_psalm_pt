def select_tone(selected_tone):
    tone_dict = {'tone_1d': ['(c4)', '(f)', '(gh)', '(h)', '(h)', '(g)', None, None, '(ixi)', '(h)', '(h)', 1, '(g)', '(h)', '(h)', 1,
               None, '(g)', '(f)', None, None, None, None, '(gh)', '(g)', '(gvFED)', 1],

                 'tone_1d2': ['(c4)', '(f)', '(gh)', '(h)', '(h)', '(g)', None, None, '(ixi)', '(h)', '(h)', 1, '(g)', '(h)', '(h)', 1,
               None, '(g)', '(f)', None, None, None, None, '(gf)', '(g)', '(d)', 2],

                 'tone_1f': ['(c4)', '(f)', '(gh)', '(h)', '(h)', '(g)', None, None, '(ixi)', '(h)', '(h)', 1, '(g)', '(h)', '(h)', 1,
               None, '(g)', '(f)', None, None, None, None, '(gh)', '(g)', '(gf)', 1],

                 'tone_1g': ['(c4)', '(f)', '(gh)', '(h)', '(h)', '(g)', None, None, '(ixi)', '(h)', '(h)', 1, '(g)', '(h)', '(h)', 1,
               None, '(g)', '(f)', None, None, None, None, '(gh)', '(g)', '(g)', 1],

                 'tone_1g2': ['(c4)', '(f)', '(gh)', '(h)', '(h)', '(g)', None, None, '(ixi)', '(h)', '(h)', 1, '(g)', '(h)', '(h)',
               1, None, '(g)', '(f)', None, None, None, None, '(g)', '(g)', '(ghg)', 1],

                 'tone_1g3': ['(c4)', '(f)', '(gh)', '(h)', '(h)', '(g)', None, None, '(ixi)', '(h)', '(h)', 1, '(g)', '(h)', '(h)',
               1, None, '(g)', '(f)', None, None, None, None, '(g)', '(g)', '(g)', 1],

                 'tone_1a': ['(c4)', '(f)', '(gh)', '(h)', '(h)', '(g)', None, None, '(ixi)', '(h)', '(h)', 1, '(g)', '(h)', '(h)', 1,
               None, '(g)', '(f)', None, None, None, None, '(g)', '(h)', '(h)', 1],

                 'tone_1a2': ['(c4)', '(f)', '(gh)', '(h)', '(h)', '(g)', None, None, '(ixi)', '(h)', '(h)', 1, '(g)', '(h)', '(h)',
               1, None, '(g)', '(f)', None, None, None, None, '(g)', '(g)', '(gh)', 1],

                 'tone_1a3': ['(c4)', '(f)', '(gh)', '(h)', '(h)', '(g)', None, None, '(ixi)', '(h)', '(h)', 1, '(g)', '(h)', '(h)',
               1, None, '(g)', '(f)', None, None, None, None, '(gh)', '(g)', '(gh)', 1],

                 'tone_2': ['(f3)', '(e)', '(f)', '(h)', '(h)', '(f)', None, None, None, None, None, None, '(i)', '(h)', '(h)', 1,
               None, None, '(g)', None, None, None, None, '(e)', '(f)', '(f)', 1],

                 'tone_3b': ['(c4)', '(g)', '(hj)', '(j)', '(j)', '(h)', None, None, '(k)', '(j)', '(j)', 1, '(ih)', '(j)', '(j)', 2,
               None, None, '(h)', None, None, None, None, '(j)', '(j)', '(i)', 1],

                 'tone_3a': ['(c4)', '(g)', '(hj)', '(j)', '(j)', '(h)', None, None, '(k)', '(j)', '(j)', 1, '(ih)', '(j)', '(j)', 2,
               None, None, '(h)', None, None, None, None, '(j)', '(j)', '(ih)', 1],

                 'tone_3a2': ['(c4)', '(g)', '(hj)', '(j)', '(j)', '(h)', None, None, '(k)', '(j)', '(j)', 1, '(ih)', '(j)', '(j)', 2,
               None, '(ji)', '(hi)', None, None, None, '(h)', '(g)', '(gh)', 1],

                 'tone_3g': ['(c4)', '(g)', '(hj)', '(j)', '(j)', '(h)', None, None, '(k)', '(j)', '(j)', 1, '(ih)', '(j)', '(j)', 2,
               None, '(ji)', '(hi)', None, None, None, None, '(h)', '(g)', '(g)', 1],

                 'tone_3g2': ['(c4)', '(g)', '(hj)', '(j)', '(j)', '(h)', None, None, '(k)', '(j)', '(j)', 1, '(ih)', '(j)', '(j)', 2,
               '(h)', '(j)', '(i)', None, None, None, None, '(h)', '(g)', '(gh)', 1],

                 'tone_4': ['(c4)', '(h)', '(gh)', '(h)', '(h)', '(g)', '(g)', '(h)', None, None, None, 1, '(i)', '(h)', '(h)', 1,
               None, None, None, None, None, None, None, '(h)', '(g)', '(g)', 1],

                 'tone_4e': ['(c4)', '(h)', '(gh)', '(h)', '(h)', '(g)', '(g)', '(h)', None, None, None, 1, '(i)', '(h)', '(h)', 1,
               '(g)', '(h)', '(ih)', None, None, None, None, '(gf)', '(g)', '(e)', 2],

                 'tone_4alt_c': ['(c3)', '(i)', '(hi)', '(i)', '(i)', '(h)', '(h)', '(g)', None, None, None, 1, '(j)', '(i)', '(i)', 1,
               None, None, None, None, None, None, None, '(i)', '(h)', '(h)', 1],

                 'tone_4alt_a': ['(c3)', '(i)', '(hi)', '(i)', '(i)', '(h)', '(h)', '(g)', None, None, None, 1, '(i)', '(h)', '(h)', 1,
               '(h)', '(i)', '(j)', None, None, None, None, '(h)', '(f)', '(f)', 1],

                 'tone_4alt_a2': ['(c3)', '(i)', '(hi)', '(i)', '(i)', '(h)', '(h)', '(g)', None, None, None, 1, '(i)', '(h)', '(h)',
               1, '(h)', '(i)', '(j)', None, None, None, None, '(h)', '(f)', '(fg)', 1],

                 'tone_4alt_d': ['(c3)', '(i)', '(hi)', '(i)', '(i)', '(h)', '(h)', '(g)', None, None, None, 1, '(i)', '(h)', '(h)',
               1, '(h)', '(i)', '(j)', None, None, None, None, '(h)', '(i)', '(i)', 1],

                 'tone_5': ['(c3)', '(d)', '(f)', '(h)', '(h)', '(f)', None, None, None, None, None, None, '(i)', '(h)', '(h)', 1,
               None, None, None, '(i)', '(g)', '(g)', 1, '(h)', '(f)', '(f)', 1],

                 'tone_6': ['(c4)', '(f)', '(gh)', '(h)', '(h)', '(g)', None, None, '(ixi)', '(h)', '(h)', 1, '(g)', '(h)', '(h)', 1,
               None, '(f)', '(gh)', None, None, None, None, '(g)', '(f)', '(f)', 1],

                 'tone_6alt': ['(c4)', '(f)', '(gh)', '(h)', '(h)', '(g)', None, '(g)', None, None, None, None, '(h)', '(f)', '(f)', 1,
               None, '(f)', '(gh)', None, None, None, None, '(g)', '(f)', '(f)', 1],

                 'tone_7a': ['(c3)', '(hg)', '(hi)', '(i)', '(i)', '(h)', None, None, '(k)', '(j)', '(j)', 1, '(i)', '(j)', '(j)', 1,
               None, None, None, '(j)', '(i)', '(i)', 1, '(h)', '(h)', '(gf)', 1],

                 'tone_7b': ['(c3)', '(hg)', '(hi)', '(i)', '(i)', '(h)', None, None, '(k)', '(j)', '(j)', 1, '(i)', '(j)', '(j)', 1,
               None, None, None, '(j)', '(i)', '(i)', 1, '(h)', '(h)', '(g)', 1],

                 'tone_7c': ['(c3)', '(hg)', '(hi)', '(i)', '(i)', '(h)', None, None, '(k)', '(j)', '(j)', 1, '(i)', '(j)', '(j)', 1,
               None, None, None, '(j)', '(i)', '(i)', 1, '(h)', '(h)', '(gh)', 1],

                 'tone_7c2': ['(c3)', '(hg)', '(hi)', '(i)', '(i)', '(h)', None, None, '(k)', '(j)', '(j)', 1, '(i)', '(j)', '(j)', 1,
               None, None, None, '(j)', '(i)', '(i)', 1, '(h)', '(h)', '(ih)', 1],

                 'tone_7d': ['(c3)', '(hg)', '(hi)', '(i)', '(i)', '(h)', None, None, '(k)', '(j)', '(j)', 1, '(i)', '(j)', '(j)', 1,
               None, None, None, '(j)', '(i)', '(i)', 1, '(h)', '(h)', '(gi)', 1],

                 'tone_8g': ['(c4)', '(g)', '(h)', '(j)', '(j)', '(h)', None, None, None, None, None, None, '(k)', '(j)', '(j)', 1,
               None, '(i)', '(j)', None, None, None, None, '(h)', '(g)', '(g)', 1],

                 'tone_8g2': ['(c4)', '(g)', '(h)', '(j)', '(j)', '(h)', None, None, None, None, None, None, '(k)', '(j)', '(j)', 1,
               None, '(i)', '(j)', None, None, None, None, '(h)', '(g)', '(gh)', 1],

                 'tone_8c': ['(c4)', '(g)', '(h)', '(j)', '(j)', '(h)', None, None, None, None, None, None, '(k)', '(j)', '(j)', 1,
               None, '(h)', '(j)', None, None, None, None, '(k)', '(j)', '(j)', 1],

                 'tp': ['(c3)', '(e)', '(f)', '(h)', '(h)', '(f)', None, '(i)', None, None, None, None, '(i)', '(f)', '(f)', 1,
               None, '(e)', '(f)', None, None, None, None, '(g)', '(f)', '(f)', 1]}

    for tone, tone_info in tone_dict.items():
        if tone == selected_tone:
            return tone_info