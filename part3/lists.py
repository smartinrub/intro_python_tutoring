# create list
programming_languages = ['Python', 'Java', 'C#', 'Go']
print(programming_languages)

# access element from list
programming_languages = ['Python', 'Java', 'C#', 'Go']
print(programming_languages[1])

# modify list
sports = ['football', 'basketball', 'tennis', 'rugby']
sports[0] = 'badminton'
print(sports)

# add value
sports = ['football', 'basketball', 'tennis', 'rugby']
sports.append('badminton')
print(sports)

sports = ['football', 'basketball', 'tennis', 'rugby']
sports.insert(0, 'badminton')
print(sports)

# removing elements
sports = ['football', 'basketball', 'tennis', 'rugby']
del sports[0]
print(sports)

sports = ['football', 'basketball', 'tennis', 'rugby']
sports.pop()
print(sports)

sports = ['football', 'basketball', 'tennis', 'rugby']
sports.remove('basketball')
print(sports)

# sorting
sports = ['football', 'basketball', 'tennis', 'rugby']
sports.sort()
print(sports)
sports.sort(reverse=True)
print(sports)

sports = ['football', 'basketball', 'tennis', 'rugby']
sports.reverse()
print(sports)

sports = ['football', 'basketball', 'tennis', 'rugby']
print(len(sports))
