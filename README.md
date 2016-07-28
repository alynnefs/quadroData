# quadroData
Simulated data API for testing smart breaker board applications.

## Usage
- **GET** `/breaker` - Use this to check the breaker state.
- **POST** `/breaker` - Use this to change the breaker state. The param `estado` should be setted.
- **GET** `/current` - Use this to check the current value.
- **GET** `/voltage` - Use this to check the voltage value.

All output data should be considered JSON.

