'''
You have recently discovered thar horses travel in a unique pattern - they're
either running (at top speed) or resting (standing still).

Here's an example of how one particular horse might travel:

The horse Blaze can run at 14 metres/second for 60 seconds, but must then rest for 45 seconds.

After 500 seconds Blaze will have traveled 4200 metres.

Your job is to write a function that returns how long a horse will have traveled after a given time.

####Input:
    totalTime - How long the horse will be traveling (in seconds)

    runTime - How long the horse can run for before having to rest (in seconds)

    restTime - How long the horse have to rest for after running (in seconds)

    speed - The max speed of the horse (in metres/second)
'''

def travel(total_time, run_time, rest_time, speed):
    seconds=0

    while total_time>0:
        if total_time-run_time<=0:
            seconds+=total_time
            break
        else:
            total_time-=run_time
            total_time-=rest_time
            seconds+=run_time
    return seconds*speed

travel(35869784, 90, 100, 5)
#Returns: 84954920
