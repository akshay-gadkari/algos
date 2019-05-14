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
    for i in range(len(dependencies)):
        # list all the dependent projects
        dependencies1.append(dependencies[i][1])
        # print(dependencies1)
        # if something is depended on, but also depends on something else
        if dependencies[i][0] in dependencies1:
            # check what it depends on, and what that depends on, and ...
            check(dependencies[i][0])
    return

build(projects, dependencies)

counter = 0
def check(dependency, counter):
    for i in range(len(dependencies)):
        if dependency == dependencies[i][1]:
            dependency == dependencies[i][0]
        else:
            first_dependencies.append(dependency)
            print(first_dependencies)
    return
