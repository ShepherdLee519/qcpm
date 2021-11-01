from qcpm.candidate.plan import Plan, Plans


def filterCandidates(candidates):
    count = 0 # plan's total number
    size = len(candidates)
    plans = []

    def selectCandidate(i):
        target = candidates[i]
        temp = [target]
        s = set(target.pos)
        delta_cost = target.pattern.delta()

        for j in range(i + 1, size):
            if not (candidates[j] & s):
                temp.append(candidates[j])
                delta_cost += candidates[j].pattern.delta()
                s = s | set(candidates[j].pos)
        
        nonlocal count
        count += 1

        plans.append(
            Plan(temp, delta_cost)
        )


    for i in range(size):
        selectCandidate(i)

    return Plans(plans)