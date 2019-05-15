# Chapter 04 - Problem 07 - Build Order
# Problem Statement:

# You are given a list of projects and a list of dependencies (which is a list of pairs of projects,
# where the second project is dependent on the first project). All of a project's dependencies must
# be built before the project is. Find a build order that will allow the projects to be built.
# If there is no valid build order, return an error.

projects = ['p1', 'p2', 'p3', 'p4']
dependencies = [['p1', 'p2'], ['p3', 'p4'], ['p0', 'p1']]
dependencies1 = []
first_dependencies = []

counter = 0
def check(dep):
    for i in range(len(dependencies)):
        if dep == dependencies[i][1]:
            dep == dependencies[i][0]
            # print(dep)
        else:
            if dep in first_dependencies:
                break
            else:
                first_dependencies.append(dep)
    print('first', first_dependencies)
    return

def build(p, d):
    for i in range(len(dependencies)):
        # put all the dependent projects in a list
        dependencies1.append(dependencies[i][1])
        # if something is depended on, but also depends on something else
        dependencies[i][0]
        # print(dependencies[i][0])
    for i in range(len(dependencies)):
        if (dependencies[i][0] in dependencies1):
            # check what it depends on, and what that depends on, and ...
            # print('true')
            check(dependencies[i][0])
    # print('false')
    # print(dependencies1)
    return

build(projects, dependencies)
