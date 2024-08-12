from awscode import listInstances,startInstances

dev_filter = {'Name': 'tag:env', 'Values': ['dev']}

startInstances(listInstances(dev_filter))

#also after line3, your can do:
# l=listInstances(dev_filter)
# startInstance(l)