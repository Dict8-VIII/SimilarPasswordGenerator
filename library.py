import mappings as map
run_upper_lower = True
run_common_subs = True
run_common_ends = True

def upper_lower(base):
    result = []
    if not run_upper_lower:
        return base
    position = 0
    for letter in base:
        if str(letter).isalpha():
            if str(letter).isupper():
                new_word = base[:position] + base[position].lower() + base[position+1:]
                result.append(new_word)
            else:
                new_word = base[:position] + base[position].upper() + base[position+1:]
                result.append(new_word)

            position += 1
    return list(dict.fromkeys(result))


def common_subs(base):
    result = []
    position = 0
    if not run_common_subs:
        return result
    result = [base]
    for letter in base:
        if letter in map.subs:
            for sub in map.subs[letter]:
                #print("Base is: " + str(base))
                new_word = base[:position] + str(sub) + base[position + 1:]
                #print("which has substitution: " + str(new_word))
                result.append(str(new_word))
        position += 1
    #print("Returning " + str(result) + " from common_subs")
    return list(dict.fromkeys(result))


def common_ends(base_list):
    result = base_list
    if not run_common_ends:
        return result
    for password in base_list:
        for ending in map.ends:
            result = result + [str(password + ending)]
            #print("added: " + password + " + " + ending)
    return result




def call_functions(base, depth):
    final = [base]
    final += upper_lower(base)
    for item in upper_lower(base):
        if len(item) > 1:
            final += common_subs(item)
    if depth > 1:
        for iteration in final:
            final = final + call_functions(iteration, depth-1)
    return list(dict.fromkeys(final))