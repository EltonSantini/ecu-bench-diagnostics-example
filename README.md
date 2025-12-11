# ECU Bench Diagnostics – Example Setup

A **generic example** of how to structure scripts and docs for an **ECU-style bench setup** using a controller on the bench.

Focus areas:
- Bench test environment design
- CAN logging and replay
- Simple DTC-style parsing

> All configurations, signal names, and logs in this repo are **fictional** and for demonstration only.

---

## 🚀 Quickstart

```bash
> Ensure you have a `requirements.txt` file in the project root directory.  
> Example contents:
> ```
> python-can
> pandas
> ```
pip install -r requirements.txt
python scripts/log_can.py --channel vcan0 --outfile logs/session_01.log
python scripts/parse_dtc.py --infile logs/session_01.log
```

See docs for more details.

---

## 📄 License

MIT.
