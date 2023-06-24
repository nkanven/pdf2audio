![Alt text](relative%20path/to/img.jpg?raw=true "Title")
# pdf2audio

> Convert your PDF file into an audio (mp3) file with pdf language detection


## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
- Pdf2audio is an easy command line script you can used to convert any pdf file to a mp3 file
<!-- You don't have to answer all the questions - just the ones relevant to your project. -->


## Technologies Used
- Pdf2audio need only Python 3.11 to function

## Features
With Pdf2audio, you can convert the whole pdf file to a mp3. The script actually support french voice for french documents
and english voice for all the other languages.


## Setup
Make sure you have pip install.

For Linux users
`sudo apt install python3-pip`

clone this repo in your computer, preferrably on your project root dir.
Package can be executed globally if add to System environment path.
Launch the module with



## Usage
How does one go about using it?

- You can convert any pdf file every easily from the project base directory by typing :

`python main.py PATH_T0_PDF_FILE`

- This will generate the PATH_T0_PDF_FILE.mp3 file.



## Project Status
Project is: _in progress_ I am continously adding features and updating the package

## Room for Improvement

Room for improvement:
- Upload the package to Pypi
- Optimize voices according to pdf language
- Add more parameters like voice speed for easy user manipulation
- Make it run in pycharm environment without error
- Add Flask for website deployment to be used freely online


## Contact
Created by [@nkanven](https://www.linkedin.com/in/nkondog) - feel free to contact me!


## License
This project is open source and available under the MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
