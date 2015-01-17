# mysteryhunt

For solving the puzzle called "Pipe".

To gather a giant results.json blob:

```
python pipe.py
```

Feel free to ctrl+c it whenever you want and resume later. It is smart about
detecting an existing results.json file and resuming from where it left off.

To split the json blob up by the type of error it caused, type:

```
python sieve.py
```

Results are placed in files like stage5.json. Successes are stored in
successes.json
