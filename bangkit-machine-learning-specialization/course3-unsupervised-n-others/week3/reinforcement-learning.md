# Reinforcement Learning

## Introduction

- Applications
  ![app](applications.png)
- The return -> rewards that you can get quicker instead taking the path into the long one
  ![return](return.png)
- Discounnt Factor -> how much less a dollar in the future worth compare to a dollar today
- Policy
  ![policy](policy.png)
- The goal of reinforcement is to find the policies
- key concepts
  ![keys](keys.png)
- Markov Decision Process
  ![mdp](mdp.png)

## State-action value function

- Picking Actions
  ![q](compute-sa-q-f.png)
- State-action value function -> discount factor closer to 1 = more patient to achieve the higher reward
- Bellman Equation
  ![bell](bell.png)
  ![bell2](bell2.png)

## Continuous State Spaces

- Reward Function Lunar Lander Problem
  ![reward](reward-f.png)
- Deep Reinforcement Learning
  - Architecture
    ![arc](nn-arch.png)
  - Learning Algorithm (DQN) -> (Deep-Q Network)
    ![dqn](learning-algo.png)
- Refining the Algorithm
  ![r-arc](r-algo.png)
- Epsilon Greedy Policy -> choose action while learning
  ![a](chose-act-while-learn.png)
- Mini-batch -> if u have 100.000.000 training dataset, is too much to compute, then u split it into a 1000 each.
  ![mini-batch](mini-batch.png)
  Mini batch with Adam is more useable in the practical
  ![grad](grad-decent-mini.png)
  Mini batch in reinforcement
  ![mini2](mini-batch-2.png)
- Soft update is to prevent the update on the Q to Qnew without overwriting it
  ![softupdate](soft-update.png)
- Limitations with Reinforcement Learning
  ![limit](limit.png)

## Summary

![summary](summary.png)
