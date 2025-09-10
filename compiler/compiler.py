import subprocess

def compiler(gabc_code: str, file_name: str) -> None:

    with open(f"{file_name}.gabc", "w", encoding="utf-8") as f:
        f.write(gabc_code)

    tex_content = f"""
    \\documentclass[a4paper,12pt]{{article}}
    \\usepackage[autocompile]{{gregoriotex}}
    \\usepackage{{fullpage}}
    \\begin{{document}}
    \\gregorioscore{{{file_name}}}
    \\end{{document}}
    """
    with open(f"{file_name}.tex", "w", encoding="utf-8") as f:
                f.write(tex_content)

    subprocess.run(["lualatex", f"{file_name}.tex"])

    subprocess.Popen([f"{file_name}.pdf"], shell=True)
