# POS API


## Description

Design an API for a point of sale (POS) system

Project requirements:
- [x] Retrieve a menu of all the items in the POS. An item can have description, a price, a quantity and an ID
- [x] Add a new item to the menu
- [x] Update an item by ID
- [x] Delete an item by ID
- [x] Create a new order. An order should contain:
  - a list of item IDs, with a quantity for each item
  - a payment amount
  - an order note
- [x] Creating a successful order should return the order ID

## How to use it  🚀

Open a terminal and follow the steps bellow

- Clone the repo 
    ```
    https://github.com/zamu5/POS-API.git
    ```
  
- Move inside the project
    ```
    cd POS-API
    ```

- Install requirements
    ```
    make config
    ```
- Run server
    ```
    make run
    ```

## How to use it  🔧

- Open the Postman app
- Import the postman collection in the Postman app

Create an item:

To create an Item use the 'Create Item' endpoint inside the API/Item in postman collection


## Deployment  📦

[Python 3](https://www.python.org/) - backend

## Author ✒️

* **Sergio Zamudio** - [zamu5](https://github.com/zamu5)
