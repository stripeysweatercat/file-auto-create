<h1 align="center"><strong>File Auto Creator!</strong></h1>
<h3 align="center">The slowest way to create a source code file!</h4>

<p align="center">
    <img src="https://img.shields.io/github/last-commit/stripeysweatercat/file-auto-create"></a>
    <img src="https://img.shields.io/github/license/stripeysweatercat/file-auto-create">
</p>
<p align="center">
    <a href="#introduction">Introduction</a> •
    <a href="#installation">Installation</a> •
    <a href="#usage">Usage</a> •
    <a href="#customisation-options">Customisation</a> •
    <a href="#features-to-implement">Upcoming Features</a>
</p>

## Introduction
A fun little project I made to test my python skills along with making my life easier! Quite scuffed so, if for some reason you've found this, do *not* expect it to work well xP Also keep in mind this is how *I* like to pre-format my files, it will most likely not fit your liking. Further customisation is in the works, however I want to get this running as an executable first :D


## Installation
1. Download the source code from the GitHub repository
2. Unzip folder
3. Boom


## Usage
### **Method 1**
1. Launch Command Promt or your terminal of choice
2. `cd` to the `file-auto-create-master` folder
3. run `py input_collector` to initiate customisation
4. Type in your response and hit enter after each input
5. Your file will be in the `results` folder

### **Method 2**
1. Enter the `file-auto-create-master` folder in File Explorer
2. type `cmd` into the address bar and hit enter
3. run `py input_collector` to initate customisation
4. Type in your response and hit enter after each input
5. Your file will also be in the `results` folder


## Customisation Options
### - File Extension
Input the file extension of the file you wish to create, including the period:
`.s, .js, .c` etc.

### - File Name
Pretty self explainitory, just input what you want the resulting file to be called :D
### - Author
The Author of the file (a.k.a you). Will be added as a comment to the top of the document
### - Format Date
If you want your date formatted as mm/dd/yy ~~like a weirdo~~ input `y`, if you'd prefer dd/mm/yyyy input `n`. Working on implementing yyyy/mm/dd as well don't fret
### - Comment Format
How are comments written in the language you intend to write? Input that here! Eventually this will be automated but for the moment it is manual
### - Include Purpose, Input, and / or Output field?
If y for any of these 3, a commented line will be created with either Purpose:, Input:, or Output: next to it. For clarity for readers (ignore that I didn't do it in this project, I mostly use it for Assembly Language)
### - Extra Content
Add any extra code you want appended to the end of the file :D

## Features to Implement
- [ ] Proper GUI - Have it be an actual app and not a cli command
- [ ] Further customisation - excluding certain options, thats it really xP
- [ ] Automatic Comment Format - Self explainitory, just automatically chooses the correct comment format from which extension you chose
- [ ] YYYY/MM/DD - Add that as an option to the date format
- [ ] Saved presets - Save presets for each language, will def come after the GUI is implemented


Do I know when any of these will happen? **NO!** Although I do hope they all happen eventually :D
