f = open("/Users/droberts/2016Feb13/output.txt","a")
f.write("%s,%s" % (request.query['p1'], request.query['p2'])
f.close()

