import os

#port is the variable that takes a port name.
#here is a list of ports with descriptions:
#Port             |Description
#-----------------------------------------
#outA             |Is the output A port
#outB             |Is the output B port
#outC             |Is the output C port
#outD             |Is the output D port
#in1              |Is the input 1 port
#in2              |Is the input 2 port
#in3              |Is the input 3 port
#in4              |Is the input 4 port

#What motor.py does?
#If you call one of the following methods,
#this API will open a specified file and read or write to that file!
#This API is based on the driver documentation to find on ev3dev.org
class Motor():
    def __init__(self, port):
	#list all motors and reads their address (port name) and compare it with 'port'
	#NOTE: I know, its not beautiful code there, but i have no idea, why i can't read the file 'address' and compare it with 'port' directly!
	#If I understand my script correctly, it founds a '\n' in the file that stores the port name
	#But its seems to be not correct!
	#if address == port:
	#	self.port = port
	#	self.N = item
        for item in os.listdir("/sys/class/tacho-motor"):
            rpn = open("/sys/class/tacho-motor/" + item + "/address", "r")
            address = rpn.read()
            address = address.replace("\n", "")
            rpn.close()
            if address == port:
                print(port + " found as " + item)
                #if the port name can be found in address, then execute the code below
                self.port = port
                self.N = item
                break
        try:
            os.system("sudo chown root:root /sys/class/tacho-motor/"+ self.N + "/command")
            os.system("sudo chmod u+rw /sys/class/tacho-motor/"+ self.N + "/command")
            os.system("sudo chmod g+rw /sys/class/tacho-motor/" + self.N + "/command")
        except:
            return "An error occurred while executing the following commands: 'sudo chown root:root /sys/class/tacho-motor/"+ self.N + "/command', 'sudo chmod u+rw /sys/class/tacho-motor/"+ self.N + "/command', 'sudo chmod g+rw /sys/class/tacho-motor/"+ self.N + "/command'. Maybe you are not root?"
        finally:
            #sends a reset command to the motor to use it        
            command = open("/sys/class/tacho-motor/" + self.N + "/command", "w")
            command.write("reset")
            command.close()
            return None
    def load_new(self):
        #finds the number of the port again, its useful, if an error occurred during writing a file
        for item in os.listdir("/sys/class/tacho-motor"):
            rpn = open("/sys/class/tacho-motor/" + item + "/address", "r")
            address = rpn.read()
            address = address.replace("\n", "")
            rpn.close()
            if address == port:
                print(port + " found as " + item)
                #if the port name can be found in address, then execute the code below
                self.port = port
                self.N = item
                break
        command = open("/sys/class/tacho-motor/" + self.N + "/command", "w")
        command.write("reset")
        command.close()
    def run_forever(self, speed):
        print(self.port + " runs in run_forever mode")
	#runs the motor with the given speed until another command is send
        command = open("/sys/class/tacho-motor/" + self.N + "/command", "w")
        command_speed = open("/sys/class/tacho-motor/" + self.N + "/speed_sp", "w")
        command_speed.write(str(speed))
        command_speed.close()
        command.write("run-forever")
        command.close()
    def run_to_abs_pos(self, position):
	#runs the motor to the given position
        command = open("/sys/class/tacho-motor/" + self.N + "/command", "w")
        command_pos = open("/sys/class/tacho-motor/" + self.N + "/position_sp", "w")
        command_pos.write(str(position))
        command_pos.close()
        command.write("run-to-abs-pos")
        command.close()
    def run_to_rel_pos(self, position):
	#runs the motor to a position relative to the given position value
        command = open("/sys/class/tacho-motor/" + self.N + "/command", "w")
        command_pos = open("/sys/class/tacho-motor/" + self.N + "/position", "w")
        command_pos.write(str(position))
        command_pos.close()
        command.write("run-to-rel-pos")
        command.close()
    def run_timed(self, time):
	#runs the motor for the given time (in seconds)
        command = open("/sys/class/tacho-motor/" + self.N + "/command", "w")
        command_time = open("/sys/class/tacho-motor/" + self.N + "/time_sp", "w")
        command_time.write(str(time))
        command_time.close()
        command.write("run-timed")
        command.close()
    def run_direct(self, speed):
	#runs the motor with the given speed
        command = open("/sys/class/tacho-motor/" + self.N + "/command", "w")
        command_speed = open("/sys/class/tacho-motor/" + self.N + "/duty_cycle_sp", "w")
        command_speed.write(str(speed))
        command_speed.close()
        command.write("run-direct")
        command.close()
    def stop(self):
	#stops the motor
        command = open("/sys/class/tacho-motor/" + self.N + "/command", "w")
        command.write("stop")
        command.close()
    def reset(self):
	#resets the motor parameters to their default values
        command = open("/sys/class/tacho-motor/" + self.N + "/command", "w")
        command.write("reset")
        command.close()
    def address(self):
	#returns the address (An address is the port name of the connected motor)
        command = open("/sys/class/tacho-motor/" + self.N + "/address", "r")
        address = str(command.read())
        command.close()
        address = address.replace("\n", "")
        return address
    def commands(self):
	#returns a space seperated list of availiable commands for the motor
        command = open("/sys/class/tacho-motor/" + self.N + "/commands", "r")
        commands = str(command.read())
        command.close()
        return commands
    def command(self, value):
	#sends a command
        command = open("/sys/class/tacho-motor/" + self.N + "/command", "w")
        command.write(value)
        command.close()
    def position(self, value=None):
	#reads or write the position
        if value == None:
            command = open("/sys/class/tacho-motor/" + self.N + "/position", "r")
            position = str(command.read())
            command.close()
            return position
        else:
            command = open("/sys/class/tacho-motor/" + self.N + "/position", "w")
            command.write(str(value))
            command.close()
    def count_per_rot(self):
	#returns the number of tacho counts in one rotation
        command = open("/sys/class/tacho-motor/" + self.N + "/count_per_rot", "r")
        c_p_r = str(command.read())
        command.close()
        return c_p_r
    def speed(self):
	#returns the speed
        command = open("/sys/class/tacho-motor/" + self.N + "/speed", "r")
        speed = str(command.read())
        command.close()
        return speed
    def driver_name(self):
	#returns the driver name
        command = open("/sys/class/tacho-motor/" + self.N + "/driver_name", "r")
        d_n = str(command.read())
        command.close()
        return d_n
    def duty_cycle(self):
	#returns the duty_cycle
        command = open("/sys/class/tacho-motor/" + self.N + "/duty_cycle", "r")
        d_c = str(command.read())
        command.close()
        return d_c
    def duty_cycle_sp(self, value):
	#sets the duty cycle
        command = open("/sys/class/tacho-motor/" + self.N + "/duty_cycle_sp", "w")
        command.write(str(value))
        command.close()
    def max_speed(self):
	#returns the maximum speed
        command = open("/sys/class/tacho-motor/" + self.N + "/max_speed", "r")
        m_s = str(command.read())
        command.close()
        return m_s
    def ramp_down_sp(self, value=None):
	#reads or writes the ramp down
        if value == None:
            command = open("/sys/class/tacho-motor/" + self.N + "/ramp_down_sp", "r")
            r_d_s = str(command.read())
            command.close()
            return r_d_s
        else:
            command = open("/sys/class/tacho-motor/" + self.N + "/ramp_down_sp", "w")
            command.write(str(value))
            command.close()
    def ramp_up_sp(self, value):
	#reads or writes the ramp up
        if value == None:
            command = open("/sys/class/tacho-motor/" + self.N + "/ramp_up_sp", "r")
            r_u_s = str(command.read())
            command.close()
            return r_u_s
        else:
            command = open("/sys/class/tacho-motor/" + self.N + "/ramp_up_sp", "w")
            command.write(str(value))
            command.close()
    def state(self):
	#returns a space seperated list of state flags
        command = open("/sys/class/tacho-motor/" + self.N + "/state", "r")
        state = str(command.read())
        command.close()
        return state
    def polarity(self, value=None):
	#reads or writes the polarity of the motor
        if value == None:
            command = open("/sys/class/tacho-motor/" + self.N + "/polarity", "r")
            polarity = str(command.read())
            command.close()
            return polarity
        else:
            command = open("/sys/class/tacho-motor/" + self.N + "/polarity", "w")
            command.write(str(value))
            command.close()
    def stop_actions(self):
	#returns a space seperated list of availiable stop actions
        command = open("/sys/class/tacho-motor/" + self.N + "/stop_actions", "r")
        s_a = str(command.read())
        command.close()
        return s_a
    def hold_pid_Kd(self, value=None):
	#reads or write the derivative constant for the position PID
        if value == None:
            command = open("/sys/class/tacho-motor/" + self.N + "/hold_pid/Kd", "r")
            Kd = str(command.read())
            command.close()
            return Kd
        else:
            command = open("/sys/class/tacho-motor/" + self.N + "/hold_pid/Kd", "w")
            command.write(str(value))
            command.close()
    def hold_pid_Ki(self, value=None):
	#reads or writes the integral constant for the position PID
        if value == None:
            command = open("/sys/class/tacho-motor/" + self.N + "/hold_pid/Ki", "r")
            Ki = str(command.read())
            command.close()
            return Ki
        else:
            command = open("/sys/class/tacho-motor/" + self.N + "/hold_pid/Ki", "w")
            command.write(str(value))
            command.close()
    def hold_pid_Kp(self, value=None):
	#reads or writes the proportional constant for the position PID
        if value == None:
            command = open("/sys/class/tacho-motor/" + self.N + "/hold_pid/Kp", "r")
            Kp = str(command.read())
            command.close()
            return Kp
        else:
            command = open("/sys/class/tacho-motor/" + self.N + "/hold_pid/Kp", "w")
            command.write(str(value))
            command.close()
    def position_sp(self, value=None):
	#reads or writes the position speed
        if value == None:
            command = open("/sys/class/tacho-motor/" + self.N + "/position_sp", "r")
            position_sp = str(command.read())
            command.close()
            return position_sp
        else:
            command = open("/sys/class/tacho-motor/" + self.N + "/position_sp", "w")
            command.write(str(value))
            command.close()
    def speed_sp(self, value=None):
	#writing sets the target speed in tacho counts per second used for all run-* commands except run-direct. Reading returns the current value.
        if value == None:
            command = open("/sys/class/tacho-motor/" + self.N + "/speed_sp", "r")
            s_s = str(command.read())
            command.close()
            return s_s
        else:
            command = open("/sys/class/tacho-motor/" + self.N + "/speed_sp", "w")
            command.write(str(value))
            command.close()
    def stop_action(self, value=None):
	#reads or writes a stop action command
        if value == None:
            command = open("/sys/class/tacho-motor/" + self.N + "/stop_action", "r")
            s_p = str(command.read())
            command.close()
            return s_p
        else:
            command = open("/sys/class/tacho-motor/" + self.N + "/stop_action", "w")
            command.write(value)
            command.close()
    def count_per_m(self):
	#returns the number of tacho counts in one meter of travel of the motor.
        command = open("/sys/class/tacho-motor/" + self.N + "/count_per_m", "r")
        c_p_m = str(command.read())
        command.close()
        return c_p_m
    def full_travel_count(self):
	#returns the number of tacho counts in the full travel of the motor.
        command = open("/sys/class/tacho-motor/" + self.N + "/full_travel_count", "r")
        c_t_c = str(command.read())
        command.close()
        return c_t_c
    def speed_pid_Kd(self, value=None):
	#reads or writes the derivative constant for the speed regulation PID
        if value == None:
            command = open("/sys/class/tacho-motor/" + self.N + "/speed_pid/Kd", "r")
            Kd = str(command.read())
            command.close()
            return Kd
        else:
            command = open("/sys/class/tacho-motor/" + self.N + "/speed_pid/Kd", "w")
            command.write(str(value))
            command.close()
    def speed_pid_Ki(self, value=None):
	#reads or writes the integral constant for the speed regulation PID
        if value == None:
            command = open("/sys/class/tacho-motor/" + self.N + "/speed_pid/Ki", "r")
            Ki = str(command.read())
            command.close()
            return Ki
        else:
            command = open("/sys/class/tacho-motor/" + self.N + "/speed_pid/Ki", "w")
            command.write(str(value))
            command.close()
    def speed_pid_Kp(self, value=None):
	#reads or writes the proportional constant for the speed regulation PID
        if value == None:
            command = open("/sys/class/tacho-motor/" + self.N + "/speed_pid/Kp", "r")
            Kp = str(command.read())
            command.close()
            return Kp
        else:
            command = open("/sys/class/tacho-motor/" + self.N + "/speed_pid/Kp", "w")
            command.write(str(value))
            command.close()
    def time_sp(self, value=None):
	#reads or writes the run time for the motor (in secnds)
        if value == None:
            command = open("/sys/class/tacho-motor/" + self.N + "/time_sp", "r")
            t_s = str(command.read())
            command.close()
            return t_s
        else:
            command = open("/sys/class/tacho-motor/" + self.N + "/time_sp", "w")
            command.write(str(value))
            command.close()
