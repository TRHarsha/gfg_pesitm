import streamlit as st

# Wrong code
wrong_code = """
#include <stdio.h>
#include <string.h>
int main()
{
    struct employee
    {
        char name[25];
        int age;
        float salary;
    };
    struct employee e;
    strcpy(name, "Shailesh");
    age = 25;
    salary = 15500.00;
    printf("%c %f %d\\n", name, age, salary);
    return 0;
}
"""

# Corrected code
corrected_code = """
#include <stdio.h>
#include <string.h>
int main()
{
    struct employee
    {
        char name[25];
        int age;
        float salary;
    };
    struct employee e;
    strcpy(e.name, "Shailesh");
    e.age = 25;
    e.salary = 15500.00;
    printf("%s %d %f\\n", e.name, e.age, e.salary);
    return 0;
}
"""

#wrong code 2
wrong_code2 ="""
#include <stdio.h>
int main()
{
    int arr[25], i, n;
    printf("\\nEnter 25 elements of array:\\n");
    for (i = 0; i < 25; i++)
    {
        scanf("%d", arr[i]); // Error: Missing '&' before 'arr[i]'
    }
    n = arr;                  // Error: Should be *arr
    for (i = 1; i <= 25; i++) // Error: Should be 'i < 25'
    {
        if (*(arr + i) < n)
            n = arr[i]; // Error: Should be *(arr + i)
    }
    printf("\\nSmallest number in the array is: %d\\n", n);
    return 0;
}
"""
# Corrected code 2
corrected_code2 = """
#include <stdio.h>
int main()
{
    int arr[25], i, n;
    printf("\\nEnter 25 elements of array:\\n");
    for (i = 0; i < 25; i++)
    {
        scanf("%d", &arr[i]);
    }
    n = *arr;
    for (i = 1; i < 25; i++)
    {
        if (*(arr + i) < n)
            n = *(arr + i);
    }
    printf("\\nSmallest number in the array is: %d\\n", n);
    return 0;
}
"""

#wrong code 3
wrong_code3 ="""
#include <stdio.h>
#include <string.h>

#define MAX_STUDENTS 100

struct student {
    char name[50];
    int age;
    float gpa;
};

void print_student(struct student s) {
    printf("Name: %s\\n", s.name);
    printf("Age: %d\\n", s.age);
    printf("GPA: %f\\n", s.gpa);
}

int main() {
    struct student students[MAX_STUDENTS];
    int num_students = 0;

    // Add first student
    strcpy(students[num_students].name, "Alice");
    students[num_students].age = 20;
    students[num_students].gpa = 3.75;
    num_students++;

    // Add second student
    strcpy(students.name, "Bob");
    students.age = 22;
    students.gpa = 3.85;
    num_students++;

    // Print all students
    for (int i = 0; i <= num_students; i++) {
        print_student(students[i]);
    }

    return 0;
}
"""

# Corrected code 3
corrected_code3 = """
#include <stdio.h>
#include <string.h>

#define MAX_STUDENTS 100

struct student {
    char name[50];
    int age;
    float gpa;
};

void print_student(struct student s) {
    printf("Name: %s\\n", s.name);
    printf("Age: %d\\n", s.age);
    printf("GPA: %.2f\\n", s.gpa);
}

int main() {
    struct student students[MAX_STUDENTS];
    int num_students = 0;

    // Add first student
    strcpy(students[num_students].name, "Alice");
    students[num_students].age = 20;
    students[num_students].gpa = 3.75;
    num_students++;

    // Add second student
    strcpy(students[num_students].name, "Bob");
    students[num_students].age = 22;
    students[num_students].gpa = 3.85;
    num_students++;

    // Print all students
    for (int i = 0; i< num_students; i++) {
        print_student(students[i]);
    }

    return 0;
}
"""

# Create a Streamlit app
st.title("Code Correction Challenge")

page = st.selectbox("Select a page", ["Page 1", "Page 2", "Page 3"])

if page == "Page 1":
    st.write("Correct the following code:")
    st.code(wrong_code, language="c")
    user_code = st.text_area("Enter the corrected code:", height=300, key="code1")
    submit_button = st.button("Submit")
    if submit_button:
        if user_code.strip() == corrected_code.strip():
            st.balloons()
            st.success("Congratulations! Your code is correct!")
            st.session_state.page_unlocked = True
        else:
            st.error("Sorry, your code is not correct. Try again!")
elif page == "Page 2":
    if "page_unlocked" in st.session_state and st.session_state.page_unlocked:
        st.write("Correct the following code:")
        st.code(wrong_code2, language="c")
        user_code2 = st.text_area("Enter the corrected code:", height=300, key="code2")
        submit_button2 = st.button("Submit", key="code2-submit")
        if submit_button2:
            if user_code2.strip() == corrected_code2.strip():
                st.balloons()
                st.success("Congratulations! Your code is correct!")
                st.session_state.page2_unlocked = True
            else:
                st.error("Sorry, your code is not correct. Try again!")
    else:
        st.error("You need to complete Page 1 first!")
elif page == "Page 3":
    if "page2_unlocked" in st.session_state and st.session_state.page2_unlocked:
        st.write("Correct the following code:")
        st.code(wrong_code3, language="c")
        user_code3 = st.text_area("Enter the corrected code:", height=300, key="code3")
        submit_button3 = st.button("Submit", key="code3-submit")
        if submit_button3:
            if user_code3.strip() == corrected_code3.strip():
                st.balloons()
                st.success("Congratulations! Your code is correct!")
            else:
                st.error("Sorry, your code is not correct. Try again!")
    else:
        st.error("You need to complete Page 2 first!")
