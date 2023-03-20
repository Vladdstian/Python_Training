# Operations and Calculations
# first calculations
quarter_1_sales <- 35657.5554
quarter_2_sales <- 43810.65
midyear_sales <- quarter_1_sales + quarter_2_sales
yearend_sales <- midyear_sales * 2
yearend_sales

# conditional operators and logical operators
x <- 4
if (x > 0 & x < 4) {
  print("x is a positive number between 0 and 4")
}else if (x == 4){
  print("x is 4")
}else{
  print("x is bigger than 4")
}
