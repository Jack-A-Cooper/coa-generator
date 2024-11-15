# Coats of Arms Generator
> A tool to create personalized coats of arms with historical heraldic rules.

<p align="center">
  <img src="resources/examples/coa gen example.png" alt="COA Gen Example">
</p>

> Current version: 0.1.0

## Table of Contents
- [Installation](#installation)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Examples](#examples)
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

## Examples

<p align="center">
  <img src="resources/examples/coa gen example 2.png" alt="COA Gen Example 2">
  <img src="resources/examples/coa gen example 3.png" alt="COA Gen Example 3">
  <img src="resources/examples/coa gen example 4.png" alt="COA Gen Example 4">
  <img src="resources/examples/coa gen example 5.png" alt="COA Gen Example 5">
  <img src="resources/examples/coa gen example 6.png" alt="COA Gen Example 6">
  <img src="resources/examples/coa gen example 7.png" alt="COA Gen Example 7">
  <img src="resources/examples/coa gen example 8.png" alt="COA Gen Example 8">
  <img src="resources/examples/coa gen example 9.png" alt="COA Gen Example 9">
  <img src="resources/examples/coa gen example 10.png" alt="COA Gen Example 10">
</p>

## Source Documentation
```
- `coa-generator/`: The root directory of the project related to coat of arms (COA) generation.

- `src/`: Contains the project's source code files.

- `assets/`: Stores various project-related assets.

  - `charges/`: Contains images or representations of heraldic charges (symbols used in coats of arms).

- `saved/`: Directory for saving or storing generated coats of arms created by the application.

- `resources/`: Contains the project's resource files.

  - `resources/examples`: Contains the project's example files.

- Various `.py` files: Python script files making up the project's source code, each serving a specific purpose.

- `cleanup.py`: Script for cleaning up or managing files or resources in the project.

- `cleanup_log.txt`: A log file recording activities or results of the cleanup process.

- `cleanup_windows.bat`: Windows batch script for running the cleanup process.

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
├── assets/
│   └── charges/
├── resources/
│   └── examples/
├── saved/
├── src/
│   ├── tests/
│   ├── coat_of_arms.py
│   ├── heraldic_elements.py
│   ├── main.py
│   ├── renderer.py
│   ├── saver.py
│   └── user_interface.py
├── cleanup.py
├── cleanup_log.txt
├── cleanup_windows.bat
├── LICENSE
├── README.md
├── requirements.txt
├── run_windows.bat
├── setup.py
└── setup_windows.bat
```
## Development
Developers interested in contributing should refer to the [Development Guide](DEVELOPMENT.md).

## Contributing
If you want to contribute to the Coats of Arms Generator, please review the [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Versioning
For versioning, I use [SemVer](https://semver.org/).

## Authors and Acknowledgment
- **Jack Alexander Cooper** - *Initial work* - [GitHub Profile](https://github.com/Jack-A-Cooper)

***Special thanks to OpenAI's ChatGPT for providing AI assistance and guidance (in particular, the much improved model 'ChatGPT-4o'). Especially for research and automating the workflow when necessary.***

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) for details.

## Changelog
For detailed release notes, see the [CHANGELOG](CHANGELOG).
* 0.0.1: 
  - Basic project structure established.
  - Rudimentary coat of arms generation (very early stage - not able to really do much at all nor follow any rules).
  - Utilities for installing requirements, ensuring correct directory structure, and automated cleaning up of the project.

* 0.0.2:
  - Improvement to coat of arms generation.
  - Bug fixes
    - Rendering not working or appearing at all.
    - Incorrect access of healdic elements within the following files: 'coat_of_arms.py' and 'hearaldic_elements.py'.

* 0.1.0:
    - Improvements:
        - Greatly expanded coat of arms generation (new divisions, ordinaries, and charges).
        - Added charges (utilizes .svg as the standard format).
        - Vastly improved project structure and cleaned up code base.
        - Version 0.1.0 is capable of being ran from either command line and/or using the run_windows.bat (a new cosole window appears with generation information and a window showing the generated coat of arms is presented to the user).
    - Bugs:
        - Still testing current version.
        - Several rules are not fully followed or behaving as desired.
        - Frequent issues with generation behavior (such as generating 'boring' and/or 'blank' coats of arms).
    - Changes:
        - Project Structure.
        - Coat of arms generation and hearaldic element rules.

## Support or Contact
For support or inquiries, reach out to [jack_cooper01@yahoo.com](mailto:jack_cooper01@yahoo.com).

---
© 2023 Jack Alexander Cooper. All Rights Reserved.
