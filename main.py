import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Compile domain list into unbound config",
    )
    parser.add_argument(
        "-i",
        "--input-file",
        help="Name of a file with line separated domains",
        required=True,
    )
    parser.add_argument(
        "-o",
        "--output-file",
        help="Name of an output file where generated config will be saved",
        required=True,
    )
    args = parser.parse_args()

    with open(args.input_file, "rt", encoding="utf-8") as in_file, open(
        args.output_file, "wt", encoding="utf-8"
    ) as out_file:
        out_file.write("server:\n")
        for line in in_file:
            domain = line.strip()
            if len(domain) == 0:
                continue
            print(domain)
            out_file.write(f'\tlocal-zone: "{domain}" always_null\n')


if __name__ == "__main__":
    main()
