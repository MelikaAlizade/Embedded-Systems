def generate_cpp(sample_fsm):
    states = list(sample_fsm.keys())
    
    cpp_code = f"""
#include <iostream>
#include <string>
using namespace std;

enum State {{ {', '.join(states)} }};
State PS = {states[0]}, NS;
string event;

int main() {{
    while (true) {{
        switch (PS) {{
"""
    
    for state, details in sample_fsm.items():
        cpp_code += f"""
            case {state}:
"""
        
        for action in details["actions"]:
            cpp_code += f"                cout << \"{action}\" << endl;\n"
        
        cpp_code += "                cout << \"Enter event: \";\n                cin >> event;\n"
        
        for condition, next_state in details["transitions"].items():
            cpp_code += f"                if (event == \"{condition}\") NS = {next_state};\n"
        
        cpp_code += "                break;\n"
    
    cpp_code += """
        }
        PS = NS;
    }
    return 0;
}
"""
    
    return cpp_code

sample_fsm = {
    "S1": {
        "actions": ["Turn_off(Heater)", "Turn_off(Cooler)"],
        "transitions": {"T<15": "S3", "T>35": "S2"}
    },
    "S2": {
        "actions": ["Turn_off(Heater)", "Turn_on(Cooler)"],
        "transitions": {"T<25": "S1"}
    },
    "S3": {
        "actions": ["Turn_on(Heater)", "Turn_off(Cooler)"],
        "transitions": {"T>30": "S1"}
    }
}

cpp_code = generate_cpp(sample_fsm)

with open("fsm.cpp", "w") as file:
    file.write(cpp_code)

print("C++ code has been generated and saved as 'fsm.cpp'.")