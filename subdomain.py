#count the sub-domains i.e parent and child



class Solution:
    def subdomainVisits(self, cpdomains):
	
        lookup = {}
        for s in cpdomains:      				#traversing through list
            num, domain = s.split(' ')     		#spliting where space is found 
            sub = domain.split('.')				#"---------------"Dot is found
            for i in range(len(sub)):
                subdomain = '.'.join(sub[i:])
                lookup[subdomain] = lookup.get(subdomain, 0) + int(num)
        return [str(n)+" "+d for d, n in lookup.items()]
