import argparse
import pyminifier

def ofs_file(file_a, file_b, level, of_vars, of_func, of_class):
    with open(file_a, "r") as f:
        script = f.read()

    sop = pyminifier.remove_comments_and_docstrings(script)

    if of_vars:
        level = max(level, 1)
    if of_func:
        level = max(level, 2)
    if of_class:
        level = max(level, 2)

    of_script = pyminifier.obfuscate(sop, rn_lvl=level,rn_glo=of_vars, rn_func=of_func, rn_cls=of_class)

    with open(file_b, "w") as f:
        f.write(of_script)

def val_args(args):
    if not args.file_a:
        raise ValueError("file_a not found")
    if not args.file_b:
        raise ValueError("file_b not found")
    if not args.level in [1, 2, 3]:
        raise ValueError("level not found")
    if not  any([args.vars, args.func, args.clas]):
        raise ValueError("-v -f -c not found")
    
if __name__ == "__main__":
    hp = argparse.ArgumentParser(desc="script que no tiene un uso aparente y no sirve para nada en un entorno real mas que joder al creador que esta programando esto :D")#moraa404
    hp.add_argument("-a", "--input", help="Archovo de Entrada")
    hp.add_argument("-o", "--output", help="Archivo de Salida")
    hp.add_argument("-l", "--level", type=int, default=0, help="Nivel de ofuscacion ( 1 = vars / 2 = vars + func / 3 = vars + func + class )")
    hp.add_argument("-v", "--variables", action="store_true", help="Ofuscar nombres de variables")
    hp.add_argument("-f", "--functions", action="store_true", help="Ofuscar nombres de Funciones")
    hp.add_argument("-c", "--classes", action="store_true", help="Ofuscar nombres de Clases")
    args = hp.parse_args()

    try:
        val_args(args)
        ofs_file(args.file_a, args.file_b, args.level, args.vars, args.func, args.clas)
    except ValueError as e:
        print(str(e))
        
