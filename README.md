# Dad Joke Showdown

An entry for the make.fun bounty of the same name. The job: write one
original dad joke of at most 200 characters, and that joke is the whole
entry.

This little program (plain Python, standard library only) keeps the
joke, checks it against the bounty rules, and writes it to
`/output/entry.txt`, where the judge reads it.

## Run it

```sh
python3 main.py
```

It creates `/output` if it is not there yet, then writes this joke:

> I told the ocean I was shore of myself. It said, 'That's deep.'

That is 63 characters: one line, no line breaks, and a clean pun —
"shore" for "sure", with "deep" doing double duty as the ocean's
answer. A father of three would be proud, and slightly ashamed.

## What the program checks before writing

- The joke is not empty.
- It is no longer than 200 characters.
- It is not only whitespace.
- It contains no line breaks, so it really is one line.

If any of those fail, the program stops with a clear message and writes
nothing.

The bounty prize pool is $5 in total.
