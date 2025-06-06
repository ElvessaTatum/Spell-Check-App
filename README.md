# Spell-Check-App
A spell checking app made in python. Created by Elvessa Tatum and Dang Pham

# Overview
This spell check application reads text files and processes them to identify misspelled words. It uses an external web service to verify spelling and marks incorrect words with square brackets [word] and words that cause exceptions during checking with underscores _word_.

# Features

File-based Processing: Read and process text files of any size
Online Spell Checking: Uses external API for accurate spell verification
Visual Error Marking:

[word] for misspelled words
_word_ for words that cause API exceptions


Command-line Interface: Easy-to-use CLI with file argument support
Robust Error Handling: Graceful handling of network errors and file issues
Multi-line Support: Preserves original text formatting and line breaks
Extensible Design: Modular architecture for easy service replacement

# Prerequisites

Python 3.6 or higher
requests library for HTTP requests

# Setup

Clone or download the project files
Install required dependencies:
bashpip install requests

Ensure you have the following files:
spell_check.py          # Core spell checking logic
process_text.py         # Text processing engine
process_text_UI.py      # Command-line interface
test_process_text.py    # Unit tests for text processing
test_spell_check.py     # Unit tests for spell checking

# Usage
Command Line Interface
  Basic Usage
    bashpython process_text_UI.py
    The application will prompt you for a filename.
With File Argument
    bashpython process_text_UI.py --file_name sample.txt

# Design Overview
Backend – process_text.py & spell_check.py Handle the core text processing and spell checking:

process_text() – main processing function that applies spell checking to entire text
process_word() – handles individual word processing with error handling
process_line() – processes each line while preserving whitespace
is_spelling_correct() – makes API calls to validate word spelling
get_response() & parse_response() – handle HTTP requests and response parsing

Frontend – process_text_UI.py Handles the user interface:

Command-line interface with file input prompts
Progress indicators during file reading and processing
Display of both raw and processed text results
Error handling for file not found and other exceptions
Command-line argument support for batch processing

# Text Processing Logic:

Correctly spelled words remain unchanged
Misspelled words are wrapped in square brackets [word]
Words that cause API errors are wrapped in underscores _word_
Whitespace and formatting are preserved throughout processing
