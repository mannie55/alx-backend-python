# python-generators-0x00

**Create and seed MySQL database with data using Python generators**

---

## Overview

This project demonstrates how to use Python generators for efficient data streaming and batch processing with a MySQL database. It covers connecting to a MySQL database, creating and seeding tables, and processing user data in both streaming and batch modes.

---

## Contents

- **0-stream_users.py**  
  Stream user records one at a time from the database using a generator.

- **1-batch_processing.py**  
  Process user records in batches using a generator for memory efficiency.

- **2-lazy_paginate.py**  
  (If present) Demonstrates lazy pagination over database records.

- **seed.py**  
  Contains functions to create the database, tables, and seed them with data from `user_data.csv`.

- **user_data.csv**  
  Sample CSV file containing user data to be loaded into the database.

- **0-main.py, 1-main.py, 2-main.py, 3-main.py, 4-stream_ages.py**  
  Example scripts to run and test the streaming and batch processing functions.

- **vitualenv/**  
  Python virtual environment for package management and isolation.

---

## Key Concepts

- **Python Generators:**  
  Efficiently stream or batch-process large datasets without loading everything into memory.

- **MySQL Database Operations:**  
  Connect, create, and seed a MySQL database using Python (`pymysql`).

- **Batch Processing:**  
  Fetch and process records in configurable batch sizes for scalability.

---

## How to Use

1. **Set up your MySQL server** and ensure you have the correct credentials in the scripts.
2. **Install dependencies** (inside the `vitualenv`):
   ```bash
   source vitualenv/bin/activate
   pip install pymysql