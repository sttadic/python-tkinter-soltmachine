# Slot Machine
Video Game - Final Project for CS50p Harvard University Course, Introduction to Programming with Python

By Stjepan Tadic

#### [Short video demo](https://youtu.be/G786LXmy0m0)


## Introduction
The Slot Machine video game 'Dino Hunt' is a Python-based application that simulates the experience of playing a slot machine. It is a simple 3-reel 3-pay lines, dinosaur-themed slot machine which offers players the excitement of spinning the reels and trying their luck to win virtual money.

## Features
- Interactive graphical user interface (GUI) for playing the slot machine.
- Realistic slot machine mechanics, including spinning reels and randomized outcomes.
- Five types of symbols with different payout values.
- Betting system that allows players to wager a chosen amount.
- Win system that calculates the payout based on the symbols and total bet amount.
- Sound effects to enhance gaming experience.
- Options to cash out, start a new game and reset the player's balance.

## Dependencies
- Python (>=3.11)
- Tkinter library (usually included with Python installations)
- Pygame (==2.5.0)
- Pytest (>=7.4.0) - used for testing and development purposes only

## Quick start guide
Clone the repository:
```bash
git clone https://github.com/sttadic/python-tkinter-soltmachine
```
Install packages from a requirements file, preferably in your active virtual environment, by navigating to the project directory and typing the following command in your command prompt or terminal:
```bash 
pip install -r requirements.txt
``` 
Finally, run a command: 
```bash
python3 project.py
```
On start of a game user is prompted for a balance. Once entered, a pay table is displayed containing information about symbol multipliers. From that point on, the user can change pay lines and bet amounts, spin the reels, choose to cash out, start a new or quit the existing game.

<br>

## Description

The heart of the project lies within the "project.py" file, which serves as the main Python script responsible for implementing the entire slot machine game, encompassing its logic, design, and functionality. In addition, distinct directories house the collection of sound effects and images.
To ensure the functionality of this project, unit tests have been provided. The test file "test_project.py" contains test cases for "get_balance", "load_image" and "play_sound" functions.

The project is structured using object-oriented programming (OOP) principles, with classes representing key components of the game: SlotMachine, Slots and ControlFrame.

- ***SlotMachine*** class starts the game itself and establishes the visual design and layout of the elements in the game by positioning different components of the slot machine in their respective places. Furthermore, it initiates the start screen and shows a paytable, checks different parameters such as screen resolution and tailors the game for optimal user experience.

- ***Slots*** class is responsible for the creation of slots or frames that would house symbols, as their combination would represent the reels of the slot machine.

- ***ControlFrame*** class constructs control panel for the slot machine which holds various mechanisms to control the game flow, such as spin, cash-out, bet amount and pay lines settings. It also holds a majority of the game logic. Functions that initiate and animate spins, configure bet amounts and pay lines, check and update balance, and many others are seamlessly integrated into this class.

### Design Choices
One of the biggest design considerations emerged during the process of adapting the game to various display resolutions. The initial development of the game was in a native 1080p resolution. As the project neared completion, it became apparent that the application might not exhibit consistent behaviour or appearance across all screen resolutions. 

While testing the app on lower resolutions, portions of the main game window extended beyond the visible screen frame, rendering the game unplayable. The most problematic element was the frame (slot_frm) encompassing pay-table and reels (slots), which consist of canvas widgets holding the game's visual symbols (images). These symbols and their containing slots (canvases) have fixed dimensions, causing the frame (slot_frm) to resize automatically to fit all of the content (symbols inside of a slots) upon instance creation. While nicely aligned on 1080p, frame resizing led to the disproportionate scaling of game elements on other resolutions.

Exploring potential solutions, I considered methods such as scaling using root.tk.call() or the Ctypes Python library. However, those approaches proved impractical, particularly their inability to properly resize actual symbol images and their slots which had fixed dimensions. 
An alternative approach involved altering the code within the Slots class and some other program components, introducing complex logic to dynamically resize game elements based on the percentage change in resolution. Regrettably, that path proved to be extremely demanding and resource-intensive and, even if successful, would not change the size of the images (symbols) themselves, only the size of slots (canvases) encompassing them. An effective solution for image resizing would have been to incorporate the Python Imaging Library (PIL).

Ultimately, I opted against extensive resizing and instead choose to relocate the control frame on lower resolutions (the frame housing controls such as spin, bet settings and pay lines settings) from the bottom of the slot machine to the side. This adjustment, achieved using the grid layout manager, ensures that when the vertical pixel count of the screen falls below the height of the game window, all vital game components remain visible and appropriately aligned offering enjoyable gameplay even on lower screen resolutions.
