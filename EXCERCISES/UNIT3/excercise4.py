import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    def run_ball_sim(balls_picked, num_sim):
        success = 0
        for i in range(num_sim):
            bucket = random.sample(['r', 'g'], counts = [3,3], k =5)
            picked = []            

            for i in range(balls_picked):
                if i < balls_picked:
                    picked.append(bucket.pop())
            if not ('r' in picked and 'g' in picked):
                success += 1

        return success/num_sim
    
    return round(run_ball_sim(3, numTrials), 3)

print(noReplacementSimulation(5000))

        