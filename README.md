# Inventory 2.0
Barcode Scanner, Home Inventory, Shopping List, Local Database... all on a Raspberry Pi.

# Setup

Requires the [rpi_ws281x](https://github.com/jgarff/rpi_ws281x) library to be installed. Clone the library to any user directory (does not have to be in project). Do the following from rpi_ws281x root:

`sudo scons`
`cd python`
`sudo apt-get install python-dev swig`
`python ./setup.py build`
`sudo python setup.py install`

This should create the necessary modules Inventory2.0 will reference.
