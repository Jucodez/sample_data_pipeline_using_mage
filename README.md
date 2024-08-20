# Pipelines Included In Mage Project

The dataset used in this project is the New York City Taxi and Limousine Commission (TLC) Trip Record Data for yellow taxi cabs in January 2021.

## ETL Pipeline from API to Postgres Database

This data pipeline takes the data from an API, cleans it and loads it into a Postgres database.

![Screenshot (878)](https://github.com/user-attachments/assets/5758a0be-1f7c-4941-b056-8fce008c1930)
![Screenshot (879)](https://github.com/user-attachments/assets/0f439a5f-04e0-42d8-822d-6acf2efa6317)
![Screenshot (880)](https://github.com/user-attachments/assets/6e73566a-45de-46b4-8fc1-c8bab1439ee2)
![Screenshot (881)](https://github.com/user-attachments/assets/326ef8ac-34e1-4343-a0b5-a85adb2d137b)
![Screenshot (882)](https://github.com/user-attachments/assets/5b55f1b6-c826-456f-bcb1-cf8511fcc973)
![Screenshot (883)](https://github.com/user-attachments/assets/c7b2a021-7bec-40eb-979e-f9123dafad6b)
![Screenshot (884)](https://github.com/user-attachments/assets/fcb19461-c750-43d0-8aa3-28b145cd9770)

## ETL Pipeline from API to a Google Cloud Storage Bucket

This data pipeline takes the data from an API, cleans it, and loads it into a Google Cloud Storage Bucket. 

The pipeline creates two outputs. The first is a single file. However, due to file size a second approach is presented for easier manipulation

The second approach stores the file in partitions based on date for easier manipulation and processing.

![Screenshot (892)](https://github.com/user-attachments/assets/2925cfca-920b-4790-98c0-622368e2ea9b)
![Screenshot (885)](https://github.com/user-attachments/assets/21e8cde2-25a0-40ae-b95b-f9d9dc8ec5ec)
![Screenshot (886)](https://github.com/user-attachments/assets/c50a1af8-9b06-465b-88a8-336baa4ba653)
![Screenshot (887)](https://github.com/user-attachments/assets/f1543d0b-0a2c-4327-9574-7ee93c267f16)
![Screenshot (888)](https://github.com/user-attachments/assets/19ff17d5-3846-4b21-94cb-4fa36a2552f2)
![Screenshot (889)](https://github.com/user-attachments/assets/823ca556-6c9a-4e77-9853-44d59ce32b8a)
![Screenshot (890)](https://github.com/user-attachments/assets/2bf9fe97-1b1e-4fd3-bcf3-8ada0f91e3cf)
![Screenshot (891)](https://github.com/user-attachments/assets/3903ce3e-915a-40ba-8828-931fc0ca97f1)

    
