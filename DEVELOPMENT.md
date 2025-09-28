# Development Setup Guide

## Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SHYAMALSOLANKI/PB2S-PB2A-watever-agentic_framework.git
   cd PB2S-PB2A-watever-agentic_framework
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install in development mode:**
   ```bash
   pip install -e .
   ```

## Running Tests

```bash
# Run all tests
python -m unittest discover tests/

# Run specific test file
python -m unittest tests.test_pb2s_framework
```

## Project Structure

```
agentic_pb2s/
├── instruction_agentic_code_suit_Architecture.py  # Main architecture entry point
├── requirements.txt                                # Project dependencies
├── README.md                                      # Project documentation
├── setup.py                                       # Package installation script
├── core/                                          # Core framework components
│   ├── __init__.py                               # Core package init
│   ├── pb2s_framework.py                         # Main PB2S recursion logic
│   ├── suit_engine.py                            # Validation engine
│   ├── schema_definitions.py                     # JSON schema definitions
│   └── sandbox_manager.py                        # Runtime environment manager
├── extensions/                                    # Framework extensions
│   ├── __init__.py                               # Extensions package init
│   ├── api_connectors.py                         # API integration ports
│   ├── plugins.py                                # Plugin system
│   └── schemas/                                  # Extension schemas
│       ├── __init__.py                           # Schemas package init
│       └── example_extension_schema.json         # Example schema definition
└── tests/                                        # Test suite
    ├── __init__.py                               # Tests package init
    ├── test_pb2s_framework.py                    # Framework core tests
    ├── test_suit_engine.py                       # Validation engine tests
    └── test_sandbox.py                           # Sandbox manager tests
```

## Development Guidelines

- Keep modules under 200 lines as specified in the framework rules
- Ensure strict schema adherence
- All code must pass through PB2S validation cycles
- Maintain framework ethos: recursion over shortcuts
- Extensions must integrate via safe ports (APIs, plugins, schemas)

## Package Installation

To install the package in production:

```bash
pip install -e .
```

## Contributing

1. Follow the PB2S framework ethos and rules
2. Ensure all changes maintain recursion and validation requirements
3. Test thoroughly with the existing test suite
4. All integrations must pass through safe integration ports