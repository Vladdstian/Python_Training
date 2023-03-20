# Here's an example of a variable
first_variable <- "This is my variable" # string variable
second_variable <- 25.5 # numeric variable
vec_1 <- c(13, 48,6, 71, 101.5, 55) # vector example
lst_1 <- list(13L, 45.2, "a", "something_else") # list example
str(lst_1) # shows the structure of the list inside the parenthesis
today() # prints out today date
now() # prints out today date and the time (hours:minutes:sec)
date_1 <- ymd("2021/08/01") # converts the string into a date object and saves it to date_1 variable
date_2 <- mdy_hms("01/20/2021 20:11:59") # converts the string into a date + time object and saves it to date_2 variable
new_df <- data_frame(x=c(1,2,3), y=c(1.5,5.5,7.5)) # example of a data frame structure
matrix_1 <- matrix(c(3:8), nrow = 2) # example of a matrix in R