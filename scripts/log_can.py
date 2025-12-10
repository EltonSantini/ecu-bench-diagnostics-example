import argparse
import can
import os


def main():
    parser = argparse.ArgumentParser(description="Log CAN traffic to a file.")
    parser.add_argument("--channel", required=True, help="CAN channel, e.g. vcan0 or can0")
    parser.add_argument("--bitrate", type=int, default=500000)
    parser.add_argument("--outfile", required=True, help="Output log file path")
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.outfile), exist_ok=True)

    bus = can.interface.Bus(channel=args.channel, bustype="socketcan", bitrate=args.bitrate)

    print(f"Logging CAN traffic on {args.channel} to {args.outfile} (Ctrl+C to stop)...")
    with open(args.outfile, "w", encoding="utf-8") as f:
        try:
            for msg in bus:
                line = f"{msg.timestamp},{msg.arbitration_id:03X},{msg.dlc},{msg.data.hex()}\n"
                f.write(line)
                f.flush()
        except KeyboardInterrupt:
            print("Stopping logging.")


if __name__ == "__main__":
    main()
