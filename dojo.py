from docopt import docopt
usage='''
DOJO 

Usage:
      dojo.py create_room <type> 
      dojo.py 
      dojo .py add_person <firstName> <LastName> <role> [<want_livingRoom>]


'''
arg=docopt(usage)
print(arg)

if arg['create_room']:
      
      print('Successfully created an orange  office')

