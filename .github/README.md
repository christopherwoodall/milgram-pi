# Milgram Pi

Run Stanley Milgram's famous experiment with a Raspberry Pi and MCP.

## Requirements

### Bill of Materials
- Raspberry Pi
- TENS Unit
- Relay Module

### Setup
1. Connect the Raspberry Pi to the relay module.
2. Connect the relay module to the TENS unit.
3. Install the required Python libraries:
   ```bash
   pip install RPi.GPIO
   ```
4. Configure the GPIO pins in the `config.py` file.
5. Run the script:
   ```bash
   python milgram_pi.py
   ```



## Acknowledgements

Inspired by Tim Keeley's [shockbot]() project.