# How to Use

Use `await getLink(USERNAME)` to return an e621 link from a username.

## Example

```py
async def main():
  while True: # forever
    print(await getLink(input("Username: "))) # get link from username

asyncio.run(main())
```
