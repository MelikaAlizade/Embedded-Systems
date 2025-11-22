main_state = 1
cooler_fan_state = 0
heater_fan_state = 0

while True:
    user_input = input("Enter temperature or 'exit' to quit: ")
    if user_input.lower() == "exit":
        break
    temperature = int(user_input)

    if main_state == 1:
        if temperature < 15:
            main_state = 3
        elif temperature > 35:
            main_state = 2
    elif main_state == 2:
        if temperature < 25:
            main_state = 1
    elif main_state == 3:
        if temperature > 30:
            main_state = 1  
    
    if main_state == 3:
        if heater_fan_state == 0:
            heater_fan_state = 1
        elif heater_fan_state == 1:
            if temperature < 5:
                heater_fan_state = 2
            elif temperature > 30:
                heater_fan_state = 0
        elif heater_fan_state == 2:
            if temperature < 0:
                heater_fan_state = 3
            elif temperature > 10:
                heater_fan_state = 1
        elif heater_fan_state == 3:
            if temperature > 5:
                heater_fan_state = 2
    else:
        heater_fan_state = 0

    if main_state == 2:
        if cooler_fan_state == 0:
            cooler_fan_state = 1
        elif cooler_fan_state == 1:
            if temperature > 40:
                cooler_fan_state = 2
            elif temperature < 25:
                cooler_fan_state = 0
        elif cooler_fan_state == 2:
            if temperature > 45:
                cooler_fan_state = 3
            elif temperature < 35:
                cooler_fan_state = 1
        elif cooler_fan_state == 3:
            if temperature < 40:
                cooler_fan_state = 2
    else:
        cooler_fan_state = 0  

    cooler = main_state == 2
    heater = main_state == 3
    cooler_rotational_speed = [0, 4, 6, 8][cooler_fan_state]
    heater_rotational_speed = [0, 4, 6, 8][heater_fan_state]
    
    print("Cooler Fan State: ", cooler_fan_state)
    print("Heater Fan State: ", heater_fan_state)
    print(f"Main State: {main_state}, Cooler Speed: {cooler_rotational_speed},Heater Speed: {heater_rotational_speed}, Heater: {heater}, Cooler: {cooler}")
