# Recommender System

## Collaborative Filtering

- Algorithm is very similar to the linear regression
  ![cost](full-cost-f.png)
- Collaborative Filtering Problem Motivation -> predict x features
  ![colla](collaborative-filtering.png)
- Gradient Descent of collaborative filtering
  ![grad-desc](gradient-des.png)
- Example applications (binary classification) -> digital market
  ![ex-app](ex-app.png)

## Recommender Systems Implementation Detail

- Mean normalization helps users that haven't rate any movie (means all ?) to get recommendations
  ![mean](mean-n-idea.png)
- Calculations mean normalization
  ![calc](mean-n-ex.png)
- Custom Function to calculate a derivatives
  ![auto-diff](auto-diff.png)
- With Adam
  ![adam](auto-adam.png)
- We can't implement collaborative filtering with the mode.fit and predict so we need to implement the cost function ourselves.
- Collaborative filtering can be used to find related items such as movies, online shops, etc.
  ![idea](find-related.png)
- Limitations of collaborative filtering
  ![limit](limit.png) -> content based filtering exist to overcome this limitations

## Content-based filtering

- Content based vs Collaborative
  ![vss](content-vs-collaborative.png)
- Example of features
  ![feat-content](ex-features-content.png)
- Deep Learning for content-based filtering architecture
  ![architecture](nn-arc-content.png)
- How to efficiently find recommendations from a large sets of items?
  ![problem](large-scale-prob.png)
  ![idea](idea-to-implement.png)
  - Retrieval step -> more items = better performance, slower recommendations. Analyze the trade off -> offline experiment to see if retrieving additional items results in more relevant recommendations ( y[i,j] = 1 ) (mungkin kek, sebanyak apa sih yang diklik sama si user?)
  - Ranking Step
    ![ranking](ranking-step.png)
- The goal of the recommender system
  ![goal](goal.png)
  - The problem is "how do we get to filter what the users consume if the content is toxic or bad"
- Implement content based filtering
  ![imp](implementation.png)
