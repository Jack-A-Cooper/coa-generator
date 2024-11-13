# Coats of Arms Generator
> A tool to create personalized coats of arms with historical heraldic rules.

## Table of Contents
- [Installation](#installation)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Configuration](#configuration)
- [Source Documentation](#Source-Documentation)
- [Directory Structure](#Directory-Structure)
- [Development](#development)
- [Contributing](#contributing)
- [Versioning](#versioning)
- [Authors and Acknowledgment](#authors-and-acknowledgment)
- [License](#license)
- [Screenshots / Demo](#screenshots--demo)
- [FAQs / Common Issues](#faqs--common-issues)
- [Changelog](#changelog)
- [Support or Contact](#support-or-contact)

## Installation
To install the Coats of Arms Generator, follow these steps:

```bash
### Clone the repository
git clone https://github.com/Jack-A-Cooper/coa-generator.git

### Navigate to the repository
cd coa-generator

### Run the setup script
#### On Linux/MacOS:
./setup.sh
#### On Windows:
setup.bat
```

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.x
- pip (Python package installer)

## Usage
To use the Coats of Arms Generator, run the following command:

\```bash
python main.py
\```

***or use the .bat files to run***

Refer to the [user guide](USER_GUIDE.md) for more detailed instructions on usage.

## Source Documentation
```
- `coa-generator/`: The root directory of the project related to coat of arms (COA) generation.

  - `src/`: Contains the project's source code files.

    - `__pycache__/`: Automatically generated directory storing compiled Python bytecode files (`.pyc`).

    - `assets/`: Stores various project-related assets.

      - `charges/`: Contains images or representations of heraldic charges (symbols used in coats of arms).

      - `compartment (supporter's compartment)/`: Holds assets related to the compartment where supporters stand in a coat of arms.

      - `crest (Crest of Arms)/`: Stores assets related to the crest, a decorative element above the shield in a coat of arms.

      - `mantling/`: Contains assets related to mantling, a decorative cloak or drapery flowing from the helmet in a coat of arms.

      - `motto/`: Holds assets related to mottos, phrases or slogans often displayed on a ribbon below the shield in a coat of arms.

      - `ordinaries/`: Contains images or assets related to ordinaries, simple geometric shapes or lines used for division or decoration in a coat of arms.

      - `pavilion/`: Stores assets related to pavilions, embellished tents or canopies, rarely found in English or Scots achievements.

      - `ribbon, collar, or badge/`: Contains assets related to ribbons, collars, or badges that can encircle or depend from the shield in a coat of arms.

      - `shield (division)/`: Holds images or assets related to the shield or divisions of the shield in a coat of arms.

      - `tinctures/`: Contains assets related to tinctures, representing the colors and metals used in coats of arms.

      - `torse (coronet)/`: Stores images or assets related to the torse, a twisted wreath or coronet from which the crest arises in a coat of arms.

  - `data/`: Directory for storing data files or resources used by the project.

  - `saved_coats_of_arms/`: Directory for saving or storing generated coats of arms created by the application.

  - `tests/`: Directory for storing test cases or files related to testing the project's code.

- Various `.py` files: Python script files making up the project's source code, each serving a specific purpose.

- `cleanup.py`: Script for cleaning up or managing files or resources in the project.

- `cleanup_log.txt`: A log file recording activities or results of the cleanup process.

- `cleanup_windows.bat`: Windows batch script for running the cleanup process.

- `DIRECTORY_STRUCTURE.md`: Markdown file containing the project's directory structure, generated by script `generate_structure.py`.

- `generate_structure.py`: Script used for generating or updating the project's directory structure.

- `generate_structure_windows.bat`: Windows batch script for running the directory structure generation script.

- `LICENSE`: File containing information about the project's licensing terms and permissions.

- `README.md`: Markdown file providing an overview, instructions, or documentation for the project.

- `requirements.txt`: File listing required Python packages and their versions for the project.

- `run_windows.bat`: Windows batch script for running or executing the project.

- `setup.py`: Script for setting up or configuring the project.

- `setup_windows.bat`: Windows batch script for running the setup process.
```

## Directory Structure
```
coa-generator/
│
├── src/
│   ├── __pycache__/
│   │   ├── coat_of_arms.cpython-311.pyc
│   │   ├── heraldic_elements.cpython-311.pyc
│   │   └── user_interface.cpython-311.pyc
│   ├── assets/
│   │   ├── charges/
│   │   ├── compartment (supporter's compartment)/
│   │   ├── crest (Crest of Arms)/
│   │   ├── mantling/
│   │   ├── motto/
│   │   ├── ordinaries/
│   │   ├── pavilion/
│   │   ├── ribbon, collar, or badge/
│   │   ├── shield (division)/
│   │   ├── tinctures/
│   │   └── torse (coronet)/
│   ├── data/
│   ├── saved_coats_of_arms/
│   ├── tests/
│   ├── coat_of_arms.py
│   ├── coat_of_arms_generator.py
│   ├── heraldic_elements.py
│   ├── main.py
│   ├── renderer.py
│   ├── saver.py
│   └── user_interface.py
├── cleanup.py
├── cleanup_log.txt
├── cleanup_windows.bat
├── DIRECTORY_STRUCTURE.md
├── generate_structure.py
├── generate_structure_windows.bat
├── LICENSE
├── New Text Document.txt
├── README.md
├── requirements.txt
├── run_windows.bat
├── setup.py
└── setup_windows.bat
```
## Development
Developers interested in contributing should refer to the [Development Guide](DEVELOPMENT.md).
#TODO

## Contributing
If you want to contribute to the Coats of Arms Generator, please review the [`CONTRIBUTING.md`](CONTRIBUTING.md).
#TODO

## Versioning
For versioning, I use [SemVer](https://semver.org/).

## Authors and Acknowledgment
- **Jack Alexander Cooper** - *Initial work* - [GitHub Profile](https://github.com/Jack-A-Cooper)

***Special thanks to OpenAI's ChatGPT for providing AI assistance and guidance. Especially for research and automating the workflow when necessary.***

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) for details.

## Screenshots / Demo
![Coat of Arms Example](path-to-screenshot.png)
#TODO

Add more screenshots or a video demo if possible.

## FAQs / Common Issues
Here you can list common issues and their solutions.
#TODO

## Changelog
For detailed release notes, see the [CHANGELOG](CHANGELOG).
#TODO

## Support or Contact
For support or inquiries, reach out to [jack_cooper01@yahoo.com](mailto:jack_cooper01@yahoo.com).

---
© 2023 Jack Alexander Cooper. All Rights Reserved.
