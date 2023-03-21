install.packages('Tmisc')
library(Tmisc)
data(quartet)
View(quartet)

quartet %>% 
  group_by(set) %>%
  summarize(mean(x), sd(x), mean(y),sd(y), cor(x,y)) # sd() = standard deviation, cor() = corelation 


install.packages("SimDesign")
library(SimDesign)

actual_temp <- c(68.3, 70, 72.4, 71, 67, 70)
predicted_temp <- c(67.9, 69, 71.5, 70, 67, 69)
bias(actual_temp, predicted_temp)

library("palmerpenguins")
head(penguins)
penguins %>%
  drop_na() %>%
  group_by(species) %>%
  summarize(mean_body = mean(body_mass_g), min = min(year), max = max(year))