class commander():
    def __init__(self, port):
    #list all motors and reads their address (port name) and compare it with 'port'
    #NOTE: I know, its not beautiful code there, but i have no idea, why i can't read the file 'address' and compare it with 'port' directly!
    #If I understand my script correctly, it founds a '\n' in the file that stores the port name
    #But its seems to be not correct!
    #if address == port:
    #	self.port = port
    #	self.N = item
        for item in os.listdir("/sys/class/tacho-motor"):
            rpn = open("/sys/class/tacho-motor/" + item + "/address", "r")
            address = rpn.read()
            rpn.close()
            if address.find(port) > -2:
                #if the port name can be found in address, then execute the code below
                self.port = port
                self.N = item
                #sends a reset command to the motor to use it
            command = open("/sys/class/tacho-motor/" + self.N + "/command", "w")
            command.write("reset")
            command.close()
    def load_new(self):
	#finds the number of the port again, its useful, if an error occurred during writing a file
        for item in os.listdir("/sys/class/tacho-motor"):
            rpn = open("/sys/class/tacho-motor/" + item + "/address", "r")
            address = rpn.read()
            rpn.close()
            if address.find(port) > -2:
                self.port = port
                self.N = item
        command = open("/sys/class/tacho-motor/" + self.N + "/command", "w")
        command.write("reset")
        command.close()
    def command(self, key=None, value=None):
	#key is the name of the file in /sys/class/tacho-motor/motor<N>
	#<N> is the count of the inizialisation and the path of the motor
	#value is the value of key
	#if you call this without arguments, this method will return you a list of availiable commands for the motor
	#if you call this with the key argument, this method will return the value of 'key'
	#if you call this with the two arguments, this method will write the 'value' in the file 'key'
        availiable_commands = []
        if key == None:
            for item in os.listdir("/sys/class/tacho-motor/" + self.N):
                availiable_commands.append(str(item))
                return availiable_commands
        elif value == None:
            command = open("/sys/class/tacho-motor/" + self.N + str(key), "r")
            read_value = str(command.read())
            command.close()
            return read_value
        else:
            command = open("/sys/class/tacho-motor/" + self.N + str(key), "w")
            command.write(str(value))
            command.close()
    def reset(self):
        command = open("/sys/class/tacho-motor/" + self.N + "/command", "w")
        command.write("reset")
        command.close()
