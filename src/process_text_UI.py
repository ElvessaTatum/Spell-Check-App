import time
import sys
import argparse
from process_text import process_text
from spell_check import is_spelling_correct

def main(file_name = None):
    print("***************************")
    print("*     Spell Check App     *")
    print("***************************")
    while True:    
        if file_name is None:
            file_name = input("Enter the file name (include extension): ")
        try:
            with open(file_name, 'r') as file:
                text = file.read()

            sys.stdout.write("Reading file...\r")
            sys.stdout.flush()
            time.sleep(2)

            sys.stdout.write("Processing text...\r")
            sys.stdout.flush()

            processed_text = process_text(text, is_spelling_correct)

            print("--------------------Process Done-------------------")

            time.sleep(1.5)

            print("\nRaw Text:")
            print(text)

            time.sleep(1.5)

            print("\nProcessed Text:")
            print(processed_text)
            break

        except FileNotFoundError:
            print(f"File '{file_name}' not found. Please try again.")
            file_name = None

        except Exception as message:
            print(f"An error occurred: {message}")
            break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Spell Check Application")
    parser.add_argument('--file_name', type=str, help='The name of the file to process.')
    
    args = parser.parse_args()
    main(args.file_name)
