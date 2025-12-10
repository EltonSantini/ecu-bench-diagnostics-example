# Example Test Plan (Generic ECU Bench)

1. Power-on sanity check
2. CAN communication check (no errors on bus)
3. Simulate sensor input A and verify ECU response on CAN
4. Inject DTC by toggling signal in `signals_example.yaml`
5. Log CAN traffic and verify DTC frame appears
6. Clear condition and verify DTC no longer appears
