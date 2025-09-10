from PETRUS_master.g2p.g2p import G2PTranscriber
import re
from engine.accents_pattern import accent_2


# psalm = ('''Quando vos invoco, respondei-me, ó Deus de minha justiça† vós que na hora da angústia me reconfortastes * Tende piedade de mim e ouvi minha oração
# Ó poderosos, até quando tereis o coração endurecido * no amor das vaidades e na busca da mentira
# O Senhor escolheu como eleito uma pessoa admirável * o Senhor me ouviu quando o invoquei
# Tremei, mas sem pecar† refleti em vossos corações * quando estiverdes em vossos leitos, e calai
# Oferecei vossos sacrifícios * com sinceridade e esperai no Senhor
# Dizem muitos: Quem nos fará ver a felicidade* Fazei brilhar sobre nós, Senhor, a luz de vossa face
# Pusestes em meu coração mais alegria * do que quando abundam o trigo e o vinho
# Apenas me deito, logo adormeço em paz * porque a segurança de meu repouso vem de vós só, Senhor
# Glória ao Pai, e ao Filho * e ao Espírito Santo
# assim como era no príncipio, agora e sempre * e por todos os séculos dos séculos. Amém''')

def psalm_generator(psalm, clef, int_1, int_2, ten, flex_1, flex_2, pre_med_1, pre_med_2, med_accent_1, med_cava_1, med_cadence_1, med_pattern_1, med_accent_2, med_cava_2, med_cadence_2, med_pattern_2, pre_fin_1, pre_fin_2, pre_fin_3, fin_accent_1, fin_cava_1, fin_cadence_1, fin_pattern_1, fin_accent_2, fin_cava_2, fin_cadence_2, fin_pattern_2):
    hemistichs = re.split(r"[*\n]", psalm)
    hemistichs_words = []
    for hemistich in hemistichs:
        hemistichs_words.append(hemistich.split())

    syllables = []
    hemistichs_syllables = []
    for hemistique in hemistichs_words:
        for word in hemistique:
            word_syllables = G2PTranscriber(word, algorithm="ceci").get_syllables_with_stress_boundaries()
            word_syllables = re.findall(r'.+?-|.+', word_syllables)
            syllables += word_syllables
        hemistichs_syllables.append(syllables)
        syllables = []
    hemistichs_with_gabc = []
    for hemistich in hemistichs_syllables:
        if hemistichs_syllables.index(hemistich) %2 == 0:# Para os hemistíquos com índice par (primeiros de cada versículo)
            if med_accent_1 != None:
                hemistich_with_gabc = accent_2(hemistich, pre_med_1, pre_med_2, None, med_accent_2, med_cava_2, med_cadence_2, True, med_accent_1, med_pattern_2)
                hemistich_less_first_cadence = []
                first_cadence = []
                for syllable in hemistich_with_gabc:
                    if '(' not in syllable:
                        hemistich_less_first_cadence.append(syllable)
                    else:
                        first_cadence.append(syllable)
                hemistich_with_gabc = accent_2(hemistich_less_first_cadence, pre_med_1, pre_med_2, None, med_accent_1, med_cava_1, med_cadence_1, False, med_accent_1, med_pattern_1) + first_cadence
            else:
                hemistich_with_gabc = accent_2(hemistich, pre_med_1, pre_med_2, None, med_accent_2, med_cava_2, med_cadence_2, True, med_accent_1, med_pattern_2)

            # Introdução
            for syllable in hemistich_with_gabc:
                if hemistich_with_gabc.index(syllable) == 0 and '(' not in syllable:
                    hemistich_with_gabc[0] = syllable + int_1
                elif hemistich_with_gabc.index(syllable) == 1 and '(' not in syllable:
                    hemistich_with_gabc[1] = syllable + int_2
            #Flexa
            for syllable in hemistich_with_gabc:
                if '†' in syllable:
                    hemistich_with_gabc = accent_2(hemistich_with_gabc[:hemistich_with_gabc.index(syllable) + 1], None, None, None, flex_1, flex_1, flex_2, True, False, 1) + hemistich_with_gabc[hemistich_with_gabc.index(syllable) + 1:] #Flexas só tem 1 acento
            # Tenor
            for syllable in hemistich_with_gabc:
                if '(' not in syllable:
                    hemistich_with_gabc[hemistich_with_gabc.index(syllable)] = syllable + ten
            hemistichs_with_gabc.append(hemistich_with_gabc)

        elif hemistichs_syllables.index(hemistich) % 2 != 0:  # Para os hemistíquos com índice ímpar (segundos de cada versículo)
            if fin_accent_1 != None:
                hemistich_with_gabc = accent_2(hemistich, pre_fin_1, pre_fin_2, pre_fin_3, fin_accent_2, fin_cava_2, fin_cadence_2, True, fin_accent_1, fin_pattern_2)
                hemistich_less_first_cadence = []
                first_cadence = []
                for syllable in hemistich_with_gabc:
                    if '(' not in syllable:
                        hemistich_less_first_cadence.append(syllable)
                    else:
                        first_cadence.append(syllable)
                hemistich_with_gabc = accent_2(hemistich_less_first_cadence, pre_fin_1, pre_fin_2, pre_fin_3, fin_accent_1, fin_cava_1, fin_cadence_1, False, fin_accent_1, fin_pattern_1) + first_cadence
            else:
                hemistich_with_gabc = accent_2(hemistich, pre_fin_1, pre_fin_2, pre_fin_3, fin_accent_2, fin_cava_2, fin_cadence_2, True, fin_accent_1, fin_pattern_2)

            # Tenor
            for syllable in hemistich_with_gabc:
                if '(' not in syllable:
                    hemistich_with_gabc[hemistich_with_gabc.index(syllable)] = syllable + ten
            hemistichs_with_gabc.append(hemistich_with_gabc)

    psalm_gabc = f"""
name: psalm;
user-notes: ;
commentary: ;
annotation: ;
centering-scheme: english;
%fontsize: 12;
%spacing: vichi;
%font: OFLSortsMillGoudy;
%width: 4.5;
%height: 11;
%%
{clef} """

    for hemistich in hemistichs_with_gabc:
        for syllable in hemistich:
            if '-' in syllable:
                syllable = syllable.replace("-", "", 1)
            else:
                syllable += ' '
            if '[' in syllable:
                syllable = syllable.replace("[", "", 1)
                syllable = syllable.replace("]", "", 1)
            psalm_gabc += syllable
        psalm_gabc += ('(:)')
    #print(psalm_gabc)
    return psalm_gabc

# if __name__ == '__main__':
#     compiler(psalm_generator(*mode_pasc), 'psalm_4_pascal')