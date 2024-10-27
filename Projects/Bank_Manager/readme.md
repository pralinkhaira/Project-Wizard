# Bank Management System

## Overview

The **Bank Management System** is a console-based application written in C that allows users to manage their bank accounts. The system provides functionalities such as account creation, deposits, withdrawals, and balance inquiries. It is designed to be simple and user-friendly, making it easy for users to perform banking operations.

## Features

- **Create Account**: Users can create a new bank account by providing their name and initial balance.
- **Deposit Money**: Users can deposit money into their accounts.
- **Withdraw Money**: Users can withdraw money from their accounts, subject to sufficient balance.
- **Balance Inquiry**: Users can check their current balance.
- **Data Management**: The application saves account details and transactions to text files for persistent storage.

## File Structure

The application creates and uses the following files:

- `acc_no_serial.txt`: Keeps track of the last account number used.
- `database_accounts.txt`: Records the details of all created accounts.
- `balance/`: Directory where individual balance files are stored.
- `customer/`: Directory where customer details are stored.

## Prerequisites

To compile and run this project, you need:

- A C compiler (e.g., GCC)
- Basic knowledge of C programming

## Installation

1. Clone the repository or download the source code.
2. Open a terminal and navigate to the project directory.
3. Compile the program using a C compiler. For example:

   ```bash
   gcc bank_management_system.c -o bank_management_system

### Run
 ```bash
    ./bank_management_system

```

### Made by <a href="https://github.com/darkforce112">Amit<a>

