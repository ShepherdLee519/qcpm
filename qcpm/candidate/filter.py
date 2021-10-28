from qcpm.candidate.plan import Plan, Plans


def filter(candidates):
    count = 0 # plan's total number
    size = len(candidates)
    book = [ 0 for k in range(size) ]
    plans = []

    def recurFilter(i, last, delta_cost):
        """
            i           : current index of Candidates[]
            last        : the last selected candidate's ending position
            delta_cost  : total cost saved by this plan
        """
        if i >= size:
            # recursion ends => new plan
            nonlocal count
            count += 1

            plans.append(
                Plan([candidates[k] for k in range(size) if book[k] == 1 ], 
                    delta_cost)
            )
            
            return
        
        item = candidates[i]
        # Case 1. 
        # --------------
        #      last
        # ...cc[c]
        #      current
        #      [c]cc
        # => abandon current item
        if item.pos <= last:
            recurFilter(i + 1, last, delta_cost)
            return

        next_item = candidates[i + 1] if i < size - 1 else None
        # Case 2. 
        # if => two candidates(this & next) have conflict
        # --------------
        #     last
        # ...ccc
        #       current
        # ...ccc [c]cc..
        #        next
        # ...ccc c[c]c    
        if item & next_item:
            # Case 2.1. select this one
            book[i] = 1
            recurFilter(i + 2, item.end, delta_cost + item.pattern.delta())
            book[i] = 0

            # Case 2.2. abandon this one
            # Case 2.2 
            # if => this item and next item has the same pos
            # --------------
            #       current
            #    ...([c]c)c.. target: cc
            #       next
            #    ...([c]cc).. target: ccc 
            # => if abandon this one => must choose next item
            if next_item != None and item.pos == next_item.pos:
                book[i + 1] = 1
                recurFilter(i + 2, next_item.end, delta_cost + next_item.pattern.delta())
                book[i + 1] = 0
            else:
                recurFilter(i + 1, last, delta_cost)
        # Case 3. 
        # else => two candidates(this & next) have no conflict
        # --------------
        #     last
        # ...ccc
        #       current
        # ...ccc ([c]c)c..
        #        next
        # ...ccc cc[c]..
        # => choose this one 
        else:
            # no conflict => choose this one
            book[i] = 1
            recurFilter(i + 1, item.end, delta_cost + item.pattern.delta())
            book[i] = 0

    recurFilter(0, -1, 0)

    return Plans(plans)