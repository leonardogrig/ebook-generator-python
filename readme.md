# OpenAI Text Generation Project

This project uses the OpenAI API, specifically the text-davinci-003 engine, to generate headers and articles for an ebook. The ebook's theme, tone, and the number of headers are user inputs. 

The program also allows the user to exclude specific headers. The generated headers and articles are written to an output.txt file. 

All generated text is translated to Brazilian Portuguese.

## How it Works

1. The user inputs the ebook theme, tone, and the number of headers.
2. The program generates a suggested header based on the given theme and tone, excluding any headers the user chooses to exclude.
3. The user has the option to accept or reject the suggested header.
4. If the header is accepted, it is added to the list of headers for the ebook. If it is rejected, the program generates a new suggested header.
5. Once all headers are generated, the program creates articles for each header, again based on the given theme and tone.
6. The articles are then written to an output.txt file.

## Prerequisites

* An OpenAI API key
* Python 3.6 or higher
* dotenv Python library
