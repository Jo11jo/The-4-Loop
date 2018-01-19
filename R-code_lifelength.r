library('tidyverse')
library('ggplot2')
----------------------------------------------------------------------------------------------------------

#The csv-files created by python have two columns each: "birthYear" and "deathYear"
year_1820 <- read.csv("1820.csv")
year_1920 <- read.csv("1920.csv")
#Now all the information we need (birth and death years per person) is in these data frames

#1820:
#converting into numeric data so we can make calculations
eighteenhundred <- year_1820

eighteenhundred$deathYear <- as.numeric(eighteenhundred$deathYear) 

eighteenhundred$birthYear <- as.numeric(eighteenhundred$birthYear) 

#We create a seperate column with the life-length of each person in 1820
complete18 <- eighteenhundred %>%
  mutate(lifetime = deathYear - birthYear)

#1920:
#converting into numeric data so we can make calculations
nineteenhundred <- year_1920

nineteenhundred$deathYear <- as.numeric(nineteenhundred$deathYear) 

nineteenhundred$birthYear <- as.numeric(nineteenhundred$birthYear) 

#We create a seperate column with the life-length of each person in 1920
complete19 <- nineteenhundred %>%
  mutate(lifetime = deathYear - birthYear)

#For these two years we calculate the mean and create a data frame with both years and both means
mean18 <- mean(complete18$lifetime)
mean19 <- mean(complete19$lifetime)
year <- c ('1820', '1920')
mean <- c (mean18, mean19)
means_frame <- data.frame(year, mean)

#This data frame is plotted in a bar graph
ggplot() +
  geom_col(data = means_frame, mapping = aes(x = year, y = mean), fill = NA, colour = "red", width = 1) + labs(x = "Year", y = "Mean Life Expectancy (in years)")

----------------------------------------------------------------------------------------------------------

#Th file 'years_means.csv' includes two columns: "year" and the corresponding "mean_life-length"
years_means <- read.csv('years_means.csv')

#The graph will show the development in averge life-expectancy from 1820 to 1920
ggplot() +
  geom_point(data = years_means, mapping = aes(x = year, y = lifetime_mean), colour = 'red') + labs(x = "Year", y = "Mean Life Expectancy (in years)") +
  theme(plot.margin=unit(c(0.5,1,0.5,0.5),"cm"))