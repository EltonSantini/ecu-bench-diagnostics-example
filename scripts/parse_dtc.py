import argparse


def main():
    parser = argparse.ArgumentParser(description="Parse DTC-like frames from CAN log.")
    parser.add_argument("--infile", required=True, help="Input log file path")
    args = parser.parse_args()

    dtc_frames = []
    with open(args.infile, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) != 4:
                continue
            ts, arb_id_hex, dlc_str, data_hex = parts
            arb_id = int(arb_id_hex, 16)
            if arb_id == 0x700:
                dtc_frames.append((ts, data_hex))

    print("DTC frames (generic example):")
    for ts, data_hex in dtc_frames:
        print(f"{ts}: {data_hex}")


if __name__ == "__main__":
    main()
