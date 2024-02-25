import asyncio
import requests

async def getLink(username):
  # get data of page
  response = requests.get(f"https://e621.net/users?commit=Search&search%5Bname_matches%5D={username}", headers={'User-Agent': 'UsernameToLink/1.0 by Spentine'})

  # get response
  rt = response.text

  # find user id
  beginningID = rt.find('<a class="user-member with-style" rel="nofollow"') + 62

  # if id wasn't found -1 (not found) + 62 = 61
  if beginningID == 61:
    return None

  # find end of user id
  endID = rt.find('"', beginningID)

  # return link
  return f"https://e621.net/users/{rt[beginningID:endID]}"

async def main():
  print(await getLink(input("Username: ")))

asyncio.run(main())
