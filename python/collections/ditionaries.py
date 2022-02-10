# dictionaries
# > 3.6: ordered, mutable

countries = {"UK":"London", "France":"Paris", "Belgium":"Brussels"}

#print(countries.pop('Belgium'))

#search_for = 'Germany'
#print(countries.get(search_for, f'{search_for} not found'))

#countries['Germany'] = 'Berlin'
countries.update({'Germany':'Berlin'})
print(list(countries.values()))