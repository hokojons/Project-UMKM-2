# test_context_switch.py
from abstract_system_constants import *
from time_slice import time_slice

def initialize_system():
    # Create system state (simulating 16MB memory)
    systemState = [0] * systemStateSz
    
    # Initialize registers
    registers = [6] * 23  # R0-R15 + special registers
    
    # Set initial stack pointer (MSP)
    registers[MSP] = STACK
    
    # Initialize two tasks
    for task_id in [0, 5]:
        tcb_addr = TCB_OFFSET + task_id * TCB_SZ
        # Store recognizable values in each register slot
        for reg in range(NREGS_CONTEXT):
            systemState[tcb_addr + reg] = task_id * 100 + reg
    
    # Set initial PID
    systemState[PID] = 0
    
    return systemState, registers

def print_state(systemState, registers, msg):
    print(f"\n{msg}:")
    print(f"Current PID: {systemState[PID]}")
    print(f"Registers R0-R15: {registers[:16]}")
    print(f"MSP: 0x{registers[MSP]:X}")

def main():
    # Initialize system
    systemState, registers = initialize_system()
    print_state(systemState, registers, "Initial state (Task 0)")
    
    # Perform context switch
    systemState, registers = time_slice(systemState, registers)
    print_state(systemState, registers, "After first switch (Task 1)")
    
    # Switch back
    systemState, registers = time_slice(systemState, registers)
    print_state(systemState, registers, "After second switch (Task 0)")

if __name__ == "__main__":
    main()