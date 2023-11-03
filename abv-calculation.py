import argparse

# From ASBC Approved Methods – Conversion Tables. Extract to Specific Gravity
def plato_to_sg(plato: float) -> float:
    sg = 1 + (plato / (258.6 - ((plato / 258.2) * 227.1)))
    return sg

#  From ASBC Approved Methods - Conversion Tables. Specific Gravity to Apparent Extract
def sg_to_plato(sg: float) -> float:
    plato = (-463.371) + (668.718 * sg) - (205.347 * (sg ** 2))
    return plato

# ABV Calculation
def calculate_abv(target_abv: float, og: float, fg: float) -> float:
    # Type and range checking
    try:
        target_abv = float(target_abv)
        og = float(og)
        fg = float(fg)
    except ValueError as e:
        raise ValueError("Target ABV, OG, and FG must be floats") from e
    
    if target_abv < 0.0 or target_abv > 20.0:
        raise ValueError("Target ABV must be between 0.0 and 20.0")
    
    # Conversion to SG
    og_sg = plato_to_sg(og)
    fg_sg = plato_to_sg(fg)
    
    # ABV calculation based on target ABV
    if target_abv <= 8.0:
        calculated_abv = (og_sg - fg_sg) * 131.25
    else:
        calculated_abv = (76.08 * (og_sg - fg_sg) / (1.775 - og_sg)) * (fg_sg / 0.794)
    
    return f"{calculated_abv:.2f} %"
    
# Arg parser
def argument_parser():
    parser = argparse.ArgumentParser(description="Calculate ABV from OG and FG")
    parser.add_argument("-t", "--targetabv", type=float, help="Target ABV")
    parser.add_argument("-o", "--og", type=float, help="Original Gravity")
    parser.add_argument("-f", "--fg", type=float, help="Final Gravity")
    return parser.parse_args()

if __name__ == "__main__":
    # Parse and validate args
    args = argument_parser()
    if args.targetabv is None or args.og is None or args.fg is None:
        print("Provide all required arguments. Use '-h' for help.")
        exit(1)
    
    # print calculated ABV
    print(calculate_abv(args.targetabv, args.og, args.fg))