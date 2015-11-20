import pdb
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('/Users/robroy/.my.cfn')

pdb.set_trace()

print config.items('client')
print config.get('client','database') 
print config

