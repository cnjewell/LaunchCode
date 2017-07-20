# U01C08

def print_triangular_numbers(n):
    sum = 0
    for i in range(n):
        sum += i+1
        print(sum)
        
def workout_coach(lift_name, wt):
    print("Time to", lift_name, wt, "pounds! Plus Ultra!")

def course_grader(test_scores):
    underfifty = 0
    underseventy = 0
    
    for score in test_scores:
        if score < 50:
            underfifty += 1
    
    if sum(test_scores)/len(test_scores) < 70:
        underseventy += 1
        
    if underfifty+underseventy:
        return("Fail")
    else:
        return("Pass")

def main():
    
    # Exercise 1
    # print_triangular_numbers(20)

    # Exercise 5
    # lifts = ["squat", "bench", "deadlift"]
    
    # for lift in lifts:
    #     wt = 10
    #     while wt < 200:
    #         workout_coach(lift, wt)
    #         wt += 10
    #         response = input("Keep doing the " + lift + "? Enter yes for the next set. ").lower()
    #         if response != "yes":
    #             break

    # Weekly Graded Assignment
    print(course_grader([100,75,45]))     # "fail"
    print(course_grader([100,70,85]))     # "pass"
    print(course_grader([80,60,60]))      # "fail"
    print(course_grader([80,80,90,30,80]))  # "fail"
    print(course_grader([70,70,70,70,70]))  # "pass" 

if __name__ == "__main__":
    main()