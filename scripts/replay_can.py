import argparse
import can
import time


def main():
    parser = argparse.ArgumentParser(description="Replay CAN traffic from a log file.")
    parser.add_argument("--channel", required=True, help="CAN channel, e.g. vcan0 or can0")
    parser.add_argument("--bitrate", type=int, default=500000)
    parser.add_argument("--infile", required=True, help="Input log file path")
    args = parser.parse_args()

    bus = can.interface.Bus(channel=args.channel, bustype="socketcan", bitrate=args.bitrate)

    print(f"Replaying CAN traffic from {args.infile} on {args.channel}...")
    with open(args.infile, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            ts, arb_id_hex, dlc_str, data_hex = line.split(",")
            arb_id = int(arb_id_hex, 16)
            data_bytes = bytes.fromhex(data_hex)
            msg = can.Message(arbitration_id=arb_id, data=data_bytes, is_extended_id=False)
            bus.send(msg)
            time.sleep(0.01)

    print("Replay complete.")


if __name__ == "__main__":
    main()
