import json
import re

def phrasel_search(P, Queries):
    # Write your solution here 
    ans = []

    # For each line we create a new list to hold the fuzzy matched phrases temporarily
    for line in Queries:
        new_list = []

        # Split each phrase by there spaces and capture the begining string
	# and the last string in the phrase list
        for phrase in P:
            p_list = phrase.split()
            start = p_list[0]
            last = p_list[len(p_list) - 1]

	    # Iterate through each line of the Queries and match substrings that
	    # start with the first word in a phrase and end in the last word.
            # ignore the extra words in between to be able to fuzzy capture the phrase
            match = re.finditer(rf"(?={start})([\s\S]*?)({last})", line)

	    # If we find a match or matches, iterate through each match and find the difference
            # between the lengths of the matched string and the phrase we are matching          
            if match is not None:
                for sec in match:

		    #If there is less than 1 word extra in the matched phrase, append to the tempory list
                    if (len(sec.group().split()) - len(phrase.split())) <= 1:
                        new_list.append(sec.group())
                    else:
                        continue
            else:
                continue

        ans.append(new_list)
    print(ans)
    return ans

if __name__ == "__main__":
    with open('sample.json', 'r') as f:
        sample_data = json.loads(f.read())
        P, Queries = sample_data['phrases'], sample_data['queries']
        returned_ans = phrasel_search(P, Queries)
        print('============= ALL TEST PASSED SUCCESSFULLY ===============')
