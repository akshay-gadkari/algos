# Chapter 04 - Problem 07 - Build Order
# Problem Statement:

# You are given a list of projects and a list of dependencies (which is a list of pairs of projects,
# where the second project is dependent on the first project). All of a project's dependencies must
# be built before the project is. Find a build order that will allow the projects to be built.
# If there is no valid build order, return an error.

projects = ['p1', 'p2', 'p3', 'p4']
dependencies = [['p1', 'p2'], ['p3', 'p4']]
dependencies1 = []

def build(p, d):
    # for i in range(len(dependencies)):
    #     if dependencies[i][0] not in dependencies[i][1]:
    #         print(dependencies[i][0])
    #         print(dependencies[i][1])
    #     else:        
    #         return('not good enough')
    for i in range(len(dependencies)):
        dependencies1.append(dependencies[i][1])
        print(dependencies1)
        if dependencies[i][0] in dependencies1:
            for i in dependencies1:
                
    return

build(projects, dependencies)
