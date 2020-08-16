"""@package docstring
# 0001
## Attention point
- Be consistent with your naming conventions. If there is a naming convention evident in any sample code, stick to it. Even if it is not the naming convention you usually use
- Recursive functions need to recurse and terminate. Make sure you understand how this happens so that you avoid bottomless callstacks
- We use the os module for interacting with the operating system in a way that is cross platform. You could say sChildPath = sPath + '/' + sChild but that wouldn't work on windows
- Familiarity with base packages is really worthwhile, but don't break your head trying to memorize everything, Google is your friend in the workplace!
- Ask questions if you don't understand what the code is supposed to do
- KISS! Keep it Simple, Stupid!
"""

def print_directory_contents(in_path):
    import os                                       
    for sChild in os.listdir(in_path):                
        sChildPath = os.path.join(in_path,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)

print_directory_contents(".") 