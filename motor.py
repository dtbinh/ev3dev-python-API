import os
import subprocess

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

class Motor():
    def __init__(self, port):
        for item in os.listdir("/sys/class/tacho-motor"):
            rpn = open("/sys/class/tacho-motor/" + item + "/address", "r")
            address = rpn.read()
            address = address.find(port)
            rpn.close()
            if address:
                print("####################################OK")
                self.port = port
                self.N = item
        command = open("/sys/class/tacho-motor/" + self.N + "/command", "w")
        command.write("reset")
        command.close()
    def load_new(self):
        for item in os.listdir("/sys/class/tacho-motor"):
            rpn = open("/sys/class/tacho-motor/" + item + "/address", "r")
            address = rpn.read()
            address = address.find(port)
            rpn.close()
            if address:
                self.port = port
                self.N = item
        command = open("/sys/class/tacho-motor/" + self.N + "/command", "w")
        command.write("reset")
        command.close()
    def run_forever(self, speed):
        command = open("/sys/class/tacho-motor/" + self.N + "/command", "w")
        command_speed = open("/sys/class/tacho-motor/" + self.N + "/speed_sp", "w")
        command_speed.write(str(speed))
        command_speed.close()
        command.write("run-forever")
        command.close()
    def stop(self):
        command = open("/sys/class/tacho-motor/" + self.N + "/command", "w")
        command.write("stop")
        command.close()
    def reset(self):
        command = open("/sys/class/tacho-motor/" + self.N + "/command", "w")
        command.write("reset")
        command.close()
    def address(self):
        command = open("/sys/class/tacho-motor/" + self.N + "/address", "r")
        address = str(command.read())
        command.close()
        address = address.replace("\n", "")
        return address
    def commands(self):
        command = open("/sys/class/tacho-motor/" + self.N + "/commands", "r")
        commands = str(command.read())
        command.close()
        return commands
    def command(self, value):
        command = open("/sys/class/tacho-motor/" + self.N + "/command", "w")
        command.write(value)
        command.close()
    def position(self):
        command = open("/sys/class/tacho-motor/" + self.N + "/position", "r")
        positon = str(command.read())
        command.close()
        return position
    def count_per_rot(self):
        command = open("/sys/class/tacho-motor/" + self.N + "/count_per_rot", "r")
        c_p_r = str(command.read())
        command.close()
        return c_p_r
    def speed(self):
        command = open("/sys/class/tacho-motor/" + self.N + "/speed", "r")
        speed = str(command.read())
        command.close()
        return speed
    def driver_name(self):
        command = open("/sys/class/tacho-motor/" + self.N + "/driver_name", "r")
        d_n = str(command.read())
        command.close()
        return d_n
    def duty_cycle(self):
        command = open("/sys/class/tacho-motor/" + self.N + "/duty_cycle", "r")
        d_c = str(command.read())
        command.close()
        return d_c
    def max_speed(self):
        command = open("/sys/class/tacho-motor/" + self.N + "/max_speed", "r")
        m_s = str(command.read())
        command.close()
        return m_s
    def ramp_down_sp(self):
        command = open("/sys/class/tacho-motor/" + self.N + "/ramp_down_sp", "r")
        r_d_s = str(command.read())
        command.close()
        return r_d_p
    def ramp_up_sp(self):
        command = open("/sys/class/tacho-motor/" + self.N + "/ramp_up_sp", "r")
        r_u_s = str(command.read())
        command.close()
        return r_u_p
    def state(self):
        command = open("/sys/class/tacho-motor/" + self.N + "/state", "r")
        state = str(command.read())
        command.close()
        return state
    def polarity(self):
        command = open("/sys/class/tacho-motor/" + self.N + "/polarity", "r")
        polarity = str(command.read())
        command.close()
        return polarity
    def stop_actions(self):
        command = open("/sys/class/tacho-motor/" + self.N + "/stop_actions", "r")
        s_a = str(command.read())
        command.close()
        return s_a
    def position_sp(self):
        command = open("/sys/class/tacho-motor/" + self.N + "/position_sp", "r")
        positon_sp = str(command.read())
        command.close()
        return position_sp
    def speed_pid(self):
        command = open("/sys/class/tacho-motor/" + self.N + "/speed_pid", "r")
        s_p = str(command.read())
        command.close()
        return s_p
    def speed_sp(self):
        command = open("/sys/class/tacho-motor/" + self.N + "/speed_sp", "r")
        s_s = str(command.read())
        command.close()
        return s_s
    def stop_action(self, value):
        command = open("/sys/class/tacho-motor/" + self.N + "/stop_action", "w")
        command.write(value)
        command.close()
