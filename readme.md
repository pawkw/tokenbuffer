# tokenbuffer

TokenBuffer provides a TokenBuffer class and tokenizer provides a Token data class.

# Use

After creating a new TokenBuffer, You will have to initialize the regex patterns with a dictionary of token names and patterns.

```python
from TokenBuffer import TokenBuffer, Token

patterns = {
    'INTEGER': r'\d+',
    'MATH_OPERATOR': r'[\+\-\*\/]',
    'BINARY_OPERATOR': r'[\&\|\^]',
    'ASSIGNMENT': r'=',
    'IDENTIFIER': r'\w+'
}

buffer = TokenBuffer()
buffer.init_patterns(patterns)
```

Now you will have to provide content to be tokenized. This can be done by adding lines or loading files or both. load_files accepts a list of strings, which are the files to load. add_lines takes a "file name", for tracking purposes, and a list of strings.

```python
buffer.load_file(sys.argv[1:])
buffer.add_lines('cleanup', ['push(result)', 'exit()'])
```

Once the source text is ready, you will have to tokenize it.

```python
buffer.tokenize()
```

The tokenizer provides white space, end of line, and end of file tokens. You can configure how they are handled when reading the buffer. The defaults are:
- 'skip_white_space': False
- 'skip_EOF': True
- 'skip_EOL': True

```python
buffer.config(
        skip_white_space = True,
        skip_EOF = True,
        skip_EOL = True
    )
```

You can read through the buffer with these methods:
- peek(): Returns the current token, skipping the tokens specified in the configuration.
- consume(): Advances to the next token.
- consume_line(): Advances to the start of the next source line.
- expect_value(expected_value, lower = False): Returns the result of an equality test. Set lower to True if you want the test to be case insenstive.
- expect_type(expected_type): expected_type is the token name you provided with the regex patterns.
- backtrack(): Backtracks to the previous unskipped token.
- backtrack_line(): Backtracks to the end of the previous line, skipping unwanted tokens.
- at_start(): Returns True if the buffer is at the first token of the first file.
- out_of_tokens(): Returns True if there are no more tokens available.
- get_position(): Returns a tuple of current file name, current file line, **token column**. Token column is not the column of the source file text! See Token below. This column is the token index of the current line. IE: The third token on the line is 2, while the source text column could be anything. 
- reset(): Reset the position of the buffer to the first token of the first line.

# Token

Token is a dataclass with three data members:
- type: The regex group name you provided.
- value: The value of the regex match. This is always a string. You will have to convert to the appropriate data type while processing.
- column: This the the position on the source text line where the value was found.

```python
while not buffer.out_of_tokens():
    peek: Token = buffer.peek()
    file, line, column = buffer.get_position()
    print(f"file: {file} line {line} column {peek.column} type: {peek.type} value: {peek.value}")
    buffer.consume()

print('\nBacktracking')
while not buffer.at_start():
    buffer.backtrack()
    peek: Token = buffer.peek()
    file, line, column = buffer.get_position()
    print(f"file: {file} line {line} column {peek.column} type: {peek.type} value: {peek.value}")
```
