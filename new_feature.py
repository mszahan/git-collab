authentication = ['admin', 'contributor', 'promoter']

for auth in authentication:
    if auth == 'admin':
        print('got it! the user is an admin')
    else:
        print(f'Sorry we did not find any admin the user is {auth}')
