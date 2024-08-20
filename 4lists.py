Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> players = [45,18,58,66,87]
>>> players[2]
58
>>> players[1]
18
>>> players
[45, 18, 58, 66, 87]
>>> players + [90,91,98]
[45, 18, 58, 66, 87, 90, 91, 98]
>>> players
[45, 18, 58, 66, 87]
>>> players.append(46)
>>> players
[45, 18, 58, 66, 87, 46]
>>> players[:2]
[45, 18]
>>> players[:2] = [0,0]
>>> players
[0, 0, 58, 66, 87, 46]
>>> players[:2] =[]
>>> players
[58, 66, 87, 46]
>>> players[:] = []
>>> players
[]
