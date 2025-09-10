from cli.cli import cli_parser
from tones.tones import select_tone
from compiler.compiler import compiler
from engine.psalm_generator import psalm_generator

if __name__ == '__main__':
    args = cli_parser()
    tone = select_tone(args.tone)
    with open(args.psalm, 'r', encoding = 'utf-8') as psalm_file:
        psalm = psalm_file.read()
    if args.export:
        compiler(psalm_generator(psalm, *tone), args.file)
    elif args.gabc:
        print(psalm_generator(psalm, *tone))
    else:
        print('Nothing happened, :( Try to export PDF or print GABC.')