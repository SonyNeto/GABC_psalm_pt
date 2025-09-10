import argparse


def cli_parser():
    parser = argparse.ArgumentParser(description='Ferramenta de geração de salmodias em português nos tons salmodicos do Ofício Divino. // Psalm Tone Tool for portuguese language.')
    parser.add_argument('-p','--psalm', type=str, required=True, help='Psalm text file, e.g. -p psalm.txt.')
    parser.add_argument('-t','--tone', type=str, required=True, help='Psalm Tones (L.U.):'
                                                                     'tone_1d, tone_1d2, tone_1f, tone_1g, tone_1g2, tone_1g3, tone_1a, tone_1a2, tone_1a3,'
                                                                     ' tone_2,' 
                                                                     ' tone_3b, tone_3a, tone_3a2, tone_3g, tone_3g2,' 
                                                                     ' tone_4, tone_4e, tone_4alt_c, tone_4alt_a, tone_4alt_a2, tone_4alt_d,' 
                                                                     ' tone_5,' 
                                                                     ' tone_6, tone_6alt,' 
                                                                     ' tone_7a, tone_7b, tone_7c, tone_7c2, tone_7d,' 
                                                                     ' tone_8g, tone_8g2, tone_8c,' 
                                                                     ' tp')
    parser.add_argument('-e','--export', action='store_true', required=False, help='Export to PDF.')
    parser.add_argument('-f','--file', type=str, required=False, help='Name of the file to export.')
    parser.add_argument('-g','--gabc', action='store_true', required=False, help='Print GABC.')

    args = parser.parse_args()

    return args

