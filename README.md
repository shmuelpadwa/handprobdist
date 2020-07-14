# handprobdist

This is just a probability distribution calculator I made for hearts. I'm sure this data is already available, but I wanted to find it testably myself. Actual math could probably find this too, but this seemed faster.

The actual values can be found in the HeartsDistribution csv file.

As usual, after finishing this project(It took like 3 hours cause matplotlib hates me), I googled it and found someone else who did it much, much better. Check them out:
http://www.occasionalenthusiast.com/bridge-hand-probability-analysis/

Edit June 14 2020 4:14 AM GMT: This has some massive bug. It consistently has 4432 at 16-17, when it should be above 21, and has 6421 above 6322, when it should be about a percentage point below. 7321 also comes at about double the expected rate, hitting 3.6% instead of 1.8%. Not sure why. I'll look in the morning.
