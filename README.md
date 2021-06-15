# PyDictHasher

A simple Python script to generate fingerprint(hash) for a Python native dictionary  and decode it using a SECRET KEY.

<hr/>

## Generating Secret Key

You can use any random string of characters but the preferred way is run the following command below in the terminal to generate the secret key.

```
openssl rand -hex 32
```