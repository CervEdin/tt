tt.py
=====

Simple CLI wrapper for the Open AI tokenizer
[tiktoken](https://github.com/openai/tiktoken).

Usage
-----

Either pipe input into `tt.py` or pass it a file as the first argument to
tokenize the text (by default using the `cl100k_base` encoding).

```sh
# tokenize the text 'Hello, World!'
echo "Hello, World!" | tt.py > hello-world-tokens.txt
# count the number of tokens
wc -w hello-world-tokens.txt
# decode the tokens
< hello-world-tokens.txt tt.py --decode > hello-world.txt
```

The main motivation for this script is to be able to quickly count tokens of a
given text.

For example, in a Vim buffer
```vim
:w !tt.py | wc -w
```
counts the number of tokens in the current buffer. Which handy if you want to
understand if the input is appropriate for a given model/context window.

For example, this `README.md` contains at the time of writing of 238 tokens. So
it fits into a small context window without any problem.

Requirements
------------

Requires [tiktoken](https://github.com/openai/tiktoken) to be installed.
For example using `pip install tiktoken`.
