import random


def testStrategy(strategy, rounds):
  scores = {}
  for choice_num, opponent_strategy in strategies.items():
    scores[opponent_strategy.__name__] = play_rounds(strategy,
                                                     opponent_strategy, rounds)

  print(
      f"Scores for strategy {strategy.__name__} against all other strategies and itself:"
  )
  for opponent_strategy, score in scores.items():
    print(f"Against {opponent_strategy}: {score}")


def play_rounds(strategy1, strategy2, rounds):
  score1 = 0
  score2 = 0
  for _ in range(rounds):
    choice1 = strategy1()
    choice2 = strategy2()
    if choice1 == choice2:
      if choice1 == 'C':
        score1 += 3
        score2 += 3
      else:
        score1 += 1
        score2 += 1
    else:
      if choice1 == 'C':
        score2 += 5
      else:
        score1 += 5
  return score1, score2


# Example strategies
def alwaysCollude():
  return 'C'


def alwaysDefect():
  return 'D'


# Add other strategies here...

strategies = {
    1: alwaysCollude,
    2: alwaysDefect,
    # Add other strategies here...
}

# Test the strategy
testStrategy(alwaysCollude, 20)
