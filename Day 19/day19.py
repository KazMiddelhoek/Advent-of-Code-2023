with open("Day 19/input.txt", newline="") as file:
    lines = file.read().splitlines()

split_at = lines.index("")
workflows = lines[:split_at]
workflows = [workflow.rstrip("}").split("{") for workflow in workflows]
workflows = {k: v.split(",") for k,v in workflows}

parts = lines[split_at+1:]
sum_of_accepted_parts = 0
for part in parts:
    part = dict([category.split("=") for category in part.lstrip("{").rstrip("}").split(",")])
    x = int(part["x"])
    m = int(part["m"])
    a = int(part["a"])
    s = int(part["s"])
    next_workflow = "in"        
    while next_workflow not in ("A", "R"):
        for condition in workflows[next_workflow]:
            try:
                condition, next_workflow = condition.split(":")
            except:
                if condition == "A":
                    sum_of_accepted_parts += sum([x,m,a,s])
                next_workflow = condition
                break        
            if eval(condition):
                if next_workflow == "A":
                    sum_of_accepted_parts += sum([x,m,a,s])
                break    
print(sum_of_accepted_parts)

# part two
with open("Day 19/input.txt", newline="") as file:
    lines = file.read().splitlines()

split_at = lines.index("")
workflows = lines[:split_at]
workflows = [workflow.rstrip("}").split("{") for workflow in workflows]
workflows = {k: v.split(",") for k,v in workflows}

#strategy: find all lists of requirements
results = []
def try_new_workflow(requirements_so_far, next_workflow):
    for condition_and_next_workflow in workflows[next_workflow]:
        try:
            condition, next_workflow = condition_and_next_workflow.split(":")
        except:
            if condition_and_next_workflow == "A":
                results.append(requirements_so_far)
            elif condition_and_next_workflow == "R":
                return
            else:
                next_workflow = condition_and_next_workflow
                try_new_workflow(requirements_so_far, next_workflow)
            continue

        if next_workflow == "A":
            results.append(requirements_so_far + [condition])
        elif next_workflow == "R":
            pass
        else:
            try_new_workflow(requirements_so_far+[condition], next_workflow)
        
        if "<" in condition:
            requirements_so_far.append(condition.replace("<",">="))
        elif ">" in condition:
            requirements_so_far.append(condition.replace(">","<="))
    return

next_workflow = "in"
try_new_workflow([], next_workflow)

# now find distinct combinations for results by combining all conditions.
total_combinations = 0
for combination in results:
    multiplication = 1
    ranges ={
        "x": [1,4000],
        "m": [1,4000],
        "a": [1,4000],
        "s": [1,4000]
    }
    for req in combination:
        if "<=" in req:
            ranges[req[0]][1] = min(int(req.split("=")[1]), ranges[req[0]][1] )
        elif ">=" in req:
            ranges[req[0]][0] = max(int(req.split("=")[1]), ranges[req[0]][0])
        elif "<" in req:
            ranges[req[0]][1] = min(int(req.split("<")[1])-1,ranges[req[0]][1])
        elif ">" in req:
            ranges[req[0]][0] = max(int(req.split(">")[1])+1, ranges[req[0]][0])

    for min_val,max_val in ranges.values():
        multiplication *= (max_val - min_val +1)
    total_combinations += multiplication
print(total_combinations)
