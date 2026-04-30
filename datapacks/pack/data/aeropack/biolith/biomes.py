import toml
import json

DIMENSION = "minecraft:overworld"

def expand_replacements(toml_data):
    output = {"replacements": []}

    for category, data in toml_data.items():
        biomes = data.get("biomes", [])
        replacements = data.get("replacements", [])

        for target in biomes:
            for repl in replacements:
                entry = {
                    "dimension": DIMENSION,
                    "target": target,
                    "biome": repl
                }
                output["replacements"].append(entry)

    return output


if __name__ == "__main__":
    with open("./biomes.toml", "r") as f:
        toml_data = toml.load(f)

    result = expand_replacements(toml_data)

    with open("replacements.json", "w") as f:
        json.dump(result, f, indent=2)

    print("Done.")