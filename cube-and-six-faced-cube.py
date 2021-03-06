#!/usr/bin/python
# -*- coding: utf-8 -*-
# team epsilon
# udit malik and max kirimi

from time import sleep
import tellopy

def handler(
    event,
    sender,
    data,
    **args
    ):
    drone = sender
    if event is drone.EVENT_FLIGHT_DATA:
        print data

# makes the drone go forward by some arbitrary distance
def go_one_unit_forward(drone):
    drone.forward(30)
    sleep(2)
    drone.forward(0)

# makes the drone turn by approximately 90 degrees (a right angle) clockwise
def turn_clockwise(drone):
    drone.clockwise(88)
    sleep(1.24)
    drone.clockwise(0)

# makes the drone go down by some arbitrary distance
def go_one_unit_down(drone):
    drone.down(30)
    sleep(2)
    drone.down(0)

# makes the drone go up by some arbitrary distance, same distance as go_one_unit_down
def go_one_unit_up(drone):
    drone.up(30)
    sleep(2)
    drone.up(0)


def test():
    drone = tellopy.Tello()
    try:
        drone.subscribe(drone.EVENT_FLIGHT_DATA, handler)
    
        # connects with the drone and performs a simple takeoff
        drone.connect()
        drone.wait_for_connection(60.0)
        drone.takeoff()
        sleep(3)

        # lifts the drone up and makes it ready to receive more commands
        drone.up(20)
        sleep(3)
        drone.up(0)

        # draws the top square base of the cube
        for i in range(4):
            go_one_unit_forward(drone)
            turn_clockwise(drone)

        # goes down to draw the bottom face of the cube
        go_one_unit_down(drone)

        # draws the bottom square base of the cube
        for i in range(4):
            go_one_unit_forward(drone)
            turn_clockwise(drone)

        # the following code draws the vertical sides of the cube
        go_one_unit_forward(drone)
        go_one_unit_up(drone)
        turn_clockwise(drone)

        go_one_unit_forward(drone)
        turn_clockwise(drone)

        go_one_unit_down(drone)
        go_one_unit_forward(drone)
        go_one_unit_up(drone)

        # starts bringing the drone down indefinitely until it reaches the ground
        drone.down(10)
        sleep(3)

        # performs the landing 
        drone.land()
        sleep(3)
        
    except Exception, ex:
        print ex
    finally:
        # shuts the drone off
        drone.quit()


if __name__ == '__main__':
    test()
