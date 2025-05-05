import re

def extract_spinel_props(filename):
    constants = {}
    key_map = {}

    define_pattern = re.compile(r'^\s*(SPINEL_PROP_[A-Z0-9_]+)\s*=\s*(.+?),?\s*(?://.*)?$')

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            match = define_pattern.match(line)
            if match:
                name, value_expr = match.groups()
                try:
                    # Replace known constants in the expression
                    for const_name, const_val in constants.items():
                        value_expr = value_expr.replace(const_name, str(const_val))
                    # Evaluate the expression safely
                    value = eval(value_expr, {"__builtins__": {}})
                    constants[name] = value
                    if name.startswith("SPINEL_PROP_") and not name.endswith("__BEGIN") and not name.endswith("__END"):
                        key_map[value] = name
                except Exception as e:
                    print(f"Skipping {name} due to error: {e}")

    # Output the dictionary
    print("KEY_MAP = {")
    for key in sorted(key_map):
        print(f"    0x{key:04X}: \"{key_map[key]}\",")
    print("}")

if __name__ == "__main__":
    extract_spinel_props("sys_ep_props.txt")
