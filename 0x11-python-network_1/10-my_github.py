#!/usr/bin/python3
"""
    a Python script that takes your GitHub credentials
    username and password) and uses the GitHub API to display your id
"""


if __name__ == "__main__":
    import sys
    import requests

    url = "https://api.github.com/users/" + sys.argv[1]
    headers = {
                'Accept': 'application/vnd.github+json',
                'Authorization': 'Bearer' + " " + sys.argv[2],
                'X-GitHub-Api-Version': '2022-11-28'
            }
    response = requests.get(url, headers=headers)
    print(response.json().get('id'))
