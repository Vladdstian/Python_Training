library(ggplot2)
library(tidyverse)
data("diamonds")
# View(diamonds) - shows the entire data frame
head(diamonds) # - shows only the header - first 6 lines
str(diamonds) # - highlights the structure of data frame
colnames(diamonds) # - prints the column names 
mutate(diamonds, carat_2=carat*100)