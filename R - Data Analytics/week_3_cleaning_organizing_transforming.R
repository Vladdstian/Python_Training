library("here")
library("dplyr")
library("skimr")
library("janitor")
library("palmerpenguins")
library(tidyverse)
library(tidyr)

# read_csv("filename.csv") when you want to load a file

# CLEANING UP THE DATA
skim_without_charts(penguins) # summary of the dataset, a number of rows and columns, column types and a summary of all the data types contained in the data frame
glimpse(penguins) # shorter summary of the data
head(penguins) # gives the first 6 lines of the data set and the column names

penguins %>% 
  select(-species) # having the minus in front will print every column but species

penguins %>% 
  rename(island_new=island) # changes the island column name into island_new

rename_with(penguins, tolower) # changes the column names to lower case

clean_names(penguins) # ensures that the names have only characters, numbers and underscores

# ORGANIZE AND FILTER DATA
penguins %>% 
  arrange(bill_length_mm) # it returns a tibble arranged in ascending order by the column specified in paranthesis

penguins %>% 
  arrange(-bill_length_mm) # it returns a tibble arranged in descending order ("-" sign) by the column specified in paranthesis

penguins2 <- penguins %>% arrange(-bill_length_mm) # saves a new data frame based on the pipe operation

penguins %>% group_by(island) %>% drop_na() %>% summarize(mean_bill_length_mm = mean(bill_length_mm))
#function above groups data by island, removes the missing values and creates a new column where the mean of a column is calculated

penguins %>% filter(species == "Adelie") # filters the data to only have the penguin type "Adelie"


# TRANSFORMING DATA
id <- c(1:10)

name <- c("John Mendes", "Rob Stewart", "Rachel Abrahamson", "Christy Hickman", "Johnson Harper", "Candace Miller", "Carlson Landy", "Pansy Jordan", "Darius Berry", "Claudia Garcia")

job_title <- c("Professional", "Programmer", "Management", "Clerical", "Developer", "Programmer", "Management", "Clerical", "Developer", "Programmer")

employee <- data.frame(id,name,job_title)

print(employee)

separate(employee, name, into=c('first_name', 'last_name'), sep=' ') # separates a column

# unite() - does the opposite of separate function

penguins %>% 
  mutate(body_mass_kg=body_mass_g/1000, flipper_length_m=flipper_length_mm/1000) # adds a new column based on a calculation of another column

penguins %>% arrange(bill_length_mm)